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

# # VERSION 1 - static creation of movie objects
# # Creates new arrays that contain only the first movie, with the index of 0
# # and separates the values by the | separator
# media1 = media[0].split("|")
# media2 = media[1].split("|")
# media3 = media[2].split("|")
# media4 = media[3].split("|")
# # Creates objects with the *args - sends all non-keyworded
# # variable lenght arguments list to new Movie instance
# the_godfather = entertainment_center.Movie(*media1)
# the_godfather_2 = entertainment_center.Movie(*media2)
# the_godfather_3 = entertainment_center.Movie(*media3)
# lord_of_the_rings_1 = entertainment_center.Movie(*media4)
# # Stores Movie objects to new list
# movies =
# [the_godfather, the_godfather_2, the_godfather_3, lord_of_the_rings_1]
# # Sends list of objects to function open_movies_page
# razvans_movie_site.open_movies_page(movies)

# VERSION 2 - dynamic creation of movie objects using
# stored text in media_data.txt
# Creates new dictionary for saving all_movies

media_files = dict()
# Creates movies list for storing the dictionary of movie objects
# to the function open_movies_page
movies = []
# Creates counter for index values initialized from 0
counter = 0
# Iterates through all elements in the media array
for all_movies in media:
    # Creates new array for storing the first element splitted data
    new_media = media[counter].split("|")
    # Sets title of movie in new variable
    title = new_media[0]
    # Creates new dictionary with the title of the movie element and sets it
    # to equal the new Movie instance
    media_files[title] = entertainment_center.Movie(*new_media)
    # Appends the new object to the movies array
    movies.append(media_files[title])
    counter += 1
# Sends list of objects to function open_movies_page
razvans_movie_site.open_movies_page(movies)
