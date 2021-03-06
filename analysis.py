#################################################################################
# Functions to do with calculating and analyzing polarity scores and sentiment. #
# Written by Lewis Kim.                                                         #
#################################################################################

import pandas as pd
import numpy as np

"""Return the average polarity score by calculating the mean of all polarity
   scores in SCORES."""
def calculate_avg_polarity(scores):
	scores = scores.dropna()

	return scores.mean()

"""Return an overall sentiment (string) for a given polarity SCORE. Sentiments
   range from very positive, generally positive, slightly positive, neutral,
   slightly negative, generally negative, and very negative.
   Scale may need readjustments."""
def get_sentiment(score):
	
	# Ranges for score-to-sentiment scale, from the VADER Lexicon documentation.
	# Negative ranges.
	if score < -4:
		return "extremely negative."

	elif score >= -4 and score <= -3:
		return "very negative."

	elif score > -3 and score <= -2:
		return "fairly negative."

	elif score > -2 and score <= -1:
		return "negative."

	elif score > -1 and score < -0.1:
		return "slightly negative."

	# Neutral range.
	elif score >= -0.1 and score <= 0.1:
		return "neutral."

	# Positive ranges.
	elif score > 0.1 and score <= 1:
		return "slightly positive."

	elif score > 1 and score <= 2:
		return "positive."

	elif score > 2 and score <= 3:
		return "fairly positive."

	elif score > 3 and score <= 4:
		return "very positive."

	elif score > 4:
		return "extremely positive."

"""Return a list of tuples of top 10 most positive tweets and their dates, from the
   selected user's Twitter DATA."""
def get_positive_tweets(data):
	
	# Sort 'polarity' values in descending order.
	df = data.sort_values('polarity', ascending = False)

	tweets = df['text'].tolist()[0:10]
	dates = df['time'].tolist()[0:10]
	polarities = [round(x, 2) for x in df['polarity'].tolist()[0:10]]

	pos_tweets = [(x, y, z) for x, y, z in zip(tweets, dates, polarities)]

	return pos_tweets


"""Return a list of tuples of top 10 most negative tweets and their dates, from the
   selected user's Twitter DATA."""
def get_negative_tweets(data):

	# Sort 'polarity' values in ascending order.
	df = data.sort_values('polarity', ascending = True)

	tweets = df['text'].tolist()[0:10]
	dates = df['time'].tolist()[0:10]
	polarities = [round(x, 2) for x in df['polarity'].tolist()[0:10]]

	neg_tweets = [(x, y, z) for x, y, z in zip(tweets, dates, polarities)]

	return neg_tweets

