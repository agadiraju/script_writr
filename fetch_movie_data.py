import api_config
import nltk

from tmdb3 import set_key
from tmdb3 import searchPerson
from tmdb3 import searchMovie
from random import randrange

set_key(api_config.API_KEY)

articles = ['and', 'a', 'the', 'as']

def return_metadata(actor, genre):
  try:
    movies = searchMovie(str(genre))
    genre_movie = movies[randrange(len(movies))]
    featured_actor = searchPerson(str(actor))[0]
  except IndexError:
    print 'Genre or actor entered is not valid. Please try again'
    return None

  actor_roles = featured_actor.roles
  rand_role = actor_roles[randrange(len(actor_roles))]
  actor_movie = searchMovie(str(rand_role).split('\'')[-2])[0]


  output = ''
  output += str(genre_movie.title) + '\n' + str(actor_movie.title)
  output += '\n'
  output += genre_movie.overview + '\n' + actor_movie.overview
  
  return output
