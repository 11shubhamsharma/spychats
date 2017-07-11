from constants import BASE_URL,APP_ACCESS_TOKEN
from get_post_id import  get_post_id
from post_a_comment import  post_a_comment
insta_username="shubhamsharma.una"
def list_a_comment(insta_username):
    media_id=get_post_id(insta_username)
    request_url=(BASE_URL +'media/%s/comments?ACCESS_TOKEN=%s')%(media_id,APP_ACCESS_TOKEN)
    print("GET request url: %s" % (request_url))
    if post_a_comment()["meta"]["code"]==200:
       print("media with media id '{}' is comment by following users :".format(media_id))
       for (index,users_comments)in enumerate(post_a_comment()["data"]):
          print("%d. %s (%s) - %d" % (index+1,users_comments["full_name"],users_comments["id"],users_comments["username"]))
    else:
        print ("wrong input  plzz try again")

list_a_comment(insta_username)