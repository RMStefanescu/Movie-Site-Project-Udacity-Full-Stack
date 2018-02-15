import webbrowser


class Movie():
    def __init__(self, title, realease, story, rating, poster, trailer):
        self.title = title
        self.release_date = realease
        self.storyline = story
        self.rating = rating
        self.poster = poster
        self.trailer = trailer

    def open_trailer(self):
        webbrowser.open(self.trailer)
