from self_info import self_info
from  delete_negative_comment import  delete_negative_comment
from get_own_post import get_own_post
from get_post_id import get_post_id
from get_user_id import get_user_id
from get_user_info import get_user_info
from get_user_post import get_user_post
from like_a_post import like_a_post
from post_a_comment import post_a_comment
from hashtag import analyse_user
def start_bot():
    while True:
        print ('\n')
        print ('Hey! Welcome to instaBot!')
        print ('Here are your menu options:')
        print ("1.Get your own details\n")
        print ("2.Get details of a user by username\n")
        print ("3.Get your own recent post\n")
        print ("4.Get the recent post of a user by username\n")
        print ("5.Like the recent post of a user\n")
        print ("6.Make a comment on the recent post of a user\n")
        print ("7.Delete negative comments from the recent post of a user\n")
        print ("8.using hash tag for comment\n")
        print ("9.Exit")

        choice = raw_input("Enter you choice: ")
        if choice == "1":
            self_info()
        elif choice == "2":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "3":
            get_own_post()
        elif choice == "4":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)

        elif choice=="5":
           insta_username = raw_input("Enter the username of the user: ")
           like_a_post(insta_username)

        elif choice=="6":
           insta_username = raw_input("Enter the username of the user: ")
           post_a_comment(insta_username)
        elif choice=="7":

           insta_username = raw_input("Enter the username of the user: ")
           delete_negative_comment(insta_username)
        elif choice=="8":
           insta_username = raw_input("Enter the username of the user: ")
           analyse_user(get_user_id(insta_username))

        elif choice == "9":
            exit()
        else:
            print "wrong choice"

start_bot()