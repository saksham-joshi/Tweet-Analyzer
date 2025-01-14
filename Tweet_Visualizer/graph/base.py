import plotly.express as Px

class XGraph :

    def __init__(this, __company_name : str, __positive_tweet_count : int = 0, __negative_tweet_count : int = 0 , __neutral_tweet_count : int = 0) :
        this._title = __company_name;
        this._positive_tweets : int = __positive_tweet_count
        this._negative_tweets : int = __negative_tweet_count
        this._neutral_tweets : int = __neutral_tweet_count
    
    def getBarGraph(this) : pass


GRAPH_OF_ALL__ : dict[str : XGraph] = {

    "Amazon" : XGraph("Amazon"),

    "Apple" : XGraph("Apple"),

    "Google" : XGraph("Google"),

    "Meta" : XGraph("Meta"),

    "Microsoft" : XGraph("Microsoft"),

    "Netflix" : XGraph("Netflix"),

    "Nvidia" : XGraph("Nvidia"),

    "Tesla" : XGraph("Tesla")
}