<<<<<<< HEAD
from flask import Flask, render_template, request
from model import recommend, movies

app = Flask(__name__) 

@app.route('/')
def home():
    movie_list = sorted(movies['title'].values)

    return render_template(
        'index.html',
        movies=movie_list   # left "movies" is the placeholder for the html file
    )

@app.route('/recommend', methods=['POST'])
def get_recommendation():

    selected_movie = request.form['movie']

    recommendations, recommendations_movies_posters = recommend(selected_movie)

    return render_template(
        'index.html',
        movies=sorted(movies['title'].values),
        recommendations=recommendations,
        selected_movie=selected_movie,
        recommendations_movies_posters=recommendations_movies_posters
    )

if __name__ == "__main__":
=======
from flask import Flask, render_template, request
from model import recommend, movies

app = Flask(__name__) 

@app.route('/')
def home():
    movie_list = sorted(movies['title'].values)

    return render_template(
        'index.html',
        movies=movie_list   # left "movies" is the placeholder for the html file
    )

@app.route('/recommend', methods=['POST'])
def get_recommendation():

    selected_movie = request.form['movie']

    recommendations, recommendations_movies_posters = recommend(selected_movie)

    return render_template(
        'index.html',
        movies=sorted(movies['title'].values),
        recommendations=recommendations,
        selected_movie=selected_movie,
        recommendations_movies_posters=recommendations_movies_posters
    )

if __name__ == "__main__":
>>>>>>> b3efb828cf32f899054b6484e0a7c6f4baa778a9
    app.run(debug=True)