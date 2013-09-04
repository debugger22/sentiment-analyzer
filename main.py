from src import features, datalink, hashtags, sentiment_plot
import time
dblink = datalink.DatabaseConnectionDown('perilipsi_tweets')
plotter = sentiment_plot.Plotter()
emoTest = features.Emoticons()
dictTest = features.DictionaryTest()
hashtest = hashtags.hashtags()
testTweet, tweetTime = dblink.fetchTweet()['tweet'], dblink.fetchTweet()['time']	#You can pass anything you want
emo_test = emoTest.analyse(testTweet)['positive']
dict_test = dictTest.analyse(testTweet)['positive']
hash_test = hashtest.analyseHashtagTweet(testTweet)['positive']
print "Emoticons:", emo_test
print "DictionaryTest:", dict_test
print "Hashtags: ", hash_test