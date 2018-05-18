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
		# try:
		# 	data = tweets.get_twitter_data(self.userEntry.get())

		# except:
		# 	showerror("Error", "Tweepy Error. Please check if that Twitter username exists.")

		window = Toplevel()



		#sentiment = utils.get_sentiment(score)

		#
		self.selectedUserLabel = Label(window, text = "Selected User: @" + username, font = ("system", 16))
		self.selectedUserLabel.pack()

		# 
		self.polarityScoreLabel = Label(window, text = "Overall Polarity Score: ", font = ("system", 14))
		self.polarityScoreLabel.pack()

		# 
		self.sentimentLabel = Label(window, text = "@" + username + "'s Twitter account is ", font = ("system", 14))
		self.sentimentLabel.pack()




	def test(self):
		print(self.df1.isnull().values.any())
		print(self.df2.isnull().values.any())

		print(len(self.df1))
		print(len(self.df2))

		print(list(self.df1))
		print(list(self.df2))

		print(self.df1['polarity'].tolist())
		print(self.df2['polarity'].tolist())


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
