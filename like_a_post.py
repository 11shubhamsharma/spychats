import requests
#import access token and basic url from constansts file
from constants import APP_ACCESS_TOKEN,BASE_URL
#import get_post_id from get _post_id
from get_post_id import get_post_id
def like_a_post(insta_username):
  media_id = get_post_id(insta_username)
  request_url = (BASE_URL + 'media/%s/likes') % (media_id)
  payload = {"access_token": APP_ACCESS_TOKEN}
  print 'POST request url : %s' % (request_url)
  post_a_like = requests.post(request_url, payload).json()
  if post_a_like['meta']['code'] == 200:
      print 'Like was successful!'
  else:
      print 'Your like was unsuccessful. Try again!'