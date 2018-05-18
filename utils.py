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

"""."""
def get_twitter_data():

	# Get authorized by Twitter, and set up tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)

	data =  api.user_timeline(screen_name = "realDonaldTrump", count = 200)

	return data
