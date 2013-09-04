Tweet-Analysis
==============

A Python module to do a set of operations on tweets. It uses a collection of stopwords to train a dataset for the sentiment analysis. It uses the basic principle of bag-of-words used for natural language processing.

Dependencies
------------
* numpy
* matplotlib(To plot sentiments)

How to use
----------
```python
from src import features

a = features.Emoticons()
print a.analyse("What if BJP loses its next election :(?")

b = features.DictionaryTest()
print b.analyse("Possibility of Narendra Modi to become the prime minister of India is really high.")
```
<strong>Output</strong>
```python
{'positive': 0.0, 'negative': 1.0}
{'positive': 1.0, 'negative': 0.0}
```
Progress
--------
- [x] Emoticons: This class uses emoticons detection to classify the passed string as positive or negative
- [x] DictionaryTest: This class uses a set of English words and their subjectivity to give a score to a string
- [ ] AllCaps
- [ ] ElongatedWords
- [ ] HashTags
- [ ] Negation
- [ ] Punctuation

Team Members
------------
<table border="0">
<tr><td>Sudhanshu Mishra</td><td> mrsud94@gmail.com</td></tr>
<tr><td>Ambar Mehrotra</td><td>ambar.prince@gmail.com</td></tr>
</table>
