# Movie Recommendation Site

This is a Flask web application that provides movie recommendations using the TMDB (The Movie Database) API. You can fetch popular movies, search for movies by title, and get movie recommendations based on genre and country.

## Table of Contents

1. [Requirements](#requirements)
2. [Setup](#setup)
3. [API Usage](#api-usage)
    - [Using cURL or Postman](#using-curl-or-postman)
    - [Using cURL and Frontend](#using-curl-and-frontend)
4. [Running the Application](#running-the-application)
5. [License](#license)

## Requirements

- Python 3.x
- Flask
- Requests
- python-dotenv

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/aJkal-abdulmoiz/DevOps-Movie-Recommendtion-API.git
   cd DevOps-Movie-Recommendtion-API

pip install -r requirements.txt

TMDB_API_KEY=your_tmdb_api_key

API Usage
Using cURL or Postman
You can interact with the API endpoints using cURL or Postman.

Popular Movies
cURL Request:

 bash
Copy code
curl -X GET "http://127.0.0.1:5000/movies/popular"


Postman Request:

Open Postman.
Create a new GET request to http://127.0.0.1:5000/movies/popular.
Click on Send.

Search Movies by Title
cURL Request:

 bash
Copy code
curl -X GET "http://127.0.0.1:5000/movies?title=Inception"

Postman Request:

Open Postman.
Create a new GET request to http://127.0.0.1:5000/movies?title=Inception.
Click on Send.


Get Movie Recommendations
cURL Request:
 ```bash
Copy code
curl -X GET "http://127.0.0.1:5000/movies/recommend?genre=Action&country=US"


Postman Request:

Open Postman.
Create a new GET request to http://127.0.0.1:5000/movies/recommend?genre=Action&country=US.
Click on Send.