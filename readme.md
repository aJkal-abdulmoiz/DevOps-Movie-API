# DevOps Movie Recommendation API

## Contributors

- **Abdul Moiz:** Backend API development and endpoints.(backend)
- **Rayan:** Frontend development.(frontend)
- **Abdullah:** Testing and quality assurance.(testing)


## Purpose
The DevOps Movie Recommendation API is designed to provide users with a seamless experience in retrieving popular movies, searching for movies by title, and receiving movie recommendations based on genre and country. This API serves as a backend service for various applications, enhancing user engagement through personalized content.

## Requirements

- Python 3.x
- Flask
- Requests
- python-dotenv

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aJkal-abdulmoiz/DevOps-Movie-Recommendtion-API.git
   cd DevOps-Movie-Recommendtion-API



2. **Set up environment variables: Create a .env file in the root directory and add your TMDB API key::**
   ```bash
    TMDB_API_KEY=your_tmdb_api_key

3. **Install the required dependencies:**
   ```bash
    pip install -r requirements.txt


# API Usage

You can interact with the API endpoints using cURL or Postman.

### Using cURL

1. **Popular Movies: To get popular movies, use the following cURL command:**
   ```bash
    curl -X GET "http://127.0.0.1:5000/movies/popular"


2. **Search Movies by Title: To search for a movie by title, use:**
   ```bash
    curl -X GET "http://127.0.0.1:5000/movies?title=Inception"


3. **Get Movie Recommendations: To get recommendations based on genre and country, use::**
   ```bash
    curl -X GET "http://127.0.0.1:5000/movies/recommend?genre=Action&country=US"


### Using Postman


Create a new GET request for each endpoint:

1. **Open Postman**

2. **Create a new GET request for each endpoint:**


- **Popular Movies**:
   ```bash
    http://127.0.0.1:5000/movies/popular
   
![image](https://github.com/aJkal-abdulmoiz/DevOps-Movie-Recommendtion-API/blob/f5ceb5033e0fad9db1be3036ca3b16c4d008a0ce/assets/images/popular-endpoint-json-response.png)
   
- **Search Movies by Title:**:
   ```bash
    http://127.0.0.1:5000/movies?title=Inception
   
![image](https://github.com/aJkal-abdulmoiz/DevOps-Movie-Recommendtion-API/blob/f5ceb5033e0fad9db1be3036ca3b16c4d008a0ce/assets/images/movies-titleendpoint-json-response.png)
   
    
- **Get Movie Recommendations::**:
   ```bash
    http://127.0.0.1:5000/movies/recommend?genre=Action&country=US

![image](https://github.com/aJkal-abdulmoiz/DevOps-Movie-Recommendtion-API/blob/f5ceb5033e0fad9db1be3036ca3b16c4d008a0ce/assets/images/get-recommendation-endpoint-json-response.png)
    

3. **Click on Send.:**


# Frontend

## Starting the Flask Application: Run the application using:

- **Get Movie Recommendations::**:
   ```bash
    python app.py

- ####  **Accessing the Frontend**: Open your web browser and go to http://127.0.0.1:5000/. You will see a simple interface to interact with the movie API.

## Using the Frontend:

- **Search by Title:** Click on this option to search for a movie by its title.

![image](https://github.com/aJkal-abdulmoiz/DevOps-Movie-Recommendtion-API/blob/f5ceb5033e0fad9db1be3036ca3b16c4d008a0ce/assets/images/search-by-title.png)
  
- **See Popular Movies:** Click here to view the top popular movies.

![image](https://github.com/aJkal-abdulmoiz/DevOps-Movie-Recommendtion-API/blob/f5ceb5033e0fad9db1be3036ca3b16c4d008a0ce/assets/images/popular-movies.png)
  
- **Get Recommendations:** Click to get movie recommendations based on genre and country.

![image](https://github.com/aJkal-abdulmoiz/DevOps-Movie-Recommendtion-API/blob/f5ceb5033e0fad9db1be3036ca3b16c4d008a0ce/assets/images/get-recommendations.png)





    
