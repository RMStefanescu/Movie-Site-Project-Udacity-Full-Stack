import entertainment_center
import razvans_movie_site

# Iterates through text file and saves movie info that occurs after the M: tag
with open("media_data.txt", "r") as file_input:
    # Media array to store movie elements
    media = []
    for element in file_input:
        if element.startswith("M:"):
            # Adds movie elements to array after second character
            media.append(element[1:])

# VERSION 1 - static creation of movie objects
# Creates new arrays that contain only the first movie, with the index of 0
# and separates the values by the | separator
media1 = media[0].split("|")
media2 = media[1].split("|")
media3 = media[2].split("|")
media4 = media[3].split("|")
# Creates objects with the *args - sends all non-keyworded
# variable lenght arguments list to new Movie instance
the_godfather = entertainment_center.Movie(*media1)
the_godfather_2 = entertainment_center.Movie(*media2)
the_godfather_3 = entertainment_center.Movie(*media3)
lord_of_the_rings_1 = entertainment_center.Movie(*media4)
# Stores Movie objects to new list
movies =
[the_godfather, the_godfather_2, the_godfather_3, lord_of_the_rings_1]
# Sends list of objects to function open_movies_page
razvans_movie_site.open_movies_page(movies)
