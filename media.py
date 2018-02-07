import movie_creator
import razvans_movie_site


the_godfather = movie_creator.Movie("The Godfather", 1972, "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.", "Francis Ford Coppola", ["Marlon Brando", "Al Pacino", "James Caan"], 9.2, "https://images-na.ssl-images-amazon.com/images/M/MV5BY2Q2NzQ3ZDUtNWU5OC00Yjc0LThlYmEtNWM3NTFmM2JiY2VhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,700,1000_AL_.jpg", "https://www.youtube.com/watch?v=sY1S34973zA")
the_godfather_2 = movie_creator.Movie("The Godfather part 2", 1974, "The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.", "Francis Ford Coppola", ["Al Pacino", "Robert Duvall", "Diane Keaton", "Robert deNiro"], 9.0, "https://images-na.ssl-images-amazon.com/images/M/MV5BMjZiNzIxNTQtNDc5Zi00YWY1LThkMTctMDgzYjY4YjI1YmQyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,702,1000_AL_.jpg", "https://www.youtube.com/watch?v=9O1Iy9od7-A")
the_godfather_3 = movie_creator.Movie("The Godfather part 3", 1990, "In the midst of trying to legitimize his business dealings in New York City and Italy in 1979, aging Mafia Don Michael Corleone seeks to avow for his sins, while taking his nephew Vincent Mancini under his wing.", "Francis Ford Coppola", ["Al Pacino", "Diane Keaton", "Andy Garcia"], 7.6, "https://images-na.ssl-images-amazon.com/images/M/MV5BY2YzNTUzZjUtYmQyMi00YTg3LWIxNGYtMmY2ZWRmOGY3ZTg4XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg", "https://www.youtube.com/watch?v=z8h3LVb8cl8")
movies = [the_godfather, the_godfather_2, the_godfather_3]

razvans_movie_site.open_movies_page(movies)
