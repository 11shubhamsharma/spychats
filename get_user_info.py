import requests
#imort get_user_id from get_user_id file
from get_user_id import get_user_id
#import access token and basic url from constansts file
from constants import APP_ACCESS_TOKEN,BASE_URL
# define get_user_info function
def get_user_info(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print ('User does not exist!')
    exit()
  request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
  print ('GET request url : %s' % (request_url))
  user_info = requests.get(request_url).json()
  if user_info['meta']['code'] == 200:
      if len(user_info['data']):
          print ('Username: %s' % (user_info['data']['username']))
          print ('No. of followers: %s' % (user_info['data']['counts']['followed_by']))
          print ('No. of people you are following: %s' % (user_info['data']['counts']['follows']))
          print ('No. of posts: %s' % (user_info['data']['counts']['media']))
      else:
          print 'There is no data for this user!'
  else:
      print ('Status code other than 200 received!')