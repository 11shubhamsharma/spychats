from constants import  APP_ACCESS_TOKEN,BASE_URL
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import requests
def analyse_user(user_id):
    request_url = BASE_URL + "users/%s/media/recent/?access_token=%s" %(user_id, APP_ACCESS_TOKEN)
    print "Getting information from: %s" %(request_url)

    interests = {"health:5"}
    response = requests.get(request_url).json()
    print response
    if response['meta']['code'] == 200:
        if len(response['data']) > 0:
            for index in range(0, len(response['data'])):
                if len(response['data'][index]['tags']) > 0:
                    for tag_index in range(0, len(response['data'][index]['tags'])):
                        if response['data'][index]['tags'][tag_index] in interests:
                            interests[response['data'][index]['tags'][tag_index]] += 1
                        else:
                            interests[response['data'][index]['tags'][tag_index]] = 1
            wordcloud = WordCloud().generate_from_frequencies(interests)

            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.show()

        else:
            print "No posts to show"

    else:
        print "Error: Not 200"








