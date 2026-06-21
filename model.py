import pickle
import pandas as pd

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

indices = pd.Series(
    movies.index,
    index=movies['title']
).drop_duplicates()

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
    for i in movie_list:
        recommended.append(movies.iloc[i[0]].title)

    return recommended