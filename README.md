Sentiment Analyzer
==================

A Python module to do a set of operations on tweets. It uses a collection of stopwords to train a dataset for the sentiment analysis. It uses the basic principle of bag-of-words used for natural language processing.

Dependencies
------------
* numpy
* matplotlib(To plot sentiments)

How to use
----------
```python
from src import features, datalink, hashtags
import time
dblink = datalink.DatabaseConnectionDown('perilipsi_tweets')
emoTest = features.Emoticons()
dictTest = features.DictionaryTest()
hashtest = hashtags.hashtags()
testTweet, tweetTime = dblink.fetchTweet()['tweet'], dblink.fetchTweet()['time']	#You can pass anything you want
emo_test = emoTest.analyse(testTweet)
dict_test = dictTest.analyse(testTweet)
hash_test = hashtest.analyseHashtagTweet(testTweet)
print "Emoticons:", emo_test
print "DictionaryTest:", dict_test
print "Hashtags: ", hash_test
```
<strong>Output</strong>
```python
Emoticons: {'positive': 0.47, 'negative': 0.53}
DictionaryTest: {'positive': 0.46153846153846156, 'negative': 0.5384615384615384}
Hashtags:  {'positive': 0.38, 'negative': 0.62}
```
Progress
--------
* <span style="color:green;">Emoticons: This class uses emoticons detection to classify the passed string as positive or negative</span>
* <span style="color:green;">DictionaryTest: This class uses a set of English words and their subjectivity to give a score to a string</span>
* <span style="color:green;">hashtags: This class extracts hashtags from the string sent and calculates the sentiment based on a trained dataset</span>
* AllCaps
* ElongatedWords
* Negation
* Punctuation

Social Network APIs
---------------
* Twitter Search API
* Facebook Graph API

Team Members
------------
<table border="0">
<tr><th>Name</th><th>Email</th></tr>
<tr><td>Sudhanshu Mishra</td><td> mrsud94@gmail.com</td></tr>
<tr><td>Ambar Mehrotra</td><td>ambar.prince@gmail.com</td></tr>
</table>
