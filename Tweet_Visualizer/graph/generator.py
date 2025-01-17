from plotly.express import bar
from plotly.io import to_json , to_html
from flask import jsonify

class XGraph :

    def __init__(this, __company_name : str, __positive_tweet_count : int = 0, __negative_tweet_count : int = 0 , __neutral_tweet_count : int = 0) :
        this._brand = __company_name.capitalize();
        this._positive_tweets : int = __positive_tweet_count
        this._negative_tweets : int = __negative_tweet_count
        this._neutral_tweets : int = __neutral_tweet_count
        this._bar_graph_json = None
        this._jsonified_graph_response = None
        this._jsonified_data_response = None
    

    def getBarGraph(this) :
        if this._bar_graph_json is None :
            this._bar_graph_json = to_json( bar ( {
                    "Sentiments" : ["Positive" , "Neutral" , "Negative"],
                    "Count" : [this._positive_tweets , this._neutral_tweets , this._negative_tweets]}, 
                    x = "Sentiments" , y = "Count", title= f"Analysis for '{this._brand}'\nin the last 7 days.",
                    color_discrete_sequence= ["#20A6DF"]
                ) )
        return this._bar_graph_json
    

    def getTweetsCount(this) -> dict[str , int] :
        return {
            "positive-tweets-count" : this._positive_tweets,
            "negative-tweets-count" : this._negative_tweets,
            "neutral-tweets-count" : this._neutral_tweets
        }
    

    def getJsonifiedGraphResponse(this) :
        
        if this._jsonified_graph_response is None :
            this._jsonified_graph_response = jsonify( {
                "response_status" : 200,
                "graph" : this.getBarGraph()
            } )

        return this._jsonified_graph_response , 200
    

    def getJsonifiedDataResponse(this) :
        if this._jsonified_data_response is None :

            this._jsonified_data_response = jsonify({

                "company-name" : this._brand,
                "response-status" : 200,
                "counts" : this.getTweetsCount()
            }) , 200

        return this._jsonified_data_response

GRAPH_DICT_OF_ALL__ : dict[str : XGraph] = {

    "amazon" : XGraph("Amazon", 100, 5, 15),

    "apple" : XGraph("Apple", 30, 50, 15),

    "google" : XGraph("Google", 80, 25, 5),

    "meta" : XGraph("Meta", 10, 5, 150),

    "microsoft" : XGraph("Microsoft" , 70, 50, 8),

    "netflix" : XGraph("Netflix", 55, 5, 15),

    "nvidia" : XGraph("Nvidia", 100, 57, 5),

    "tesla" : XGraph("Tesla", 150, 75, 8)
}

GRAPH_TOGETHER_OF_ALL_BRANDS__ = None

def generateTogetherGraph() :
    global GRAPH_DICT_OF_ALL__
    brands = []
    positive_counts = []
    neutral_counts = []
    negative_counts = []

    for brand, graph_obj in GRAPH_DICT_OF_ALL__.items():

        brands.append(brand)

        positive_counts.append(graph_obj._positive_tweets)

        neutral_counts.append(graph_obj._neutral_tweets)

        negative_counts.append(graph_obj._negative_tweets)


    return jsonify ( to_json ( bar ( {

        "Brands": brands * 3,
        
        "Sentiments": ["Positive"] * len(brands) + ["Neutral"] * len(brands) + ["Negative"] * len(brands),
        
        "Count": positive_counts + neutral_counts + negative_counts
    
    }, x="Brands", y="Count", color="Sentiments", barmode="group", title= "Analysis for all brands in last 7 days."
     
     , color_discrete_sequence= ["#00cc96" , "#636efa" , "#ef553b"] ) ) ) , 200