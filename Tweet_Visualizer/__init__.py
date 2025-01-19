from Tweet_Visualizer.cache import *

@TWEET_APP__.route('/')
def getIndexHtml() : 
    global TOTAL_WEBSITE_VISITORS__ , TOTAL_DATA_FETCHES__

    TOTAL_WEBSITE_VISITORS__ += 1

    return INDEX_TEMPLATE__


# function to display graphs of particulars companies
@TWEET_APP__.route('/get-graph/<__company_name>', methods= ['GET'])
def getGraphOfCompany(__company_name : str) : 

    incrementTotalDataFetches()

    graph_to_transmit : XGraph = GRAPH_DICT_OF_ALL__.get(__company_name, None)

    if graph_to_transmit is None : return COMPANY_DATA_NOT_PROVIDED_BY_US

    return graph_to_transmit.getJsonifiedGraphResponse()



@TWEET_APP__.route('/get-data/<__company_name>' , methods= ['GET'])
def getJsonData(__company_name) :

    incrementTotalDataFetches()

    xgraph_obj : XGraph = GRAPH_DICT_OF_ALL__.get(__company_name, None)

    if xgraph_obj is None : return COMPANY_DATA_NOT_PROVIDED_BY_US
        
    return xgraph_obj.getJsonifiedDataResponse()


@TWEET_APP__.route('/get-graph-of-all')
def getGraphOfAll() :
    incrementTotalDataFetches()
    return GRAPH_TOGETHER_OF_ALL_BRANDS__



@TWEET_APP__.route('/get-site-stats')
def getSiteStats() :
    return jsonify ( {
        "total-data-fetches" : TOTAL_DATA_FETCHES__,
        "total-site-visits" : TOTAL_WEBSITE_VISITORS__
    } ) , 200



@TWEET_APP__.errorhandler(404)
def handleError404(__error) :
    return RESPONSE_TO_404