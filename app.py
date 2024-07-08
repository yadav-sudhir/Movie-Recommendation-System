import streamlit as st
import pickle

# Load the movie list and similarity matrix
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list['title']  # Assuming 'title' is a column in your DataFrame

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    # Ensure movies_list is accessed as a global variable
    global movies_list
    
    # Find the index of the selected movie in movies_list
    movie_index = movies_list[movies_list == movie].index[0]
    
    # Get similarity scores for the selected movie
    distances = similarity[movie_index]
    
    # Sort and get the indices of most similar movies
    similar_movies_indices = sorted(range(len(distances)), key=lambda x: distances[x], reverse=True)[1:6]
    
    # Get the titles of recommended movies
    recommended_movies = [movies_list[i] for i in similar_movies_indices]
    
    return recommended_movies

# Streamlit interface
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie', movies_list)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for movie in recommendations:
        st.write(movie)
