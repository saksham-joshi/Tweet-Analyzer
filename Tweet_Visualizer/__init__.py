from flask import Flask, render_template , Response , jsonify , url_for
from flask_cors import CORS
from Tweet_Visualizer.graph import *

TWEET_APP__ = Flask(__name__)

CORS(TWEET_APP__)

TOTAL_WEBSITE_VISITORS__ : int = 0
TOTAL_DATA_FETCHES__ : int = 0

@TWEET_APP__.route('/')
def getIndexHtml() : 
    global TOTAL_WEBSITE_VISITORS__ , TOTAL_DATA_FETCHES__
    TOTAL_WEBSITE_VISITORS__ += 1
    return render_template("index.html", total_website_visitors= TOTAL_WEBSITE_VISITORS__, total_data_fetches= TOTAL_DATA_FETCHES__, graph_figure = open("Tweet_Visualizer/static/sorry_image.png"))

@TWEET_APP__.route('/company/<__company_name>')
def getGraphOfCompany(__company_name : str) : 
    graph_to_transmit = GRAPH_OF_ALL__.get(__company_name, None)

    if graph_to_transmit == None : Response()

    return graph_to_transmit
