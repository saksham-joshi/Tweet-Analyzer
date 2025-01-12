from Tweet_Extractor import *
#from Tweet_Sentiment import analyzer
#from Tweet_Visualizer import *


if __name__ == "__main__" :
    try :
         setupTweetExtractor()
    except XException_AuthenticationKeysNotFound as __excep:
        print(__excep)


