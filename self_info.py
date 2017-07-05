import requests
#import access token and basic url from constansts file
from constants import APP_ACCESS_TOKEN,BASE_URL
# define self info function
def self_info():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()