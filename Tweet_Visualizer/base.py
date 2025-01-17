from flask import Flask, render_template , jsonify
from flask_cors import CORS
from typing import Final
from Tweet_Visualizer.graph import *

TWEET_APP__ = Flask(__name__)

CORS(TWEET_APP__)

TOTAL_WEBSITE_VISITORS__ : int = 0
TOTAL_DATA_FETCHES__ : int = 0

URL_TO_COMPANY_DATA_NOT_AVAILABLE_IMAGE : Final = "https://cdn.jsdelivr.net/gh/saksham-joshi/Tweet-Analyzer@main/Tweet_Visualizer/static/img/sorry_image.png"


def incrementTotalDataFetches() : 
   global TOTAL_DATA_FETCHES__
   TOTAL_DATA_FETCHES__ += 1
    