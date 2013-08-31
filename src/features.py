'''
	Author: Sudhanshu Mishra
	Email: mrsud94@gmail.com
'''
import re
import json

class Emoticons:
	'''
		This class uses emoticons detection to classify the passed string as positive or negative
	'''
	def analyse(self, string):
		'''
			This method takes a string as parameter and returns a dictionary of
			probabilities of sentiment of the string
			keys: 'positive', 'negative'
			If the test fails, both the keys will have value equal to 0
		'''
		self.string = re.sub(r'\W+:\)\(\'\{\}\-\@\>\<\=\;\[\]\!', ' ', string).lower()
		self.string = self.string.replace('.', '')
		self.string = self.string.replace('?', '')
		self.words = self.string.split(" ")
		if self.words[-1] == '':#how will something to to the -1 index?
			del self.words[-1]
		positiveEmoz = [':)', ':-)', ':D', ':-D', ':P', ':-P', ';)', ';-)', ';D', ';-D', ':o)', ':]', ':3',\
		 ':c)', ':>', '=]', '8)', '=)', ':}', '8D', 'xD', 'XD', 'X-D', '=D', '=3', ':-))', ':\')', 'lol', 'lol!']
		negativeEmoz = [':(', ':-(', ':(', ':-(', ':-<', ':-[', ':[', ':{', ':-||', ':@', ':\'-(', ':\'('\
			, 'QQ', 'D:', 'D:<', 'D8', 'D;', 'DX', 'v.v', '>.<', 'D=']
		positiveCount = 0
		negativeCount = 0
		for i in self.words:
			if i in positiveEmoz:
				positiveCount += 1
			if i in negativeEmoz:
				negativeCount += 1
		positiveEmoz, negativeEmoz = 0,0
		if positiveCount + negativeCount == 0:
			return {'positive':0,'negative':0}
		return {'positive':float(positiveCount)/(positiveCount+negativeCount),\
		'negative':float(negativeCount)/(positiveCount+negativeCount)}


class DictionaryTest:
	'''
		This class uses a set of English words and their subjectivity to give a score to a string
	'''
	def analyse(self, string):
		'''
			This method takes a string as parameter and returns a dictionary of
			probabilities of sentiment of the string
			keys: 'positive', 'negative'
			If the test fails, both the keys will have value equal to 0
		'''
		self.string = re.sub(r'\W+', ' ', string).lower()
		self.words = self.string.split(" ")
		if self.words[-1] == '':
			del self.words[-1]
		fin = open("data/negative.json","r")
		negativeWords = json.loads(fin.read())
		fin.close()
		fin = open("data/positive.json","r")
		positiveWords = json.loads(fin.read())
		fin.close()
		positiveScore = 0
		negativeScore = 0
		for i in self.words:
			if i in positiveWords:
				if positiveWords[i]=='strong':
					positiveScore += 1
				else:
					positiveScore += 0.5 
			if i in negativeWords:
				if negativeWords[i]=='strong':
					negativeScore += 1
				else:
					negativeScore += 0.5
		if positiveScore + negativeScore == 0:
			return {'positive':0,'negative':0}
		return {'positive':float(positiveScore)/(positiveScore+negativeScore),\
		'negative':float(negativeScore)/(positiveScore+negativeScore)}