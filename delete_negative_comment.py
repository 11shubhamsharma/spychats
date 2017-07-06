import requests
#import access token and basic url from constansts file
from constants import APP_ACCESS_TOKEN,BASE_URL
#import get_post_id from get _post_id
from get_post_id import get_post_id
# define the delete_negative_comment
def delete_negative_comment(insta_username):
  media_id = get_post_id(insta_username)
  request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  comment_info = requests.get(request_url).json()