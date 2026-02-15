# 🎬 Movie Recommender System

A content-based Movie Recommender System built using Python and Streamlit.
It suggests movies similar to the selected title and displays posters using the TMDB API.

---

## 🚀 Live Demo

🔗 https://movie-recommender-system-82fs.onrender.com

---

## 📌 Features

- Content-based recommendation system
- Cosine similarity model
- Top 5 similar movie suggestions
- Movie posters fetched from TMDB API
- Clean Streamlit UI
- Secure API key using Streamlit Secrets

---

## 🛠 Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- TMDB API

---

## 📂 Project Structure

movie-recommender-system/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
└── README.md



---

## ⚙️ How It Works

1. Movie metadata is vectorized using CountVectorizer.
2. Cosine similarity is calculated between movie vectors.
3. Top 5 similar movies are retrieved.
4. Posters are fetched using TMDB API.

---

## 🔐 Security

The TMDB API key is securely stored using Streamlit Secrets and is not exposed in the repository.

---

## 👨‍💻 Author

Shivansh Srivastava
