####
# 
# Written by Lewis Kim.
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
   tweet location, hour (see line ), 
   indexed by tweet id. The data for the columns comes from get_twitter_data()."""
def create_tweet_df(tweets):

	#Initialize an empty dataframe.
	df = pd.DataFrame([])

	# Add columns of twitter data to df.
	df['id'] = [tweet.id for tweet in tweets]
	df['text'] = [tweet.text for tweet in tweets]  # Some entries may be missing (see line ).
	df['retweet_count'] = [tweet.retweet_count for tweet in tweets]
	df['time'] = [tweet.created_at for tweet in tweets]
	df['location'] = [tweet.location for tweet in tweets]

	df = df.set_index('id')

	# Some tweets store their text in full_text as opposed to text.
	# Check if a tweet has full_text. If so, append it to a temporary DF and fill the missing
	# values in df['text'] with them.
	fullTexts = []
	ids = []

	for tweet in tweets:
		if 'full_text' in tweet:
			fullTexts.append(tweet['full_text'])
			ids.append(tweet['id'])

	tempDF = pd.DataFrame({'id': ids, 'text': fullTexts})
	tempDF = tempDF.set_index('id')

	df['text'] = df['text'].fillna(tempDF['text'])
	df.sort_index(inplace = True)

	# Create a new column called 









