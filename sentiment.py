#!/usr/bin/env python

from textblob import TextBlob

with open ("stt.txt", "r") as myfile:
  data = myfile.read()
#text = '''You are a lovely lady. I hate you so much.'''

blob = TextBlob(data)

for sentence in blob.sentences:
  print(sentence.sentiment.polarity) 
