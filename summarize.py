from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
import pandas as pd

with open('shengine.txt') as f1:
	data = f1.read().decode('utf-8','ignore').replace("\n"," ").replace(u"\u2019","'").replace(u"\u2018","'")
data.encode('ascii','ignore')
sents = sent_tokenize(data)
for i in sents:
	i.encode('ascii','ignore')
words = word_tokenize(data.lower())
mystops = set(stopwords.words('english')+list(punctuation))
words = [word for word in words if word not in mystops]
freq = FreqDist(words)
print(pd.DataFrame(list(freq.items()), columns = ["Word","Frequency"]))
#print(nlargest(10,freq, key = freq.get))   #count for the word
ranking = defaultdict(int)
for i,sent in enumerate(sents):
	for w in word_tokenize(sent.lower()):
		if w in freq:
			ranking[i] +=freq[w]

final_numbers = nlargest(3,ranking,key=ranking.get)
print(final_numbers)
print([sents[j] for j in sorted(final_numbers)])
