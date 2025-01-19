from textblob import TextBlob

def getTypeOfSentiment(__polarity_score : float) -> str :
    return "Positive" if __polarity_score > 0 else "Neutral" if __polarity_score == 0 else "Negative"

def getSentiment(__tweet : str) -> str :
    return getTypeOfSentiment(TextBlob(__tweet).polarity)
