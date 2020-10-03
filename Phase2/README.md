Based on the sources from phase 1, the second phase added a "get_hashtag.py" file used to retrieve the last related 100 tweets from 2020-10-01. 
In this case, used "United Airline" as an example. 

All the 100 tweets will be stored into a csv file called "ua.csv". 

![Image text](https://github.com/zhoux17/EC_601/blob/master/Phase2/Screen%20Shot%202020-10-03%20at%203.43.22%20AM.png)

So basically phase 2 is using Twitter API and Google NLP API to achieve social media analysis. But focus more on the hashtags, since while new things are happening, peopel prefer to tweet with hashtag, this is a more productive way to get the trending. 
There are two ways to analyze: 
(1) if we want to know a specific person's emotion towars UA, we can analyze his/ her tweet individually in Google NLP API. Take the most recent tweet got from Twitter API as an example: 

![Image text](https://github.com/zhoux17/EC_601/blob/master/Phase2/Screen%20Shot%202020-10-03%20at%203.56.58%20AM.png)

it shows the sentiment is positive, and the magnitude of this sentiment is relatively high. 

If using " Airline companies ripping off our tax and money":

![Image text](https://github.com/zhoux17/EC_601/blob/master/Phase2/Screen%20Shot%202020-10-03%20at%204.01.08%20AM.png)

the sentiment is negative and magnitude is high as well. 

So individually, combine the Twitter API and Google NLP API can analyze the person's emotion at this time. 

(2) If we want to figure out how's the public's reaction based on UA's new published policy, we can use "sentiment_analysis.py" used in phase 1, which is an analysis based on each text and do the average, get the final sentiment & magnitude of the whole paragraph. 
So if we are interested in the public's attitude based on the trending, we can get the average sentiment calculation. This can reflect their emotion 
on the news. 






