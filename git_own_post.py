import requests
#imort get_user_id from get_user_id file
from constants import APP_ACCESS_TOKEN,BASE_URL
# define get_own_post function
def get_own_post():
  request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  own_media = requests.get(request_url).json()