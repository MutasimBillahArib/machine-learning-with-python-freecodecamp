# 💸 Health Costs Predictor with Linear Regression (TensorFlow)

This project uses a **deep neural network regression model** to predict individual medical insurance expenses based on personal attributes such as **age**, **BMI**, **smoking status**, and **region**. Built with **TensorFlow** and **Keras**, the model learns to map relationships between user data and healthcare costs.


## 📌 Project Overview

- **Objective**: Predict insurance expenses (in USD) for individuals using demographic and health-related features.
- **Model Type**: Multi-layer feedforward neural network for **regression**.
- **Dataset**: Provided by **freeCodeCamp**, based on real-world medical cost data.


## 📊 Dataset Features

The dataset includes the following columns:

| Feature   | Description                                           |
|-----------|-------------------------------------------------------|
| `age`     | Age of the individual (in years)                      |
| `sex`     | Gender (`0 = female`, `1 = male`)                     |
| `bmi`     | Body Mass Index                                       |
| `children`| Number of children covered by insurance               |
| `smoker`  | Smoker status (`0 = no`, `1 = yes`)                   |
| `region`  | Residential area (`0–3`, categorical)                 |
| `expenses`| **Target variable** – medical costs in USD            |


## 🧪 Workflow

### 1. 🔄 Data Preprocessing

- Label encoding for categorical variables: `sex`, `smoker`, `region`
- Data split into:
  - **Training Set**: 80%
  - **Testing Set**: 20%
- Features and target (`expenses`) separated for model input


### 2. 🧠 Model Architecture

A **simple feedforward neural network** built with Keras:

```python
Sequential([
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1)
])
```

---

### 3. ⚙️ Model Configuration

- **Loss**: Mean Squared Error (MSE)  
- **Optimizer**: RMSprop  
- **Metrics**:  
  - Mean Absolute Error (MAE)  
  - Mean Squared Error (MSE)


### 4. 🏋️‍♂️ Training

- Trained over **1000 epochs**
- Uses a **20% validation split**
- **Silent training** enabled using `tfdocs.modeling.EpochDots()` callback for clean logging


## 📈 Evaluation

- Evaluated using the test dataset
- Metric: **Mean Absolute Error (MAE)**

```
Testing set Mean Abs Error: 3448.99 expenses
You passed the challenge. Great job!
```
The goal is to keep MAE below $3500.

## 🔍 Prediction Plot

Compares predicted vs. actual medical expenses:
