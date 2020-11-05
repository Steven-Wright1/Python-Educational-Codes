from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest


#This class computes the frequency of words. It thhen removes stopwords and punctuation
#It then removes the words below and above the 10th and 90th frequency percentiles
class FrequencySummary:
    #create constructor - function called every time object of class is instantiated
    def __init__(self, min_cut=0.1, max_cut=0.9):
        self.min_cut = min_cut  #Assign cut values to member variables
        self.max_cut = max_cut
        #Set stopwords as english stopwords and punctutation
        self.stopwords = set(stopwords.words('english') + list(punctuation))

    #This member function takes in the list of sentences, and outputs a dictionary
    #where the keys are words and the values are frequency
    def _compute_frequencies(self, word_sent):

        freq = defaultdict(int)         #intialise a defaultdict to store key-value pairs
        #iterate through words and sentences.
        for sentences in word_sent:
            for word in sentences:
                if word not in self.stopwords:
                    freq[word] +=1  #Defaultdict allows us to create a new key-value pair, if the word isn't in the dictionary, which is obviously the case at the start

        #from here want to normalise frequencies by dividing freq by modal word
        #then want to filter out words occuring too little or too often
        max_freq = float(max(freq.values()))
        for word in list(freq.keys()):
            freq[word] = freq[word]/max_freq
            if freq[word] >= self.max_cut or freq[word] <= self.min_cut:
                del freq[word]
        return freq


    def summarise(self,text,n): # n = number of sentences
        sents = sent_tokenize(text) #Breaks text down into sentences

        #assert will throw an error if the statement is not true. used for sanity checks
        assert n <= len(sents) #assert than n is not greater than the number of setences

        #This line takes every sentence s, in the list sents, and then tokenizes it,
        #to return the list of words in the sentence
        word_sent = [word_tokenize(s.lower()) for s in sents]

        #Call the compute frequencies function
        self._freq = self._compute_frequencies(word_sent)
        rankings = defaultdict(int) #create an empty dictionary
        for i,sent in enumerate(word_sent):
            for word in sent:
                if word in self._freq:
                    rankings[i] += self._freq[word]    #This is used to rank each sentence, by iterating through each word in the sentence, and adding the frequen
        #This code find the nlargest sentences
        sents_idx = nlargest(n,rankings, key=rankings.get)
        return[sents[j] for j in sents_idx]

from bs4 import BeautifulSoup
import urllib.request


def get_only_text_from_washington_post_url(url):
    #This code is specific to the washington post, due to the structure of the html page

    #Page is a long string containing all the html of the website
    page = urllib.request.urlopen(url).read().decode('utf8')

    soup = BeautifulSoup(page, 'html.parser')


    # use this code to get everything in that text that lies between a pair of 
    # <article> and </article> tags. We do this because we know that the URLs we are currently
    # interested in - those from the WashingtonPost have this nice property
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
    soup2 =  BeautifulSoup(text, 'html.parser')
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text

                
someUrl = "https://www.washingtonpost.com/news/the-switch/wp/2015/08/06/why-kids-are-meeting-more-strangers-online-than-ever-before/"
text_of_url = get_only_text_from_washington_post_url(someUrl)
print(text_of_url)

#instantiate fs as an object of the frequency summary class.
#Immediately, the FrequencySummary class constructor will be called
fs = FrequencySummary()

#text_of_url[0] is the title so text_of_url[1] is the text.
summary = fs.summarise(text_of_url[1],3)
print(summary)



























                
                
    
    
         
        
            
        
        



































