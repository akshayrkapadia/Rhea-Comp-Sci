class Movie:

    def __init__(self, title, year, rating, link):
        self.title = title
        self.year = year
        self.rating = rating
        self.link = link

    def showFullDesc(self):
        print(self.title, "(" + self.year + ")", "|", "Rating:", self.rating, "|", self.link)