import pickle
import pandas as pd
import requests
import time

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

indices = pd.Series(
    movies.index,
    index=movies['title']
).drop_duplicates()

def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=13cf3587f132337dc3b9c3728695ec5a&language=en-US',
            timeout=10
        )

        data = response.json()

        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "/static/placeholder.jpg"

    except Exception as e:
        print("ERROR:", e)
        return "/static/placeholder.jpg"

def recommend(movie):

    # Get index of the movie
    index = indices[movie]

    # Similarity scores
    distances = similarity[index]

    # Sort movies by similarity
    movie_list = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)

    # Remove itself and take top 5
    movie_list = movie_list[1:6]

    # Collect movie names
    recommended = []
    recommended_movies_posters = []
    for i in movie_list:
        # Getting movie_id
        movie_id = movies.iloc[i[0]]['id']

        # Fetch poster from the API
        recommended_movies_posters.append(fetch_poster(movie_id))

        # Fetch name of the movie from data base
        recommended.append(movies.iloc[i[0]].title)

    return recommended, recommended_movies_posters