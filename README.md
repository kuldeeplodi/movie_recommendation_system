#🎬 Movie Recommendation System
###A content-based movie recommendation web application built using Python, Streamlit, and Scikit-learn. Just select a movie and get 6 similar movie suggestions along with their posters — thanks to the TMDb API.


#🚀 Live Demo
🔗 Click here to try the live app

#📌 Features
🔍 Search and select a movie from the dropdown

🤖 See 6 recommended movies based on content similarity

🖼️ Get posters via TMDb API

🧠 Cosine similarity-based recommendations

☁️ Deployed on Render

🔐 API key management using environment variables

🛠️ Tech Stack
Layer	Tools Used
Frontend	Streamlit
Backend	Python, Scikit-learn, Pandas
Deployment	Render (Cloud PaaS)
Storage	GitHub Releases (for large files)
API	TMDb API

🧠 How It Works
Data: The app loads movie_dict.pkl (a dictionary of movie metadata) and similarity.pkl (cosine similarity matrix).

Select Movie: User selects a movie title from the dropdown.

Recommend: Backend finds top 6 most similar movies using content-based filtering.

Posters: Posters are fetched via the TMDb API using the movie's ID.

Display: Results are displayed in columns using Streamlit.

📂 Project Structure
bash
Copy
Edit
.
├── app.py              # Main Streamlit app
├── setup.sh            # Render deployment script to fetch large files
├── requirements.txt    # Python dependencies
├── render.yaml         # (optional) Render deployment config
🧪 Local Setup Instructions
Clone the repo

bash
Copy
Edit
git clone https://github.com/kuldeeplodi/movie_recommendation_system
cd movie_recommendation_system
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Download model files
Download these manually from GitHub Releases:

movie_dict.pkl

similarity.pkl

Set TMDb API key
Create a .env file:

env
Copy
Edit
TMDB_API_KEY=your_tmdb_bearer_token
Run the app

bash
Copy
Edit
streamlit run app.py
🛡️ Deployment Notes (Render)
Add TMDB_API_KEY in Render → Environment → Add Variable

setup.sh pulls .pkl files from GitHub Releases

Use this Start Command in Render:

bash
Copy
Edit
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
📷 Demo Preview
You can add a GIF or screenshot of the app in action here.

📘 Acknowledgements
TMDb API

Streamlit team for the fast UI engine

Scikit-learn for similarity computation

🤝 Connect with Me
👤 Kuldeep Lodi
📫 LinkedIn
💻 GitHub
