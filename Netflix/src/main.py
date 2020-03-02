from library import Library
from movie_scraper import getMovies

lib = Library()

url = "https://reelgood.com/movies/source/netflix"

movies = getMovies(url)
lib.addMovies(movies)
lib.showMovies()