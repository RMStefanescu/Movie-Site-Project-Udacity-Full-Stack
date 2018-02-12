import webbrowser


class Movie():
    def __init__(self, title, realease_date, storyline, rating, poster, trailer):
        self.title = title
        self.release_date = realease_date
        self.storyline = storyline
        self.rating = rating
        self.poster = poster
        self.trailer = trailer

    def open_trailer(self):
        webbrowser.open(self.trailer)
