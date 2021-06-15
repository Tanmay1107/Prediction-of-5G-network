import os
import tweepy as tw
import pandas as pd

consumer_key ='2SypEC1Z7YtAZrDwA37pjx46x'
consumer_secret='0jvwNvBVMkaAIYgnFf9sEKTTs1YSTmm0CVsIDK8hFXwzObFP2H'
access_token='1324562119673569281-GBt3bIUSz3G1Fg8l7TCM97v0n4NVDZ'
access_token_secret='XRN0CXhOMPDz7JUk01xluUxbDn5ACYWX6hhd43rUaeeyY'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
geocode='34.16500,77.58400,250km'
search_words = ('#jio OR #jiospeed OR #jiocomplain OR #jioservice')
new_search= search_words + ' -filter:retweets'
results = api.search(q=search_words,lang='en',count=1000,geocode=geocode)

actualtweets=[]
actualuser=[]
actualloc=[]

for tweet in results:
    actualtweets.append(tweet.text)
    actualuser.append(tweet.user.screen_name)
    actualloc.append(tweet.user.location)

df = pd.DataFrame({'User Name':actualuser,'User Location':actualloc,'Tweet':actualtweets})
df.to_csv('TwitterDataLadakh12345678910.csv',index=False,encoding='utf-8')
