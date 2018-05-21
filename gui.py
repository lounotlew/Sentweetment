###############################################################
# Main GUI class for Sentweetment using tkinter as framework. #
# Written by Lewis Kim.                                       #
###############################################################

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import subprocess, os

import tweets
import analysis
import utils


# GUI class for Sentweetment.
class MainPage:

	def __init__(self, master):

		# Frames for the main page of the GUI.
		frame1 = Frame(master)
		frame2 = Frame(master)
		frame3 = Frame(master)
		frame4 = Frame(master)
		frame5 = Frame(master)
		frame1.pack()
		frame2.pack()
		frame3.pack()
		frame4.pack()
		frame5.pack()

		# A welcome label.
		self.welcomeLabel = Label(frame1, text = "Sentweetment: Twitter Sentiment Analysis", font = ("Arial", 18))
		self.welcomeLabel.pack()

		# A label for the currently selected twitter user. Defaults to "Please enter a twitter user."
		self.currentUser = Label(frame2, text = "Please enter a twitter user.", font = ("Arial", 16))
		self.currentUser.pack()

		# A label for entering in a twitter user.
		self.selectLabel = Label(frame3, text = "Twitter Username: @", font = ("Arial", 16))
		self.selectLabel.grid(row = 0, column = 0)

		# A text entry for entering in a twitter user.
		self.userEntry = Entry(frame3)
		self.userEntry.grid(row = 0, column = 1)

		# A button for launching the sentiment analysis page.
		self.analyzeButton = Button(frame4, text = "Analyze!", font = ("Arial", 16), command = self.analyze)
		self.analyzeButton.pack()

	"""Open a new window that contains the necessary labels and buttons that describe the sentiments of the selected user's
	   tweets, according to the vader lexicon."""
	def analyze(self):
		self.username = self.userEntry.get()

		# Check if there is a selected twitter user.
		if self.username == "":
			showerror("Error", "Please select a twitter user.")
			return

		# Check if tweepy is able to retrieve any data on the selected user.
		try:
			data = tweets.get_twitter_data(self.userEntry.get())

		except:
			showerror("Error", "Tweepy Error. Please check if that Twitter username exists.")
			return

		window = Toplevel()

		# Get the tweepy data of USERNAME as a pandas dataframe.
		self.userdata = tweets.create_tweet_df(tweets.get_twitter_data(self.username))

		# Get the average polarity score and sentiment of USERNAME's Twitter account.
		self.polarity_score = round(analysis.calculate_avg_polarity(self.userdata['polarity']), 2)
		self.sentiment = analysis.get_sentiment(self.polarity_score)

		# A label that displays the selected user.
		self.selectedUserLabel = Label(window, text = "Selected User: @" + self.username, font = ("system", 14))
		self.selectedUserLabel.pack()

		# A label that displays the selected user's average polarity score.
		self.polarityScoreLabel = Label(window, text = "Overall Polarity Score: " + str(self.polarity_score), font = ("system", 14))
		self.polarityScoreLabel.pack()

		# A label that displays the selected user's account sentiment.
		self.sentimentLabel = Label(window, text = "@" + self.username + "'s Twitter account is " + self.sentiment, font = ("system", 14))
		self.sentimentLabel.pack()

		# A button that displays an explanation of the polarity score and sentiment.
		self.explainButton = Button(window, text = "What do the polarity scores and sentiment mean?", font = ("system", 14), command = self.explainValues)
		self.explainButton.pack()

		# A button that displays the top 10 most positive tweets by the selected user.
		self.posTweetsButton = Button(window, text = "Display @" + self.username + "'s Top 10 Most Positive Tweets", font = ("system", 14),
		                              command = self.displayPositiveTweets)
		self.posTweetsButton.pack()

		# A button that displays the top 10 most negative tweets by the selected user.
		self.negTweetsButton = Button(window, text = "Display @" + self.username + "'s Top 10 Most Negative Tweets", font = ("system", 14),
			                          command = self.displayNegativeTweets)
		self.negTweetsButton.pack()

		# A button that displays a polarity vs. time trend graph.
		self.trendButton = Button(window, text = "View How @" + self.username + "'s Tweet Polarity Changes Over Time", font = ("system", 14),
			                      command = self.displayTrendGraph)
		self.trendButton.pack()

		# A button that displays a polarity distribution histogram.
		self.histButton = Button(window, text = "View the Distribution of @" + self.username + "'s Tweet Polarities", font = ("system", 14),
			                     command = self.displayHist)
		self.histButton.pack()

	"""Open the .txt file containing help information about what the polarity scores/values mean."""
	def explainValues(self):
		subprocess.call(['open', "data/help.txt"])

	"""Open the .txt file created in utils.writePositiveTweets with the default OS program."""
	def displayPositiveTweets(self):
		utils.writePositiveTweets(self.username, self.userdata)

		subprocess.call(['open', "data/tweets/" + self.username + "-positive-tweets.txt"])

	"""Open the .txt file created in utils.writePositiveTweets with the default OS program."""
	def displayNegativeTweets(self):
		utils.writeNegativeTweets(self.username, self.userdata)

		subprocess.call(['open', "data/tweets/" + self.username + "-negative-tweets.txt"])

	"""Display a matplotlib polarity trend graph."""
	def displayTrendGraph(self):
		title = 'Tweet Polarity vs. Tweet Time (Pacific) for @' + self.username

		fig, ax = plt.subplots()
		ax.plot(self.userdata['pst_time'], self.userdata['polarity'], marker = 'o', ls = '-')

		ax.set_title(title)
		ax.set_xlabel('Tweet Time (Pacific)')
		ax.set_ylabel('Tweet Polarity')

		plt.show()

	"""Display a matplotlib proportion (probability) histogram for tweet polarities."""
	def displayHist(self):
		fig, ax = plt.subplots()

		# the histogram of the data
		ax.hist(self.userdata['polarity'].dropna(), density = 1)

		ax.set_xlabel('@' + self.username + "'s Tweet Polarity")
		ax.set_ylabel('Proportion')
		ax.set_title(r'Histogram of @' + self.username + "'s Tweet Polarities")

		# Tweak spacing to prevent clipping of ylabel
		fig.tight_layout()
		plt.show()


# Run the application.
root = Tk()
root.title("Sentweetment: Twitter Sentiment Analysis")
app = MainPage(root)

while True:
	try:
		root.mainloop()
		break
	except UnicodeDecodeError: # Added to avoid the program crashing when scrolling.
		pass

