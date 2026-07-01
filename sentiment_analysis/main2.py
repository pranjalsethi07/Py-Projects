from textblob import TextBlob

with open('mytext.txt', 'r') as f:
    text=f.read()

blob=TextBlob(text)
sentiment=blob.sentiment.polarity
print("Sentiment Polarity:", sentiment) #-1 to 1, where -1 is very negative, 0 is neutral, and 1 is very positive

#to run this code in venv  terminal, use the following command:
# python main.py