import streamlit as st
import pickle
import pandas as pd


import requests
import os

# Load environment variable
TMDB_API_KEY = os.getenv("TMDB_API_KEY")




def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?language=en-US"
     headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4YjRhYTQzMmM0ZTc5MjU1NTQxNzJlYTZhOTFkMzY0YiIsIm5iZiI6MTc1MzIxMDc1NS43NDcsInN1YiI6IjY4N2ZkZjgzNDlmOWE0ZTZlZjcyZDU4MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.WO4k03mD0sMm-Xo6-5Luqq0ShFycL8qI13s1Wmk5hiY"
     }
     response = requests.get(url.format(movie_id), headers=headers)
     data=response.json()
     return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']





def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[0:6]

    recommended_movies=[]
    recommended_movies_posters=[]
   
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
      

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))
st.title("movie recommender system")

selected_movie_name=st.selectbox("How would you like to be contacted?",movies['title'].values)

if st.button('Recommend'):
    name,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5,col6=st.columns(6)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
        st.text(name[4])
        st.image(posters[4])
    with col6:
        st.text(name[5])
        st.image(posters[5])
   



