from flask import Flask, render_template, request
from model import recommend, movies

app = Flask(__name__) 

@app.route('/')
def home():
    movie_list = movies['title'].values

    return render_template(
        'index.html',
        movies=movie_list   # left "movies" is the placeholder for the html file
    )

@app.route('/recommend', methods=['POST'])
def get_recommendation():

    selected_movie = request.form['movie']

    recommendations = recommend(selected_movie)

    return render_template(
        'index.html',
        movies=movies['title'].values,
        recommendations=recommendations,
        selected_movie=selected_movie
    )

if __name__ == "__main__":
    app.run(debug=True)