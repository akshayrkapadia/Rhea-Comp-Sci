from Classes.library import Library
from movie_scraper import getAllMovies

lib = Library()

url = "https://reelgood.com/movies/source/netflix"

movies = getAllMovies(url)
lib.addMovies(movies)
lib.showMovies()
