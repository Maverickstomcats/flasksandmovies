from flask import Flask
import json
app = __name__
@app.route("/")
def home():
    # passes stuff to the move and genre data to 'home.html' i think 
    pass

@app.route("/movie/<title>")
def movie_detail(title):
    #retrieve stuff and pass selected movie details to 'movie_detail.html'
    pass

@app.route("/genre/<genre_name>")
def genre_page(genre_name):
    # retrieve and pass all movies of the selected genre to genre_page.html
    pass

