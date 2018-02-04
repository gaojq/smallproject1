#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:12:10 2018

@author: jianqinggao
"""

import tweepy
from tweepy import OAuthHandler
import json
import wget
 
consumer_key = 'RGKFQNODtcUyQvxnOIBAqY1jt'
consumer_secret = 'ClBlYbnXVBgtvWLBtVFNz1K9uwk5HjTlRoRpdym3XRTLETkt9a'
access_token = '809486610312163328-cJwClZaBmfijSFZarMAh5I34p5Z6iy0'
access_secret = 'v4m7tPN7zfMJX2iSEkvltr3U9AxtDGjONI1ctN0e2tUHT'
 
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
 
# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
# User() is the data model for a user profil
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
# You need to do it for all the models you need
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='rogerfederer',
                           count=20, include_rts=False,
                           exclude_replies=True)
last_id = tweets[-1].id
 
while (True):
    more_tweets = api.user_timeline(screen_name='rogerfederer',
                                count=20,
                                include_rts=False,
                                exclude_replies=True,
                                max_id=last_id-1)
# There are no more tweets
    if (len(more_tweets) == 0):
        break
    else:
        last_id = more_tweets[-1].id-1
        tweets = tweets + more_tweets
      
media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
    if(len(media_files)>20):
        break
        
for media_file in media_files:
    wget.download(media_file)