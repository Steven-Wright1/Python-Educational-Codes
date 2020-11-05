import requests
import urllib.request
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
from math import log



def getWashPostText(url,token):

    try:
        page = urllib.request.urlopen(url).read().decode('utf8')
    except:
        # if unable to download the URL, return title = None, article = None
        return (None,None)
    soup = BeautifulSoup(page, 'html.parser')
    if soup is None:
        return (None,None)
    # If we are here, it means the error checks were successful, we were
    # able to parse the page
    text = ""
    if soup.find_all(token) is not None:
        # Search the page for whatever token demarcates the article
        # usually '<article></article>'
        text = ''.join(map(lambda p: p.text, soup.find_all(token)))
        # mush together all the text in the <article></article> tags
        soup2 = BeautifulSoup(text)
        # create a soup of the text within the <article> tags
        if soup2.find_all('p')!=[]:
            # now mush together the contents of what is in <p> </p> tags
            # within the <article>
            text = ''.join(map(lambda p: p.text, soup2.find_all('p')))
    return text, soup.title.text


def getNYTText(url,token):
    response = requests.get(url)
    # THis is an alternative way to get the contents of a URL
    soup = BeautifulSoup(response.content, 'html.parser')
    page = str(soup)
    title = soup.find('title').text
    mydivs = soup.findAll("p", {"class":"story-body-text story-content"})
    text = ''.join(map(lambda p:p.text, mydivs))
    return text, title


def scrapeSource(url, magicFrag='2015',scraperFunction=getNYTText,token='None'):
    urlBodies = {}
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response, 'html.parser')
    # we are set up with a Soup of the page - now find the links
    # Remember that links are always of the form 
    # <a href='link-url'> link-text </a>
    numErrors = 0
    for a in soup.findAll('a'):
        try:
            url = a['href']
            if( (url not in urlBodies) and 
               ((magicFrag is not None and magicFrag in url) 
               or magicFrag is None)):
                body = scraperFunction(url,token)
                # this line above is important - scraperFunction 
                # refers to the individual scraper function for the 
                # new york times or the washington post etc.
                if body and len(body) > 0:
                    urlBodies[url] = body
                print(url)
        except:
            numErrors += 1
            # plenty of parse errors happen - links might not
            # be external links, might be malformed and so on -
            # so don't mind if there are exceptions.
    return urlBodies


class FrequencySummary:
    def __init__(self, min_cut = 0.1, max_cut = 0.9):
        self._min_cut = min_cut
        self.max_cut = max_cut
        self._stopwords = set(stopwords.words('english') + list(punctuation) + [u"'s",'"']) 

    def _compute_frequencies(self, word_sent, customStopWords = None):
        freq = defaultdict(int)
        
        # If we have entered in custom stop words we want to filter, we use .union
        # to unionise both stopword sets
        if customStopWords is None:
            stopwords = set(self._stopwords)
        else :
            stopwords  = set(self._stopwords).union(self.stopwords) 
    
         # Calculate the frequency of all words that aren't stopwords
        for sentence in word_sent:
             for word in sentence:
                 if word not in stopwords:
                     freq[words] += 1
        # Normalise frequencies by dividing value by m.
        # Remove words that occur too little or too often
        m = float(max(freq.values()))
        for word in list(freq.keys()):
            freq[word] = freq[word]/m
            if freq[word] >= self._max_cut or freq[word] <= self._min_cut:
                del freq[word]
        return freq

    def _extractFeatures(self, article, n, customStopWords = None):
        # Take article and reduce to sentences... then words
        text = article[0]
        title = article[1]
        sentences = sent_tokenize(text)
        word_sent = [word_tokenize(s.lower()) for s in sents]

        # Call compute frequencies to return the freq dictionary
        self.freq = self._compute_frequencies(word_sent, customStopWords)

        if n < 0:
            return nlargest(len(self._freq_keys()), self._freq, key=self._freq.get)
        else:
            return nlargest(n,self._freq,key=self._freq.get)
    
    # Set this function up to simply complete the frequency of words in the article
    # This will not normalise frequencies, or max and min filter. does remove stopwords
    def extractRawFrequencies(self,article):
        text = article[0]
        title = article[1]

        sentences = sent_tokenize(text)
        word_sent = [word_tokenize(s.lower()) for s in sents]
        freq = defaultdict(int)

        for s in word_sent:
            for word in s:
                if word not in self._stopwords:
                    freq[word] += 1
        return freq

    def summarise(self,article,n):
        text = article[0]
        title = article[1]
        
        sentences = sent_tokenize(text)
        word_sent = [word_tokenize(s.lower()) for s in sents]
        self._freq = self._compute_frequencies(word_sent)

        ranking = defaultdict(int)
        for i, sentence in enumerate(word_sent):
            for word in sentence:
                if word in self.freq:
                    ranking[i] += self.freq[word]
        sentences_index = nlargest(n, ranking, key = ranking.get())
        return [sentences[j] for j in sentences_index]
        

