####################################################
# Misc. useful utility functions for Sentweetment. #
# Written by Lewis Kim.                            #
####################################################

from datetime import datetime
import math

"""Return the hour of the given DAY as a floating point number computed by:
   hour + minute/60 + second/60^2."""
def get_hour(day):
	hour = day.hour + day.minute/60 + day.second/3600
	return hour


"""Return an overall sentiment (string) for a given polarity SCORE. Sentiments
   range from very positive, generally positive, slightly positive, neutral,
   slightly negative, generally negative, and very negative."""
def get_sentiment(score):
	return