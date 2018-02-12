import entertainment_center_api
import razvans_movie_site
import http.client
import json

# The Movie Database API HTTPConnection
conn = http.client.HTTPConnection("api.themoviedb.org")

payload = "{}"
# API request for user movie list
conn.request("GET", "/3/list/47228?language=en-US&api_key=623a7df325a12927fd613644a9eaa648", payload)

# Store & read response in variable
res = conn.getresponse()
data = res.read()
# Load response as json string
list_data = json.loads(data)
# Define new array for storing the instances of the Movie class
movie_list = []
# Shorthand for json keys
li = list_data['items']
title = 'original_title'
release = 'release_date'
vote = 'vote_average'
story = 'overview'
poster = 'poster_path'

counter = 0
# Iterate in all items of the list
for value in li:
    # Get list movie ID
    movie_id = li[counter]['id']
    # Request movie trailer info
    conn.request("GET", "/3/movie/" + str(movie_id) + "/videos?api_key=623a7df325a12927fd613644a9eaa648")
    # Get & read response
    res = conn.getresponse()
    data = res.read()
    # Load json trailer ID string
    trailer_json = json.loads(data)
    # Get trailer ID
    trailer_json = trailer_json['results'][0]['key']
    # Concatenate youtube link with API trailer ID
    trailer = 'https://www.youtube.com/watch?v=' + trailer_json
    # Append Movie class objects to movie_list
    movie_list.append(entertainment_center_api.Movie(li[counter][title], li[counter][release], li[counter][story], li[counter][vote], "https://image.tmdb.org/t/p/original/" + li[counter][poster], trailer))
    counter += 1
# Open movie list of objects in razvans_movie_site
razvans_movie_site.open_movies_page(movie_list)
