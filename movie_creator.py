import webbrowser

class Movie():
    def __init__(self, title, year, storyline, director, actors, rating, poster, trailer):
        self.title = title
        self.year = year
        self.storyline = storyline
        self.director = director
        self.actors = actors
        self.rating = rating
        self.poster = poster
        self.trailer = trailer

    def open_trailer(self):
        webbrowser.open(self.trailer)
