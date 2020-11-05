from newspaper import Article
import nltk


url = 'https://www.fool.co.uk/investing/2020/09/05/as-apple-stock-beats-the-ftse-100-heres-how-growth-shares-can-make-you-rich/'

article = Article(url)
article.download()
article.parse()
article.nlp()

print(article.summary)
