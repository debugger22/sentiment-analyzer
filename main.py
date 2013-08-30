from src import features

a = features.Emoticons()
print a.analyse("What if BJP loses its next election :(?")

b = features.DictionaryTest()
print b.analyse("Possibility of Narendra Modi to become the prime minister of India is really high.")