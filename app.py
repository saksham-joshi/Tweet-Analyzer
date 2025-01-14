from Tweet_Extractor import *
from Tweet_Sentiment import analyzer
from Tweet_Visualizer import *


if __name__ == "__main__" :
    try :    
        setupTweetExtractor()
        TWEET_APP__.run(debug=True, host="0.0.0.0", port= 5000)
    
    except XException_AuthenticationKeysNotFound as __excep:
        print(__excep)