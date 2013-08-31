from src import features, datalink

dblink = datalink.DatabaseConnectionDown('perilipsi_tweets')
emoTest = features.Emoticons()
dictTest = features.DictionaryTest()

testTweet = dblink.fetchTweet()
print "\n\n"+testTweet+"\n\n"
print emoTest.analyse(testTweet)
print dictTest.analyse(testTweet)