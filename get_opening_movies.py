import urllib2, simplejson
import api_config

try:
    print api_config.API_KEY
    url ='http://data.tmsapi.com/v1/lineups?country=USA&postalCode=78701&api_key=356xjjpcyhqzkkz47cvw7fpp&api_key=%s' % (api_config.API_KEY)

    # Making the request
    req = urllib2.urlopen(url).read()
    raw = simplejson.loads(req)

    #Grabbing the movies returned into an array
    movies = raw['movies']

    print "*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*="
    print "Showing This Week's Opening Movies"
    print "*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*="

    #iterating through the movies returned and printing the Movie Title
    for i, movie in enumerate(movies):
        print str(i+1) + ", " + movie['title']

#Handling HTTP errors gracefully
except urllib2.URLError, e:
    if e.code == 403:
        print str(e) + ' -- Did you enter your API key in the api_config.py file?'

