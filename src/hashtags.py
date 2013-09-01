from datalink import DatabaseConnectionDown
class hashtags:

	def extractHashtagTweet(self):
		self.hashtagList = []
		for i in self.tempTweet:
			try:
				if i[0] == '#':
					self.hashtagList.append(i)
			except:
				pass

	def analyseHashtagTweet(self, tweet):
		self.tempTweet = tweet.split(" ")
		self.extractHashtagTweet()
		if len(self.hashtagList)==0:
			return {'postive':0,'negative':0}

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
				#print tempLine[0]
				if i != tempLine[0]:
					continue
				else:
					#print tempLine
					positiveNum = float(tempLine[2])
					negativeNum = float(tempLine[3])
					#print positiveNum,negativeNum	
					positiveProb.append(positiveNum/(positiveNum+negativeNum))
					negativeProb.append(negativeNum/(positiveNum+negativeNum))
					#print positiveProb,negativeProb
				
		positiveProb = sum(positiveProb)/len(self.hashtagList)
		negativeProb = sum(negativeProb)/len(self.hashtagList)
		if positiveProb+negativeProb==0:
			return {'postive':0,'negative':0}
		resultDict["postive"] = positiveProb
		resultDict["negative"] = negativeProb
		return resultDict 

			


