import nltk
#from nltk.book import *

# Moby Dick = Text 1, Sense and Sensibility = Text 2

#text1.concordance('monstrous')
#text2.concordance('monstrous')
#print('\n Austin uses the word monstrous in a similar content to the following words:')
#text2.similar('monstrous')

#Use tokenize to split text into words and sentences
from nltk.tokenize import word_tokenize, sent_tokenize
text = "Mary had a little lamb. Her fleece as white as snow."
sents = sent_tokenize(text)
print(sents)

words = [word_tokenize(sent) for sent in sents]
print(words)

#Let's filter out common stopwords
from nltk.corpus import stopwords
from string import punctuation

customStopWords = set(stopwords.words('english') + list(punctuation))
wordWOStopWords = [word for word in word_tokenize(text) if word not in customStopWords]
print(wordWOStopWords)

#nltk can also tag words as nouns, verbs, conjunctions etc.
print(nltk.pos_tag(word_tokenize(text)))





