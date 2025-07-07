import streamlit as st
import pandas as pd
import pickle
import requests
import os

# Function to fetch poster

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Recommendation function
def recommend(movie):
    try:
        movie_index = movies[movies["title"] == movie].index[0]
    except IndexError:
        st.error("Selected movie not found in the dataset.")
        return [], []

    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        movie_title = movies.iloc[i[0]].title
        poster_url = fetch_poster(movie_id)
        recommended_movies.append(movie_title)
        recommended_posters.append(poster_url if poster_url else "https://via.placeholder.com/300x450?text=No+Image")

    return recommended_movies, recommended_posters


# File paths
movies_file_path = r"C:\Users\mypc\OneDrive\Desktop\asad\ml project\movie-recommend-system\movies_dict.pkl"
similarity_file_path = r"C:\Users\mypc\OneDrive\Desktop\asad\ml project\movie-recommend-system\similarity.pkl"

# Load data
if not os.path.exists(movies_file_path) or not os.path.exists(similarity_file_path):
    st.error("Required pickle files not found. Please check the file paths.")
else:
    movies_dict = pickle.load(open(movies_file_path, 'rb'))
    similarity = pickle.load(open(similarity_file_path, 'rb'))
    movies = pd.DataFrame(movies_dict)

    # Streamlit UI
    st.title("🎬 Movie Recommendation System")

    option = st.selectbox('📽️ Select a movie to get recommendations:', movies["title"].values)

    if st.button("🔎 Recommend"):
        with st.spinner("Fetching recommendations..."):
            recommended_movies, recommended_posters = recommend(option)

        if recommended_movies:
            st.subheader(f"🎥 Recommendations for: {option}")
            cols = st.columns(5)

            for i in range(5):
                with cols[i]:
                    st.text(recommended_movies[i])
                    st.image(recommended_posters[i], use_column_width=True)
            st.success("✅ Recommendations displayed successfully!")
        else:
            st.error("Could not generate recommendations.")
    else:
        st.info("Please select a movie to get recommendations.")
        st.warning("Click the '🔎 Recommend' button to see the results.")
        st.success("Ready to recommend movies!")