# These are the url's to WP and NYT's sports and tech pages. From these
# url's we want to download all relevant url's posted on these webpages
urlWashingtonPostNonTech = "https://www.washingtonpost.com/sports"
urlNewYorkTimesNonTech = "https://www.nytimes.com/pages/sports/index.html"
urlWashingtonPostTech = "https://www.washingtonpost.com/business/technology"
urlNewYorkTimesTech = "http://www.nytimes.com/pages/technology/index.html"
    

# To download ALL posted url's, use scrapesource(url, filter, urllib code, token)
washingtonPostTechArticles = scrapeSource(urlWashingtonPostTech,
                                          '2016',
                                         getWashPostText,
                                         'article') 
washingtonPostNonTechArticles = scrapeSource(urlWashingtonPostNonTech,
                                          '2016',
                                         getWashPostText,
                                         'article')
                
                
newYorkTimesTechArticles = scrapeSource(urlNewYorkTimesTech,
                                       '2016',
                                       getNYTText,
                                       None)
newYorkTimesNonTechArticles = scrapeSource(urlNewYorkTimesNonTech,
                                       '2016',
                                       getNYTText,
                                       None)


articleSummaries = {}
for techUrlDictionary in [newYorkTimesTechArticles, washingtonPostTechArticles]:
     for articleUrl in techUrlDictionary:
        if techUrlDictionary[articleUrl][0] is not None:
            if len(techUrlDictionary[articleUrl][0]) > 0:
                fs = FrequencySummarizer()
                summary = fs.extractFeatures(techUrlDictionary[articleUrl],25)
                articleSummaries[articleUrl] = {'feature-vector': summary,
                                               'label': 'Tech'}

for nontechUrlDictionary in [newYorkTimesNonTechArticles, washingtonPostNonTechArticles]:
    for articleUrl in nontechUrlDictionary:
        if nontechUrlDictionary[articleUrl][0] is not None:
            if len(nontechUrlDictionary[articleUrl][0]) > 0:
                fs = FrequencySummarizer()
                summary = fs.extractFeatures(nontechUrlDictionary[articleUrl],25)
                articleSummaries[articleUrl] = {'feature-vector': summary,
                                               'label': 'Non-Tech'}

#Function to get the article at the testUrl
def getDoxyDonkeyText(testUrl,token):
    response = requests.get(testUrl)
    soup = BeautifulSoup(response.content)
    page = str(soup)
    title = soup.find("title").text
    mydivs = soup.findAll("div", {"class":token})
    text = ''.join(map(lambda p:p.text,mydivs))
    return text,title

#TestUrl and TestArticle to return
testUrl = "http://doxydonkey.blogspot.in"
testArticle = getDoxyDonkeyText(testUrl,"post-body")


######################################################
#     Classification Using K-nearest Neighbour       #
######################################################
"""
We will do this by finding t articles with most similar feature vectors, and then
completing a majority vote from those 5 articles
"""
similarities = {}
for articleUrl in articleSummaries:
    oneArticleSummary = articleSummaries[articleUrl]['feature_vector']
    # for each article summary, test thhe length of intersection between summaries of both articles.
    similarities[articleUrl] = len(set(testArticleSummary)).intersection(set(oneArticleSummary))

labels = defaultdict(int)
knn = nlargest(5, similarities, key = similarities.get)
for oneNeighbour in knn:
    labels[articleSummaries[oneNeighbour]['label']] += 1

print(nlargest(1,labels, key = labels.get))
    






























































































    
















































    
            
                
             
