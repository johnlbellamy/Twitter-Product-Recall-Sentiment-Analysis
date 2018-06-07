# Product Recall Live Twitter Sentiment Analysis
Keep scrolling for usage info...
# Abstract
Over the last several years there have been several major recalls. Recently, we see the recall from Samsung, related to their latest flagship smartphone catching fire or exploding. In perhaps one of the most infamous recalls in recent history, which resulted in (at that time) a record fine from the US government of 1.2 billion dollars, was the recall of Toyota in early 2014, for sudden acceleration problems. Blue Bell went through two painful recalls and seemed to be a bit slow in reacting by pulling their products. Finally, Atkins had a voluntary recall on June 6th, 2016, out of what they term "an abundance of caution".

What affect does recalls have on the public perception of a company? Can we gain insight into this perception of a company through social media? We can broadly group recalls into two groups: companies that immediately issue a recall; and companies that deny the problem altogether. Does a negative perception increase if a problem is denied instead of embraced? How long does a recall affect a company’s social media perception?
# Data
Tweets from three time-intervals were collected; immediately before (before there was talk of a recall), during a recall and immediately after a recall event was settled. Company keywords will be studied and used for tweet retrieval; keywords such as “Blue Bell”,  “Samsung,” and “Toyota.” These terms will be used in conjunction in temporal partitioning of the search.  The resulting tweets will be cleaned and tokenized.  
# Methodology
Jefferson Henriques beautiful package for exploring historic tweets was used (https://github.com/Jefferson-Henrique/GetOldTweets-python/tree/master/got3) to download tweets based on search terms and periods of time. This data was completed for each product and for the three periods of time mentioned.
I then used my own tool TextCleaner 2000 to clean the data (RecallMunging) and then vaderSentiment (see attribution at end of the README) was used to categorize each tweet as positive, negative, neutral (RecallVader). 
Finally, the score for each period was calculated by each period and per company and visualized (RecallVisuals).
# Outcome
Surprisingly, Atkins seemed to do the best. It seems that overall their sentiment is mostly unchanged. Samsung seems to not have suffered too much of an impact, followed by Toyota, with Blue Bell taking a major hit for their second recall.
If we compare Atkins to Blue Bell, it certainly appears that coming out with a recall fast is the best path to maintain positive sentiment.
# Installation
Requirements:
1)	You must use pip or conda install to install vaderSentiment.
2)	Download GOT3 and install. 
Once this is done, running it is simple as unzipping file. Start with RecallMunging, then go to RecallVader. Finally, finish with RecallVisuals.

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
