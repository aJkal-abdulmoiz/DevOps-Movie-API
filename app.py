from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
TMDB_API_KEY = os.getenv('TMDB_API_KEY')



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

if __name__ == '__main__':
    app.run(debug=True)