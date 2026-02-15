import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8124f2c79d43c248fd8af8fe030151a4&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(selected_movie_name):
    movie_index = movies[movies['title']==selected_movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #Fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return recommended_movies,posters


movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Select a movie from the dropdown',
    movies['title'].values
)

if st.button('Recommend'):
    recommended_movies, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(posters[1])
    with col3:
        st.text(recommended_movies[2])
        st.image(posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(posters[4]) 