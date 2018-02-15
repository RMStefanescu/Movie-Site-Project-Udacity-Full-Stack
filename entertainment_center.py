import webbrowser


class Movie():
    def __init__(self, title, year, story, direct, act, rate, poster, trailer):
        self.title = title
        self.year = year
        self.storyline = story
        self.director = direct
        self.actors = act
        self.rating = rate
        self.poster = poster
        self.trailer = trailer

    def open_trailer(self):
        webbrowser.open(self.trailer)
