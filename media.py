import entertainment_center
import razvans_movie_site
import tmdbsimple as tmdb


tmdb.API_KEY = "623a7df325a12927fd613644a9eaa648"

search = tmdb.Search()
response = search.movie(query="Lord of the Rings")
for s in search.results:
    print(s['title'], s['id'], s['release_date'])
