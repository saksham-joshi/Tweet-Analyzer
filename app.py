from Tweet_Extractor import *
from Tweet_Sentiment import *
from Tweet_Visualizer import *


if __name__ == "__main__" or __name__ == "app" :
    try :
        print("\n Launching the APP!")
        setupTweetExtractor()
        #setupTweetVisualizer()
        TWEET_APP__.run(debug=True, host="0.0.0.0", port= 5000)
    
    except XException_AuthenticationKeysNotFound as __excep:
        print(__excep)