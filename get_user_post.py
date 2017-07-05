#import get_user_id from get_user_id file
from get_user_id import get_user_id
def get_user_post(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print 'User does not exist!'
    exit()