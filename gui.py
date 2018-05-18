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

		# A welcome label.
		self.welcomeLabel = Label(frame1, text = "Sentweetment: Twitter Sentiment Analysis", font = ("system", 18))
		self.welcomeLabel.pack()

		# A label for the currently selected twitter user. Defaults to "Please enter a twitter user."
		self.currentUser = Label(frame2, text = "Please enter a twitter user.", font = ("system", 16))
		self.currentUser.pack()

		# A label for entering in a twitter user.
		self.selectUserLabel = Label(frame3, text = "Twitter Username: @", font = ("system", 16))
		self.selectUserLabel.grid(row = 0, column = 0)

		# A text entry for entering in a twitter user.
		self.userEntry = Entry(frame3)
		self.userEntry.grid(row = 0, column = 1)

		# A button for launching the sentiment analysis page.
		self.analyzeButton = Button(frame4, text = "Analyze!", font = ("system", 16), command = self.analyze)
		self.analyzeButton.pack()


	"""Open a new window that contains the necessary labels and buttons that describe the sentiments of the selected user's
	   tweets, according to the vader lexicon."""
	def analyze(self):
		window = Toplevel()




# Run the application.
root = Tk()
root.title("Sentweetment: Twitter Sentiment Analysis")
app = MainPage(root)

root.mainloop()
