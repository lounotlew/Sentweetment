#
#
#

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

import pandas as pd
import numpy as np
from pandastable import Table, TableModel

import tweets
import analysis


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

		self.df1 = pd.read_pickle('data/katyperry.gz')
		self.df2 = pd.read_pickle('data/ucb.gz')

		# A welcome label.
		self.welcomeLabel = Label(frame1, text = "Sentweetment: Twitter Sentiment Analysis", font = ("system", 18))
		self.welcomeLabel.pack()

		# A label for the currently selected twitter user. Defaults to "Please enter a twitter user."
		self.currentUser = Label(frame2, text = "Please enter a twitter user.", font = ("system", 16))
		self.currentUser.pack()

		# A label for entering in a twitter user.
		self.selectLabel = Label(frame3, text = "Twitter Username: @", font = ("system", 16))
		self.selectLabel.grid(row = 0, column = 0)

		# A text entry for entering in a twitter user.
		self.userEntry = Entry(frame3)
		self.userEntry.grid(row = 0, column = 1)

		# A button for launching the sentiment analysis page.
		self.analyzeButton = Button(frame4, text = "Analyze!", font = ("system", 16), command = self.analyze)
		self.analyzeButton.pack()

		self.test = Button(frame5, text = "test", command = self.test)
		self.test.pack()


	"""Open a new window that contains the necessary labels and buttons that describe the sentiments of the selected user's
	   tweets, according to the vader lexicon."""
	def analyze(self):
		username = self.userEntry.get()

		# Check if there is a selected twitter user.
		if username == "":
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
		self.userdata = tweets.create_tweet_df(tweets.get_twitter_data(username))

		# Get the average polarity score and sentiment of USERNAME's Twitter account.
		self.polarity_score = round(analysis.calculate_avg_polarity(self.userdata['polarity']), 2)
		self.sentiment = analysis.get_sentiment(self.polarity_score)

		# A label that displays the selected user.
		self.selectedUserLabel = Label(window, text = "Selected User: @" + username, font = ("system", 14))
		self.selectedUserLabel.pack()

		# A label that displays the selected user's average polarity score.
		self.polarityScoreLabel = Label(window, text = "Overall Polarity Score: " + str(self.polarity_score), font = ("system", 14))
		self.polarityScoreLabel.pack()

		# A label that displays the selected user's account sentiment.
		self.sentimentLabel = Label(window, text = "@" + username + "'s Twitter account is " + self.sentiment, font = ("system", 14))
		self.sentimentLabel.pack()

		# A button that displays an explanation of the polarity score and sentiment.
		self.explainButton = Button(window, text = "What does the polarity score and sentiment mean?", font = ("system", 14))
		self.explainButton.pack()

		# A button that displays the top 10 most positive tweets by the selected user.
		self.posTweetsButton = Button(window, text = "Display @" + username + "'s Top 10 Most Positive Tweets", font = ("system", 14),
		                              command = lambda: analysis.get_positive_tweets(self.userdata))
		self.posTweetsButton.pack()

		# A button that displays the top 10 most negative tweets by the selected user.
		self.negTweetsButton = Button(window, text = "Display @" + username + "'s Top 10 Most Negative Tweets", font = ("system", 14),
			                          command = lambda: analysis.get_negative_tweets(self.userdata))
		self.negTweetsButton.pack()




	def test(self):
		a1 = analysis.calculate_avg_polarity(self.df1['polarity'])
		a2 = analysis.calculate_avg_polarity(self.df2['polarity'])

		print("katy " + str(round(a1, 2)))
		print("ucb " + str(round(a2, 2)))

		print("katy " + analysis.get_sentiment(a1))
		print("ucb " + analysis.get_sentiment(a2))



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
