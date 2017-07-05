import requests
#imort get_user_id from get_user_id file
from get_user_id import get_user_id
#import access token and basic url from constansts file
from constants import APP_ACCESS_TOKEN,BASE_URL
# define get_user_info function
def get_user_info(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print 'User does not exist!'
    exit()
  request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()