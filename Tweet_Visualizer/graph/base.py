import plotly.express as Px

class XGraph :

    def __init__(this, __company_name : str) :
        this._title = __company_name;
        this._positive_tweets : int = 0
        this._negative_tweets : int = 0
        this._neutral_tweets : int = 0
    
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