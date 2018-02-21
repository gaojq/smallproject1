import tweepy
import requests
import os

def image_down(Username):
    #api = twitter_api()
    timeline = api.user_timeline(screen_name = Username,count=999, include_rts = True)
    urls = []
    for tweet in timeline:
        for media in tweet.entities.get("media",[{}]):
            #checks if there is any media-entity
            if media.get("type",None) == "photo":
                urls.append(media["media_url"])
    # checks if the entity is of the type "photo"
#             urls.add(requests.get(media["media_url"]))
index = 1;
    for url in urls:
        request = requests.get(url, stream=True)
        if request.status_code == 200:
            index = index+1
            with open(url.split('/')[-1], 'wb') as image:
                for chunk in request:
                    image.write(chunk)


def tweet_image(url, message):
    #api = twitter_api()
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
    
        api.update_with_media(filename, status=message)
    os.remove(filename)
else:
    print("Unable to download image")

def twitter_api(consumer_token,consumer_secret,key,secret):
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(key, secret)
    global api
    api = tweepy.API(auth)
    return api
