#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta

import tweepy #https://github.com/tweepy/tweepy
import json
import os
import api



CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

#Twitter API credentials
# CONSUMER_KEY: ${{ secrets.CONSUMER_KEY }}
# CONSUMER_SECRET:  ${{ secrets.CONSUMER_SECRET }} 
# ACCESS_TOKEN: ${{ secrets.ACCESS_TOKEN }}
# ACCESS_TOKEN_SECRET: ${{ secrets.ACCESS_TOKEN_SECRET }}


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    ## The first tweet##
    api.update_status(status ="Hello Everyone !")

    #tweet = api.update_status('Bad Tweet')
    #api.destroy_status(tweet.id_str)
    count = 3 
    tweets = api.user_timeline(screen_name, count = count )
    for tweet in tweets:
    	print(tweet.text)

    ## Search by key words## 
    q = "BTS"
    # search the query 
    users = api.search_users(q) 
    # print the users retrieved 
    for user in users: 
        print(user.screen_name) 


    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))
       
    #write tweet objects to JSON
    file = open('tweet.json', 'w') 
    print ("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    print ("Done")
    file.close()



# def todays_stats(dict_name):
#   # Get my account information
#   info = api.me()
#   # Get follower and following counts
#   followers_cnt = info.followers_count  
#   following_cnt = info.friends_count
#   # Get today's date
#   today = date.today()
#   d = today.strftime("%b %d, %Y")
#   # Save today's stats only if they haven't been collected before
#   if d not in dict_name:
#     dict_name[d] = {"followers":followers_cnt, "following":following_cnt}

#     file = open('follower_history.json', 'w') 
#     print ("Writing tweet objects to JSON please wait...")
#     for status in dict_name:
#         json.dump(status._json,file,sort_keys = True,indent = 4)
#     #close the file
#     print ("Done")
#     file.close()
#     #save_json("follower_history.json", dict_name)
#   else:
#     print('Today\'s stats already exist')



if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@btschartdata")

