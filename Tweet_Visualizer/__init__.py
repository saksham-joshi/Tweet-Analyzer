from flask import Flask, render_template , Response , jsonify , url_for
from flask_cors import CORS
from flask_socketio import SocketIO
from typing import Final
from json import dumps
from Tweet_Visualizer.graph import *

TWEET_APP__ = Flask(__name__)
TWEET_SOCKET__ = SocketIO(TWEET_APP__)

CORS(TWEET_APP__)

TOTAL_WEBSITE_VISITORS__ : int = 0
TOTAL_DATA_FETCHES__ : int = 0

URL_TO_COMPANY_DATA_NOT_AVAILABLE_IMAGE : Final = "https://cdn.jsdelivr.net/gh/saksham-joshi/Tweet-Analyzer@main/Tweet_Visualizer/static/sorry_image.png"


@TWEET_APP__.route('/')
def getIndexHtml() : 
    global TOTAL_WEBSITE_VISITORS__ , TOTAL_DATA_FETCHES__
    TOTAL_WEBSITE_VISITORS__ += 1
    return render_template("index.html", total_website_visitors= TOTAL_WEBSITE_VISITORS__, total_data_fetches= TOTAL_DATA_FETCHES__, graph_figure= GRAPH_TOGETHER_OF_ALL_BRANDS__ )


# function to display graphs of particulars companies
@TWEET_APP__.route('/company/<__company_name>', methods= ['GET'])
def getGraphOfCompany(__company_name : str) : 
    global TOTAL_DATA_FETCHES__

    TOTAL_DATA_FETCHES__ += 1

    graph_to_transmit = GRAPH_DICT_OF_ALL__.get(__company_name, None)

    if graph_to_transmit is None : 
        return jsonify( {
            "response_status" : 400,
            "url" : URL_TO_COMPANY_DATA_NOT_AVAILABLE_IMAGE
        } )

    return jsonify({
        "response_status" : 200,
        "graph" : Pio.to_json(graph_to_transmit.getBarGraph())
    })


@TWEET_APP__.errorhandler(404)
def handleError404(__error) :
    return jsonify( {
        "error" : "not found",
        "code" : 404,
        "message" : "Your requests is invalid. Visit 'https://github.com/saksham-joshi/Tweet-Analyzer' to learn more!"
    } )