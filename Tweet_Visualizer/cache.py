from Tweet_Visualizer.base import *

# store the rendered template of main html page
INDEX_TEMPLATE__ = None

# stores the dictionary to response for 404 error
RESPONSE_TO_404 = None

# if we do not provide data for a certain company then this response is used
COMPANY_DATA_NOT_PROVIDED_BY_US = None

# generating cache ...
with TWEET_APP__.app_context() :

    INDEX_TEMPLATE__ = render_template("index.html" , total_website_visitors= TOTAL_WEBSITE_VISITORS__ , total_data_fetches= TOTAL_DATA_FETCHES__ , graph_figure= GRAPH_TOGETHER_OF_ALL_BRANDS__ )

    RESPONSE_TO_404 = jsonify( {
        "error" : "data not found",
        "response-status" : 404,
        "message" : "Your request is invalid. Visit 'https://github.com/saksham-joshi/Tweet-Analyzer' to learn more!"
    } ) , 404

    # if we do not provide data for a certain company then this response is used
    COMPANY_DATA_NOT_PROVIDED_BY_US = jsonify({
                "response_status" : 404,
                "message" : f"We do not provide data for the given company."
            } ), 404
    
    
