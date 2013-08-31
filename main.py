from src import features, datalink

dblink = datalink.DatabaseConnectionDown('perilipsi_tweets')
emoTest = features.Emoticons()
dictTest = features.DictionaryTest()

testTweet = dblink.fetchTweet()
print "\n\n"+testTweet+"\n\n"
print "Emoticons:", emoTest.analyse(testTweet)
print "DictionaryTest:", dictTest.analyse(testTweet)