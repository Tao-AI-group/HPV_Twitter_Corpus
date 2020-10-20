import tweepy
import pandas as pd
import time

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

annotation_pd = pd.read_csv("hpv_twitter_annotation.tsv", sep='\t')
tweet_list = []
for index, row in annotation_pd.iterrows():
    tweet_id = row["Tweet_ID"]
    try:
        tweet = api.get_status(tweet_id)
        tweet_text = str(tweet.text).replace("\t"," ").replace("\r"," ").replace("\n", " ")
        print(tweet_id,tweet_text )
        tweet_list.append(tweet_text)
    except:
        tweet_list.append("")
        print(tweet_id,"Not Available")
    time.sleep(1)

annotation_pd["Tweet_text"] = tweet_list
tweet_pd = annotation_pd[["Tweet_ID","Tweet_text"]]

tweet_pd.to_csv("twitter_id_text.tsv", sep='\t', index=False)