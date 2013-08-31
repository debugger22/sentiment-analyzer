Tweet-Analysis
==============

A Python module to do a set of operations on tweets. It uses a collection of stopwords to train a dataset for the sentiment analysis. It uses the basic principle of bag-of-words used for natural language processing.
<br/><br/>

<strong>How to use</strong>

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
<br/>
<hr/>
<strong>Team Members</strong>
<ul>
<li>Sudhanshu Mishra mrsud94@gmail.com</li>
<li>Ambar Mehrotra ambar.prince@gmail.com</li>
</ul>
