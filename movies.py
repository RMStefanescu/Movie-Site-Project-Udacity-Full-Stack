import movie_creator
import razvans_movie_site


the_godfather = movie_creator.Movie("The Godfather", "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.", "Francis Ford Coppola", ["Marlon Brando", "Al Pacino", "James Caan"], 9.2, "https://images-na.ssl-images-amazon.com/images/M/MV5BY2Q2NzQ3ZDUtNWU5OC00Yjc0LThlYmEtNWM3NTFmM2JiY2VhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,700,1000_AL_.jpg", "http://www.imdb.com/title/tt0068646/videoplayer/vi1348706585")

movies = [the_godfather]

razvans_movie_site.open_movies_page(movies)
