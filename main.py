from src import features, datalink, hashtags

dblink = datalink.DatabaseConnectionDown('perilipsi_tweets')
emoTest = features.Emoticons()
dictTest = features.DictionaryTest()
testTweet = dblink.fetchTweet()
hashtest = hashtags.hashtags()
print hashtest.analyseHashtagTweet(testTweet)

print "\n\n"+testTweet+"\n\n"
print emoTest.analyse(testTweet)
print dictTest.analyse(testTweet)