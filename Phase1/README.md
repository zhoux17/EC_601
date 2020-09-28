//Twitter API results: 

'''tweets = api.user_timeline(screen_name, count = count )
    for tweet in tweets:
    	print(tweet.text)
      
'''----> Get the most recent 2 tweets 

iTunes US      

#8. Dynamite (+5)

https://t.co/ns6KR79IJq
Spotify Update (26/09): 

Total streams — 11,939,658,860 (+19,911,875) https://t.co/nCtJFHOxhY
Spotify Update (26/09): 

MAP OF THE SOUL: 7 — 1,978,211,915 (+4,105,852)



'''q = "BTS"
    # search the query 
    users = api.search_users(q) 
    # print the users retrieved 
    for user in users: 
        print(user.screen_name) 

'''----> Search by 20 related twitter accounts, which the keyword "BTS" is included 

https://t.co/nkbZtMUUMS          
BTS_twt
bts_bighit
BTSW_official
bts_love_myself
BTS_ARMY
btsanalytics
choi_bts2
BTS_Billboard
BangtanTrends
gainbtsm
UKBTSARMATION
BTS__Europe
BTSGlobalCharts
BTS_History613
BTS_National
BTSxBRAZIL
SuperStarBTStwt
btsdiary
btsworldwider
btsvotingorg
Writing tweet objects to JSON please wait...
Done


'''def todays_stats(dict_name):
  # Get my account information
  info = api.me()
  # Get follower and following counts
  followers_cnt = info.followers_count  
  following_cnt = info.friends_count
  # Get today's date
  today = date.today()
  d = today.strftime("%b %d, %Y")
  # Save today's stats only if they haven't been collected before
  if d not in dict_name:
    dict_name[d] = {"followers":followers_cnt, "following":following_cnt}

    file = open('follower_history.json', 'w') 
    print "Writing tweet objects to JSON please wait..."
    for status in dict_name:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    #close the file
    print "Done"
    file.close()
    #save_json("follower_history.json", dict_name)
  else:
    print('Today\'s stats already exist')
 
 ''' ----> Get the account status of the day, including the follwers count and following count. Then store them in the .json file. 


//Google NLP API results 

'''
Text: I love softdrink
Sentiment: 0.899999976158, 0.899999976158

''' ----> This returns a positive sentiment result, due to the keyword "love" 

'''
Text: I hate coke
Sentiment: -0.800000011921, 0.800000011921
'''----> This returns a negative sentiment result, due to the keyword "hate" 

'''
Text: I love softdrink, but I hate coke
Sentiment: -0.300000011921, 0.300000011921
'''


'''
gracezhou@Grace Desktop % python sentiment_analysis.py reviews/bladerunner-pos.txt
Sentence 0 has a sentiment score of 0.699999988079
Sentence 1 has a sentiment score of 0.20000000298
Sentence 2 has a sentiment score of 0.699999988079
Sentence 3 has a sentiment score of -0.10000000149
Sentence 4 has a sentiment score of 0.0
Sentence 5 has a sentiment score of -0.600000023842
Sentence 6 has a sentiment score of -0.10000000149
Sentence 7 has a sentiment score of 0.5
Sentence 8 has a sentiment score of 0.40000000596
Sentence 9 has a sentiment score of 0.899999976158
Overall Sentiment: score of 0.20000000298 with magnitude of 4.59999990463
''' ----> Given a text, which contains several sentences. Analyze the text per sentence, then get the overall sentiment result.  

