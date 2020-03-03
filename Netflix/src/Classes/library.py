class Library:

    def __init__(self, movies=[]):
        self.movies = movies

    def addMovie(self, movie):
        self.movies.append(movie)

    def addMovies(self, movies):
        for movie in movies:
            self.movies.append(movie)

    def showMovies(self):
        for movie in self.movies:
            movie.showFullDesc()
