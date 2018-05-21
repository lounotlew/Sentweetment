####################################################
# Misc. useful utility functions for Sentweetment. #
# Written by Lewis Kim.                            #
####################################################

from datetime import datetime
import math

import analysis

"""Return the hour of the given DAY as a floating point number computed by:
   hour + minute/60 + second/60^2."""
def get_hour(day):
	hour = day.hour + day.minute/60 + day.second/3600
	return hour

"""Write the positive tweets returned by analysis.get_positive_tweets() into a .txt file in data/tweets."""
def writePositiveTweets(username, data):
	filepath = "data/tweets/" + username + "-positive-tweets.txt"
	file = open(filepath, "w+")

	file.write("Top 10 Most Positive Tweets by @" + username + '\n' + '\n')

	tweets = analysis.get_positive_tweets(data)

	for i in range(10):
		j = i + 1
		tweet = str(j) + ") " + tweets[i][0] + " - created at " + str(tweets[i][1]) + " (polarity: " + str(tweets[i][2]) + ")" + '\n' + '\n'

		file.write(tweet)

"""Write the negative tweets returned by analysis.get_positive_tweets() into a .txt file in data/tweets."""
def writeNegativeTweets(username, data):
	filepath = "data/tweets/" + username + "-negative-tweets.txt"
	file = open(filepath, "w+")

	file.write("Top 10 Most Negative Tweets by @" + username + '\n' + '\n')

	tweets = analysis.get_negative_tweets(data)

	for i in range(10):
		j = i + 1
		tweet = str(j) + ") " + tweets[i][0] + " - created at " + str(tweets[i][1]) + " (polarity: " + str(tweets[i][2]) + ")" + '\n' + '\n'

		file.write(tweet)

