from src import features, datalink, hashtags
import time

dblink = datalink.DatabaseConnectionDown('perilipsi_tweets')
emoTest = features.Emoticons()
dictTest = features.DictionaryTest()
hashtest = hashtags.hashtags()
testTweet, tweetTime = dblink.fetchTweet()['tweet'], dblink.fetchTweet()['time']
print testTweet+" Time:"+`tweetTime`
print "Emoticons:", emoTest.analyse(testTweet)
print "DictionaryTest:", dictTest.analyse(testTweet)
print "Hashtags: ",hashtest.analyseHashtagTweet(testTweet)