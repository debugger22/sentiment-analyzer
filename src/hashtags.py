from datalink import DatabaseConnectionDown
class hashtags:
	'''
	This method extracts all the hashtags present in the tweet
	'''
	def extractHashtagTweet(self):
		self.hashtagList = []
		for i in self.tempTweet:
			try:
				if i[0] == '#':
					self.hashtagList.append(i)
			except:
				pass
	'''
	This method extracts all the hashtags by calling extractHashtagTweet method and analyzes
	them by searching for them in a database of hashtags
	This method takes a string as parameter and returns a dictionary of the probabilities
	of the sentiment about that string
	DictKeys: 'positive', 'negative' 
	'''
	def analyseHashtagTweet(self, tweet):
		self.tempTweet = tweet.split(" ")
		self.extractHashtagTweet()
		if len(self.hashtagList)==0:
			return {"positive":0,"negative":0}

		fin = open("data/unigrams-pmilexicon.txt","r")
		resultDict = {}
		positiveNum = 0.0
		negativeNum = 0.0
		positiveProb = []
		negativeProb = []
		tempFile = fin.readlines()
		for i in self.hashtagList:
			for j in tempFile:
				tempLine = j[:-1].split("\t")
				if i != tempLine[0]:
					continue
				else:
					positiveNum = float(tempLine[2])
					negativeNum = float(tempLine[3])
					positiveProb.append(positiveNum/(positiveNum+negativeNum))
					negativeProb.append(negativeNum/(positiveNum+negativeNum))
		positiveProb = sum(positiveProb)/len(self.hashtagList)
		negativeProb = sum(negativeProb)/len(self.hashtagList)
		if positiveProb+negativeProb==0:
			return {"positive":0,"negative":0}
		resultDict["positive"] = positiveProb
		resultDict["negative"] = negativeProb
		return resultDict