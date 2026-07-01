from textblob import TextBlob
from newspaper import Article

# url='https://en.wikipedia.org/wiki/Mathematics'
# url='https://indianexpress.com/article/long-reads/up-coaching-neet-paper-leak-student-protests-yogi-adityanath-akhilesh-yadav-2027-elections-10765007/?ref=hometop_hp'

# url='https://www.bbc.com/news/articles/cvgmv98ez3zo'

# url='https://pmc.ncbi.nlm.nih.gov/articles/PMC7470595/'

url='https://www.news18.com/cities/pune/ketan-agarwal-murder-cab-driver-bombshell-account-twist-lohagad-fort-sia-chetan-10178883.html'


article=Article(url)
article.download()
article.parse()
article.nlp()

text=article.summary
print(text)

blob=TextBlob(text)
sentiment=blob.sentiment.polarity
print("Sentiment Polarity:", sentiment) #-1 to 1, where -1 is very negative, 0 is neutral, and 1 is very positive

#to run this code in venv  terminal, use the following command:
# python main.py
# to activate venv,use the following command:
# .\.venv\Scripts\activate (use deactivate to deactivate the venv)