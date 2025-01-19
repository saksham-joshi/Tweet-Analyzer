from Tweet_Visualizer.util import *

# def setupTweetVisualizer() :
    
#     # generating cache ...
#     with CONTEXT_APP:
#         global INDEX_TEMPLATE__ , RESPONSE_TO_404 , COMPANY_DATA_NOT_PROVIDED_BY_US , GRAPH_TOGETHER_OF_ALL_BRANDS__
#         print(">>>>>>>>>>>> Setting Visualizer ...")
#         INDEX_TEMPLATE__ = generateIndexHtmlTemplate()

#         GRAPH_TOGETHER_OF_ALL_BRANDS__ = generateTogetherGraph()

#         RESPONSE_TO_404 = jsonify( {
#             "error" : "data not found",
#             "response-status" : 404,
#             "message" : "Your request is invalid. Visit 'https://github.com/saksham-joshi/Tweet-Analyzer' to learn more!"
#         } ) , 404

#         # if we do not provide data for a certain company then this response is used
#         COMPANY_DATA_NOT_PROVIDED_BY_US = jsonify({
#                     "response_status" : 404,
#                     "message" : f"We do not provide data for the given company."
#                 } ), 404
        
with CONTEXT_APP :

        INDEX_TEMPLATE__ = render_template("index.html")

        GRAPH_TOGETHER_OF_ALL_BRANDS__ = generateTogetherGraph()

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
