# 📚 Book Recommendation Engine using KNN

This is a **collaborative filtering-based** book recommendation engine built using the **K-Nearest Neighbors (KNN)** algorithm and **cosine similarity**. It recommends similar books based on user rating patterns and is powered by the [Book-Crossing](https://www.bookcrossing.com/) Dataset.


## 📌 Project Overview

- **Goal**: Recommend books similar to a given title by finding books with similar user rating patterns.
- **Technique**: Item-based collaborative filtering using **KNN** and **sparse matrix computation**.
- **Tools Used**: `pandas`, `numpy`, `scikit-learn`, `scipy`, `matplotlib`


## 📁 Dataset Description

This project uses the **Book-Crossing Dataset**, consisting of:

- `BX-Books.csv`: Book metadata including ISBN, title, and author
- `BX-Book-Ratings.csv`: User-submitted ratings for books

The dataset is **downloaded and extracted automatically** via script commands.


## ⚙️ How It Works

### 1. 🧹 Data Preprocessing

- Filters:
  - Users who rated **200+ books**
  - Books that received **100+ ratings**
- Merges rating data with book metadata
- Creates a **user-item matrix** (pivot table) with books as rows and users as columns

### 2. 🧮 Sparse Matrix Creation

- Converts the pivot table to a **Compressed Sparse Row (CSR)** matrix for memory efficiency

### 3. 🔍 KNN Model

- Trained using:
  - **Cosine distance**
  - **Brute-force search**
- Finds **nearest neighbors** (most similar books) to the query book

### 4. 📖 Recommendation Output

- Returns **Top 5 recommended books** (excluding the query book)
- Displays **cosine distance** (lower = more similar)

---

## 🧪 Example

```python
books = get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))")
print(books)
```

Output:

```python
[
  "Where the Heart Is (Oprah's Book Club (Paperback))",
  [
    ["I'll Be Seeing You", 0.80],
    ["The Weight of Water", 0.77],
    ["The Surgeon", 0.77],
    ["I Know This Much Is True", 0.77],
    ["The Lovely Bones: A Novel", 0.75]
  ]
]
```


## 🧪 Evaluation

A simple test is included to verify the correctness of the KNN-based recommendation system by manually inspecting returned book titles for known examples.

```python
test_book_recommendation()
```

Output:

```python
You passed the challenge! 🎉🎉🎉🎉🎉
```


> 📘 This project showcases how collaborative filtering and KNN can be used for real-world recommendation systems with large-scale datasets.

