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
