import tweepy
import csv
import pandas as pd
import os 



CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
####input your credentials here
# CONSUMER_KEY: ${{ secrets.CONSUMER_KEY }}
# CONSUMER_SECRET:  ${{ secrets.CONSUMER_SECRET }} 
# ACCESS_TOKEN: ${{ secrets.ACCESS_TOKEN }}
# ACCESS_TOKEN_SECRET: ${{ secrets.ACCESS_TOKEN_SECRET }}
  
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
                           lang="en",
                           since="2020-10-01").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
