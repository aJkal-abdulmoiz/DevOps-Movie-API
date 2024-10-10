from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
TMDB_API_KEY = os.getenv('TMDB_API_KEY')


#MOvie Search Endpoint

@app.route('/movies', methods=['GET'])
def search_movies():
    title = request.args.get('title')
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=5, type=int)

    if not title:
        return jsonify({"error": "Title is required"}), 400  # Error handling for missing title

    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}&page={page}"
    response = requests.get(url)
    data = response.json()

    movies = []
    for movie in data.get('results', [])[:limit]:
        movies.append(
            {
            
            'title': movie['title'],
            'description': movie['overview'],
            'rating': movie['vote_average'],
            'image': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie['poster_path'] else None
            }
        )
    
    return jsonify(movies)


#Movie recommendation Endpoint
@app.route('/movies/recommend', methods=['GET'])
def recommend_movies():
    genre = request.args.get('genre')
    country = request.args.get('country')
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=5, type=int)

    # Use TMDB API to recommend movies based on genre and country
    genre_id = get_genre_id(genre)
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&page={page}"
    if genre_id:
        url += f"&with_genres={genre_id}"
    if country:
        url += f"&region={country}"

    response = requests.get(url)
    data = response.json()

    movies = []
    for movie in data.get('results', [])[:limit]:
        movies.append({
            'title': movie['title'],
            'description': movie['overview'],
            'rating': movie['vote_average'],
            'image': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie['poster_path'] else None
        })
    
    return jsonify(movies)


def get_genre_id(genre_name):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}"
    response = requests.get(url)
    genres = response.json().get('genres', [])
    for genre in genres:
        if genre['name'].lower() == genre_name.lower():
            return genre['id']
    return None


#Popular Movie Endpoint
@app.route('/movies/popular', methods=['GET'])
def popular_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    data = response.json()

    movies = []
    for movie in data.get('results', [])[:5]:  # Limit to top 5 popular movies
        movies.append({
            'title': movie['title'],
            'description': movie['overview'],
            'rating': movie['vote_average'],
            'image': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie['poster_path'] else None
        })

    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True)