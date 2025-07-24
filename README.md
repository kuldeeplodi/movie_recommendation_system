# 🎮 Movie Recommendation System

A content-based movie recommendation web application built using **Python**, **Streamlit**, and **Scikit-learn**. Just select a movie and get 6 similar movie suggestions along with their posters — thanks to the TMDb API.

---

## 🚀 Live Demo

🔗 [Click here to try the live app](https://your-render-app-url.com)

---

## 📌 Features

- 🔍 Search and select a movie from the dropdown
- 🤖 See **6 recommended movies** based on content similarity
- 🖼️ Get posters via **TMDb API**
- 🧠 Cosine similarity-based recommendations
- ☁️ **Deployed on Render**
- 🔐 API key management using environment variables

---

## 🛠️ Tech Stack

| Layer          | Tools Used                              |
| -------------- | --------------------------------------- |
| **Frontend**   | Streamlit                               |
| **Backend**    | Python, Scikit-learn, Pandas            |
| **Deployment** | Render (Cloud PaaS)                     |
| **Storage**    | GitHub Releases (for large files)       |
| **API**        | [TMDb API](https://www.themoviedb.org/) |

---

## 🧠 How It Works

1. **Data**: The app loads `movie_dict.pkl` (a dictionary of movie metadata) and `similarity.pkl` (cosine similarity matrix).
2. **Select Movie**: User selects a movie title from the dropdown.
3. **Recommend**: Backend finds top 6 most similar movies using content-based filtering.
4. **Posters**: Posters are fetched via the TMDb API using the movie's ID.
5. **Display**: Results are displayed in columns using Streamlit.

---

## 📂 Project Structure

```
.
├── app.py              # Main Streamlit app
├── setup.sh            # Render deployment script to fetch large files
├── requirements.txt    # Python dependencies
├── render.yaml         # (optional) Render deployment config
```

---

## 🧪 Local Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/kuldeeplodi/movie_recommendation_system
   cd movie_recommendation_system
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download model files**\
   Download these manually from [GitHub Releases](https://github.com/kuldeeplodi/movie_recommendation_system/releases):

   - `movie_dict.pkl`
   - `similarity.pkl`

4. **Set TMDb API key**\
   Create a `.env` file:

   ```env
   TMDB_API_KEY=your_tmdb_bearer_token
   ```

5. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## ⚡ Deployment Notes (Render)

- Add `TMDB_API_KEY` in **Render → Environment → Add Variable**
- `setup.sh` pulls `.pkl` files from GitHub Releases
- Use this **Start Command** in Render:

```bash
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

---

## 📷 Demo Preview

> Add a GIF or screenshot of the app in action here if available.

---

## 📘 Acknowledgements

- [TMDb API](https://developers.themoviedb.org/)
- Streamlit for UI
- Scikit-learn for similarity computation

---

## 🤝 Connect with Me

👤 **Kuldeep Lodi**\
📧 [LinkedIn](https://www.linkedin.com/in/kuldeep-lodi)\
💻 [GitHub](https://github.com/kuldeeplodi)

