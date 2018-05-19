####################################################
# Misc. useful utility functions for Sentweetment. #
# Written by Lewis Kim and the DS 100 Staff.       #
####################################################

from datetime import datetime
import math

"""Return the hour of the given DAY as a floating point number computed by:
   hour + minute/60 + second/60^2."""
def get_hour(day):
	hour = day.hour + day.minute/60 + day.second/3600
	return hour

