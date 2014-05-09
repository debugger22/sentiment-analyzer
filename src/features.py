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
        self.string = re.sub(
            r'\W+:\)\(\'\{\}\-\@\>\<\=\;\[\]\!',
            ' ',
            string).lower()
        self.string = self.string.replace('.', '')
        self.string = self.string.replace('?', '')
        self.words = self.string.split(" ")
        if self.words[-1] == '':  # how will something to to the -1 index?
            del self.words[-1]
        positiveEmoz = [
            ':)',
            ':-)',
            ':D',
            ':-D',
            ':P',
            ':-P',
            ';)',
            ';-)',
            ';D',
            ';-D',
            ':o)',
            ':]',
            ':3',
            ':c)',
            ':>',
            '=]',
            '8)',
            '=)',
            ':}',
            '8D',
            'xD',
            'XD',
            'X-D',
            '=D',
            '=3',
            ':-))',
            ':\')',
            'lol',
            'lol!']
        negativeEmoz = [
            ':(',
            ':-(',
            ':(',
            ':-(',
            ':-<',
            ':-[',
            ':[',
            ':{',
            ':-||',
            ':@',
            ':\'-(',
            ':\'(',
            'QQ',
            'D:',
            'D:<',
            'D8',
            'D;',
            'DX',
            'v.v',
            '>.<',
            'D=']
        positiveCount = 0
        negativeCount = 0
        for i in self.words:
            if i in positiveEmoz:
                positiveCount += 1
            if i in negativeEmoz:
                negativeCount += 1
        positiveEmoz, negativeEmoz = 0, 0
        if positiveCount + negativeCount == 0:
            return {'positive': 0, 'negative': 0}
        return {'positive': float(positiveCount) /
                (positiveCount +
                 negativeCount), 'negative': float(negativeCount) /
                (positiveCount +
                 negativeCount)}


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
        self.string = self.repairString(self.string)
        self.words = self.string.split(" ")
        if self.words[-1] == '':
            del self.words[-1]
        fin = open("data/negative.json", "r")
        negativeWords = json.loads(fin.read())
        fin.close()
        fin = open("data/positive.json", "r")
        positiveWords = json.loads(fin.read())
        fin.close()
        positiveScore = 0
        negativeScore = 0
        for i in self.words:
            testPositiveWord = self.compareWords(i, positiveWords)
            if testPositiveWord is not None:
                if positiveWords[testPositiveWord] == 'strong':
                    positiveScore += 1
                else:
                    positiveScore += 0.5
            testNegativeWord = self.compareWords(i, negativeWords)
            if testNegativeWord is not None:
                if negativeWords[testNegativeWord] == 'strong':
                    negativeScore += 1
                else:
                    negativeScore += 0.5

            '''
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
			'''
        if positiveScore + negativeScore == 0:
            return {'positive': 0, 'negative': 0}
        return {'positive': float(positiveScore) /
                (positiveScore +
                 negativeScore), 'negative': float(negativeScore) /
                (positiveScore +
                 negativeScore)}

    def compareWords(self, aString, aDict):
        '''
        This method takes a string and a dictionary as parameters and compares the string with
        the keys of dictionary using CompStrings method and returns the most suitable word match
        if the probability is greater that 0.9 otherwise it returns None
        '''
        probabilities = {}
        for i in aDict:
            probabilities[i] = self.compStrings(aString, i)
        maxProbab = 0
        for i in probabilities:
            if probabilities[i] > maxProbab:
                maxProbab = probabilities[i]
                correspondingWord = i
        probabilities = 0
        if maxProbab > 0.9:
            return correspondingWord
        else:
            return None

    def compStrings(self, str1, str2):
        '''
        This method takes two strings as parameters and checks if they are same or not
        It returns probability of the comparision
        '''
        str1 = list(str1)
        str2 = list(str2)
        total = len(str1)
        count = 0
        for i in str1:
            try:
                str2.index(i)
                count += 1
            except:
                pass
        try:
            para1 = float(count) / float(total)
        except:
            para1 = 0
        count = 0
        total = len(str2)
        for i in str2:
            try:
                str1.index(i)
                count += 1
            except:
                pass
        try:
            para2 = float(count) / float(total)
        except:
            para2 = 0
        return (para1 + para2) / 2

    def repairString(self, string):
        data = {
            'm': 'am',
            'u': 'you',
            'yrs': 'years',
            'ur': 'your',
            'urs': 'yours',
            'tc': 'take care',
            'gn': 'good night',
            'nite': 'night',
            'wat': 'what',
            'abt': 'about',
            'k': 'okay',
            'kk': 'okay',
            'ok': 'okay',
            'don\'t': 'do not',
            'won\'t': 'will not',
            'gonna': 'going to',
            'juz': 'just',
            'jus': 'just',
            'fk': 'fuck',
            'wtf': 'what the fuck',
            'shud': 'should',
            'coz': 'because',
            'cos': 'because'}
        string = string.split(" ")
        for i in string:
            if i in data:
                string[string.index(i)] = data[i]
        return " ".join(string)
