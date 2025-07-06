# 🪨📄✂️ Rock Paper Scissors Strategy Bot

This is a Python implementation of an intelligent **Rock, Paper, Scissors (RPS)** bot designed to compete in adaptive environments by identifying and exploiting patterns in opponent behavior. The strategy combines rule-based decision-making, opponent modeling, and frequency analysis to **maximize win rate over time**.


## 🚀 Features

- **Pattern Detection**: Recognizes fixed cycles like those used by the "Quincy" bot.
- **Opponent Modeling**: Simulates the internal state of other bots (especially “Abbey”) and counters them effectively.
- **Fallback Strategy**: Uses simple heuristics like repeated move detection, cycling behavior, and frequency-based predictions when no specific pattern is identified.
- **Self-Learning**: Maintains internal history of both its own and the opponent's moves for intelligent future decisions.


## 🧠 Strategy Overview

- **Opening Move**: Always starts with `'R'`.
- **Detect Quincy**: Checks for repeating sequences of 5 moves in the opponent's history.
- **Simulate Abbey**: Reconstructs Abbey's 2-gram model based on our past moves to predict and counter Abbey's next action.

### Behavioral Heuristics:

- Counters repeated opponent moves.
- Detects rock-paper-scissors style 3-cycles.
- Detects opponents who always try to beat our last move.
- **Fallback**: Predicts opponent’s most frequent move and plays the counter.


## 🧩 Key Concepts

- **2-gram frequency tracking**: Used to simulate Abbey's predictive model.
- **Opponent profiling**: Dynamic classification of opponents based on recent behavior.
- **Adaptive responses**: The bot modifies its strategy in real-time based on observed opponent patterns.


## 🧪 Testing & Benchmarking

This bot was designed to compete in pattern-based RPS environments, such as the **freeCodeCamp Rock, Paper, Scissors Challenge**. It performs especially well against scripted bots like **Quincy**, **Kris**, and **Abbey**, thanks to its built-in detection mechanisms.


> 🎯 The project demonstrates how simple game strategies can evolve into complex adaptive systems with elements of learning, prediction, and real-time decision-making.
