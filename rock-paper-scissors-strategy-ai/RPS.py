import random
from collections import Counter

def _beats(move):
    """Return the move that beats the given one."""
    return {'R': 'P', 'P': 'S', 'S': 'R'}[move]

def player(prev_play,
           opponent_history=[],
           my_history=[],
           # For simulating Abbey’s internal state:
           abbey_opp_history=[],
           abbey_play_order=[{
               "RR": 0, "RP": 0, "RS": 0,
               "PR": 0, "PP": 0, "PS": 0,
               "SR": 0, "SP": 0, "SS": 0,
           }]):
    """
    prev_play: the opponent’s last move ('R','P','S') or '' for the first round
    opponent_history: all actual opponent moves seen so far
    my_history:       all our past moves
    abbey_opp_history: simulated “opponent_history” as Abbey would see it (i.e. our moves),
                        including Abbey’s dummy 'R' on its first turn
    abbey_play_order: simulated 2‐gram counts exactly as Abbey counts them
    """

    # --- 1) On first round (prev_play == ""), reset all histories for a fresh match. ---
    if prev_play == "":
        opponent_history.clear()
        my_history.clear()
        abbey_opp_history.clear()
        # Reset Abbey’s 2‐gram counts to zero:
        abbey_play_order[0] = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0,
        }
        # Abbey’s very first “prev” is forced to 'R':
        abbey_opp_history.append("R")

        # We can choose anything for our opening move; pick 'R':
        choice = "R"
        my_history.append(choice)

        # **Simulate** Abbey appending our 'R' and updating its play_order (for the next round).
        abbey_opp_history.append(choice)  # now ['R','R']
        abbey_play_order[0]["RR"] += 1

        return choice

    # --- 2) Not the first round: record opponent’s last move. ---
    opponent_history.append(prev_play)

    # --- 3) Helper: Detect “Quincy” by checking for a repeating block of length 5. ---
    def detect_quincy(hist):
        """
        True if, in the last 10 moves, the last 5 exactly repeat the previous 5
        (i.e. a period‐5 cycle). Quincy’s sequence is length 5 (R,P,P,S,R → repeat).
        """
        if len(hist) < 10:
            return False
        return hist[-5:] == hist[-10:-5]

    # --- 4) If we see a 5‐cycle, assume “Quincy.”  Predict Quincy’s next and counter it. ---
    if detect_quincy(opponent_history):
        # Quincy’s cycle is exactly: ['R','P','P','S','R'], repeating.
        # But since it starts with a shift (its “counter” array is [R,R,P,P,S]),
        # the actual first‐five will be:   R,  P,  P,  S,  R  (then repeat).
        # We can just read off the last 5 and index by (len % 5).
        seq = opponent_history[-5:]
        idx = len(opponent_history) % 5
        quincy_next = seq[idx]
        choice = _beats(quincy_next)
        my_history.append(choice)

        # **Simulate** Abbey’s state update (in case we face Abbey later; harmless otherwise):
        abbey_opp_history.append(choice)
        if len(abbey_opp_history) >= 2:
            last_two = "".join(abbey_opp_history[-2:])
            abbey_play_order[0][last_two] += 1

        return choice

    # --- 5) Simulate what “Abbey” would play THIS round, and counter it. ---
    #
    # Abbey’s move for round T is based on our move from round T−1.  At this point,
    # abbey_opp_history already equals exactly what Abbey’s own `opponent_history`
    # would be just before its call this round.  And abbey_play_order holds the
    # correct 2‐gram counts (including the last pair).  So:
    #
    #   let prefix = abbey_opp_history[-1]  # = our (T−1)th move
    #   Abbey looks at counts for prefix+'R', prefix+'P', prefix+'S';
    #   chooses the Y with max count, predicts our next is Y, then returns _beats(Y).
    #
    def simulate_abbey_next():
        prefix = abbey_opp_history[-1]
        # Gather 2‐gram counts for “prefix → R/P/S”:
        counts = {
            "R": abbey_play_order[0].get(prefix + "R", 0),
            "P": abbey_play_order[0].get(prefix + "P", 0),
            "S": abbey_play_order[0].get(prefix + "S", 0),
        }
        # Find the move (R/P/S) with the highest count.  Tie‐break: R > P > S by list order.
        best = max(
            ["R", "P", "S"],
            key=lambda m: (counts[m], -["R", "P", "S"].index(m))
        )
        # Abbey’s actual play = the counter to “best”:
        return _beats(best)

    # We’ll attempt to use Abbey‐simulation if it “fits” the opponent’s behavior.  Check
    # how many times in the recent history Abbey‐simulation would have matched the actual move.
    def matches_abbey(hist_my, hist_opp, abb_opp_hist, abb_po):
        """
        Count how many of the last up to 10 rounds (where T≥2) satisfy:
          actual opp_move == simulate_abbey’s predicted opp_move.
        If it’s ≥ 70% of those rounds, assume Abbey.
        """
        if len(hist_my) < 2:
            return False
        # Let’s check up to the last 10 rounds:
        checks = min(len(hist_my) - 1, 10)  # because round #1 of our moves → no sim
        match = 0
        # We need a temporary copy of Abbey’s internal state and walk it forward
        # from the start, comparing each predicted move to actual.  But that’s O(n²).
        # Instead, do a “rolling” check over the last few rounds.  We’ll rebuild Abbey’s
        # state step by step for those last `checks+1` rounds.
        temp_opp = ["R"]  # Abbey’s dummy for round 1
        temp_po = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0,
        }
        # We want to simulate from round 2 up to round (N), but only check the last few.
        total_rounds = len(hist_my)  # our total moves so far
        start = max(1, total_rounds - checks)  # the earliest move index we’ll test
        for t in range(1, total_rounds):
            # In real Abbey, round t: prev_opponent_play = our move at t−1 = hist_my[t−1]
            m_prev = hist_my[t - 1]
            temp_opp.append(m_prev)
            if len(temp_opp) >= 2:
                pair = "".join(temp_opp[-2:])
                temp_po[pair] += 1
            # Abbey predicts now (for round t):
            #   prefix = temp_opp[-1]; best = argmax temp_po[prefix+R/P/S]; abbey_move = _beats(best)
            prefix = temp_opp[-1]
            cnts = {
                "R": temp_po[prefix + "R"],
                "P": temp_po[prefix + "P"],
                "S": temp_po[prefix + "S"],
            }
            predicted = max(
                ["R", "P", "S"],
                key=lambda m: (cnts[m], -["R", "P", "S"].index(m))
            )
            abbey_move = _beats(predicted)
            # Compare to *actual* opponent move at that round = hist_opp[t]
            if t >= start and abbey_move == hist_opp[t]:
                match += 1

        return (match / checks) >= 0.7

    # If we “match” Abbey’s past behavior ≥70%, assume opponent_is_abbey → use Abbey‐sim strategy:
    if matches_abbey(my_history, opponent_history, abbey_opp_history, abbey_play_order):
        abbey_choice = simulate_abbey_next()
        choice = _beats(abbey_choice)
        my_history.append(choice)

        # Update our simulation of Abbey’s state:
        abbey_opp_history.append(choice)
        if len(abbey_opp_history) >= 2:
            pair = "".join(abbey_opp_history[-2:])
            abbey_play_order[0][pair] += 1

        return choice

    # --- 6) Fallback “general” strategy (beats last, repeat‐detect, cycle‐detect, freq‐fallback) ---
    # Update Abbey’s state with whoever we ended up playing last round (to keep sim in sync):
    # (But we’ll do that below, after we pick a fallback choice.)

    # a) Very short history (first 2 actual moves): just beat their last:
    if len(opponent_history) < 2:
        choice = _beats(opponent_history[-1])
        my_history.append(choice)
        # Update Abbey’s sim-state:
        abbey_opp_history.append(choice)
        if len(abbey_opp_history) >= 2:
            pair = "".join(abbey_opp_history[-2:])
            abbey_play_order[0][pair] += 1
        return choice

    # b) If opponent just repeated twice, assume “repeat”:
    if opponent_history[-1] == opponent_history[-2]:
        choice = _beats(opponent_history[-1])
        my_history.append(choice)
        abbey_opp_history.append(choice)
        if len(abbey_opp_history) >= 2:
            pair = "".join(abbey_opp_history[-2:])
            abbey_play_order[0][pair] += 1
        return choice

    # c) Detect a 3‐cycle (R→P→S→R):
    last_two = opponent_history[-2:]
    if last_two == ["R", "P"]:
        choice = _beats("S")
        my_history.append(choice)
        abbey_opp_history.append(choice)
        if len(abbey_opp_history) >= 2:
            pair = "".join(abbey_opp_history[-2:])
            abbey_play_order[0][pair] += 1
        return choice
    if last_two == ["P", "S"]:
        choice = _beats("R")
        my_history.append(choice)
        abbey_opp_history.append(choice)
        if len(abbey_opp_history) >= 2:
            pair = "".join(abbey_opp_history[-2:])
            abbey_play_order[0][pair] += 1
        return choice
    if last_two == ["S", "R"]:
        choice = _beats("P")
        my_history.append(choice)
        abbey_opp_history.append(choice)
        if len(abbey_opp_history) >= 2:
            pair = "".join(abbey_opp_history[-2:])
            abbey_play_order[0][pair] += 1
        return choice

    # d) Detect “beat‐my‐last” (like kris does): if they just played _beats(my_last), they react to us.
    if my_history:
        if opponent_history[-1] == _beats(my_history[-1]):
            choice = random.choice(["R", "P", "S"])
            my_history.append(choice)
            abbey_opp_history.append(choice)
            if len(abbey_opp_history) >= 2:
                pair = "".join(abbey_opp_history[-2:])
                abbey_play_order[0][pair] += 1
            return choice

    # e) Fallback: frequency analysis of opponent’s entire history:
    freq = Counter(opponent_history)
    most_common = freq.most_common(1)[0][0]
    choice = _beats(most_common)
    my_history.append(choice)
    abbey_opp_history.append(choice)
    if len(abbey_opp_history) >= 2:
        pair = "".join(abbey_opp_history[-2:])
        abbey_play_order[0][pair] += 1
    return choice
