# Sentweetment - Sentiment Analysis for Twitter
> Written by Lewis Kim

### Description

Sentweetment is a Twitter account sentiment analyzer for a selected twitter user, based on the 'Donald Trump Tweet Analysis' project I completed in UC Berkeley's Data Science 100. Using the VADER Lexicon (https://github.com/cjhutto/vaderSentiment), Sentweetment analyzes the polarity of the words in any given user's tweets (given they have enough tweets, with a max. of latest 200 tweets), and explores the general sentiment and mood of that user's twitter account. Sentweetment also offers the option of visualizing this analysis, such as showing which top 10 tweets are the most/least positive/negative, displaying a tweet polarity vs. time trend graph, and tweet polarity histogram.

For a GUI sample and applet walkthrough, click this [link](gui_sample/README.md).

### Installation

Sentweetment was written in Python 3.6, and may not work with Python 2.

Required packages:
- ``tkinter`` (included with Python 3)
- ``tweepy`` (pip install: ``pip3 install tweepy``)
- ``pandas`` (pip install: ``pip3 install pandas``)
- ``scipy``/``numpy`` (pip install: ``pip3 install scipy numpy``)
- ``matplotlib`` (pip install: ``pip3 install matplotlib``)

To run this application (after installing all required packages), type the following command in terminal/bash in the directory inside the Sentweetment folder:

```
python3 gui.py
```

### References:

References to the libraries and packages used in Sentweetment:

1) ``tkinter``: https://wiki.python.org/moin/TkInter
2) ``tweepy``: http://docs.tweepy.org/en/v3.5.0/
3) ``pandas``: https://pandas.pydata.org/pandas-docs/stable/
4) ``matplotlib``: https://matplotlib.org/gallery/index.html#