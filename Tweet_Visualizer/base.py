from flask import Flask, render_template , jsonify
from flask_cors import CORS
from typing import Final
from Tweet_Visualizer.graph import *

TWEET_APP__ = Flask(__name__)

CORS(TWEET_APP__)

CONTEXT_APP = TWEET_APP__.app_context()

TOTAL_WEBSITE_VISITORS__ : int = 0
TOTAL_DATA_FETCHES__ : int = 0

URL_TO_COMPANY_DATA_NOT_AVAILABLE_IMAGE : Final = "https://cdn.jsdelivr.net/gh/saksham-joshi/Tweet-Analyzer@main/Tweet_Visualizer/static/img/sorry_image.png"
    
# store the rendered template of main html page
INDEX_TEMPLATE__ = None

# stores the dictionary to response for 404 error
RESPONSE_TO_404 = None

# if we do not provide data for a certain company then this response is used
COMPANY_DATA_NOT_PROVIDED_BY_US = None