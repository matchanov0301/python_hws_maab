import requests
import random

# Replace with your actual API key from https://developer.themoviedb.org/docs/getting-started
API_KEY = "4fd0e75e2126f206c910f257c5879749"
BASE_URL = "https://api.themoviedb.org/3"

def get_genre_id(genre_name):
    """Fetch genre ID using the provided API link."""
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url).json()

    for genre in response.get("genres", []):
        if genre_name.lower() == genre["name"].lower():
            return genre["id"]
    return None

def get_movies_by_genre(genre_id):
    """Fetch movies using the link from the task description."""
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url).json()
    return response.get("results", [])

def recommend_movie():
    """Ask user for a genre and recommend a random movie."""
    genre_name = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
    genre_id = get_genre_id(genre_name)

    if not genre_id:
        print("❌ Invalid genre! Try again.")
        return

    movies = get_movies_by_genre(genre_id)

    if not movies:
        print("❌ No movies found for this genre.")
        return

    movie = random.choice(movies)
    print("\n🎬 **Recommended Movie:**")
    print(f"Title: {movie['title']}")
    print(f"Overview: {movie['overview']}")
    print(f"Rating: {movie['vote_average']}/10")
    print(f"More Info: https://www.themoviedb.org/movie/{movie['id']}")

# Run the program
recommend_movie()
