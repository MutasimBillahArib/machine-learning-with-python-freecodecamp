# 📩 Neural Network SMS Spam Classifier

This project is a **deep learning-based binary text classifier** that detects whether an SMS message is **spam** or **ham (not spam)**. It uses a **Bidirectional LSTM neural network** built with **TensorFlow** and trained on a real-world dataset of labeled SMS messages.


## 📌 Project Overview

- **Goal**: Automatically classify SMS messages as **spam** or **ham**
- **Approach**: Use a **Bidirectional LSTM** neural network with **text vectorization** and **embedding**
- **Dataset**: Provided by **freeCodeCamp**, includes labeled **training** and **validation** SMS message data


## 🧠 Model Architecture

The classifier uses the following architecture:

```
Input (string)
│
├── TextVectorization (tokenization & padding)
├── Embedding Layer (5000 tokens, 64-dim)
├── BiLSTM (64 units, return_sequences=True)
├── BiLSTM (32 units)
├── Dense (64 units, ReLU) + Dropout
├── Dense (32 units, ReLU) + Dropout
└── Output: Dense (1 unit, Sigmoid)
```

- **Loss Function**: Binary Crossentropy  
- **Optimizer**: Adam (`learning_rate=0.0005`)  
- **Training**: Up to **30 epochs** with **EarlyStopping** to prevent overfitting


## 📁 Dataset

The dataset is split into two **TSV (Tab-Separated Values)** files:

- `train-data.tsv`: Contains training samples with labels and SMS messages
- `valid-data.tsv`: Contains validation samples for model evaluation

Each file follows this format:

| label | text                           |
|-------|--------------------------------|
| ham   | Hey, how are you?              |
| spam  | You've won a free iPhone! Click here. |

- Labels:  
  - `ham` → not spam  
  - `spam` → unwanted or promotional message


## 📈 Evaluation

Model is validated on a held-out test set using accuracy. A built-in testing function checks if predictions align with expected output.

Example evaluation output:

```
You passed the challenge. Great job!
```

## 🧪 Example Prediction

You can run predictions with:

```
predict_message("how are you doing today?")
```

Output:

```
[0.03, 'ham']
```


## 🧰 Key Concepts Covered

- **Natural Language Processing (NLP)**
- **Text Vectorization and Tokenization**
- **Bidirectional LSTM Networks**
- **Binary Classification with Deep Learning**
- **Model Evaluation and Inference**


## 📬 Let's Connect

I'm always open to feedback, collaboration, or career opportunities!

🔗 [LinkedIn](https://www.linkedin.com/in/mmbillah804/)  
🔗 [GitHub](https://github.com/mmbillah804)
