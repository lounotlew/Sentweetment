####
# Utility functions for 
####

import tweepy
import pandas as pd

# Twitter API Credentials
consumer_key = "3daaCRqE9kbiVSxxNjmmx1iGp"
consumer_secret = "nqaBQPe54hx7sJeFtVWTK8QyhBo5J75nVlqFERQ6SaMFerBb3d"
access_token = "967529922724966400-AtEXEfM4mxxkhfBtDshgh8eV8ZTimDI"
access_secret = "CT9biXzWYloFVpTsaYVvfwbGpHHGQo0arS4dnhK7Wo1wA"

"""Return the list of tweepy's Status objects (from user_timeline()) for the given USERNAME."""
def get_twitter_data(username = "realDonaldTrump"):

	# Get authorized by Twitter, and set up tweepy.
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)

	return api.user_timeline(screen_name = username, count = 200)

"""Return a pandas dataframe with its columns as tweet text, retweet count, and tweet time,
   
   indexed by tweet id. The data for the columns comes from get_twitter_data()."""
def create_tweet_df(tweets):

	#Initialize an empty dataframe.
	df = pd.DataFrame([])

	# Add columns of twitter data to df.
	df['id'] = [tweet.id for tweet in tweets]
	df['text'] = [tweet.full_text for tweet in tweets]
	df['time'] = [tweet.created_at for tweet in tweets]
	df['']