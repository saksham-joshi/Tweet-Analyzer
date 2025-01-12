from Tweet_Extractor.base import *

def loadAuthenticationData() -> None :

    global X_API_KEY, X_API_SECRET_KEY , X_ACCESS_TOKEN , X_ACCESS_SECRET_TOKEN

    try :
        with open("Tweet_Extractor/base/assets/auth.json") as auth_json_file :
            dit = load(auth_json_file)

            X_API_KEY = dit[X_JSON_KEY_OF_API_KEY]
            X_API_SECRET_KEY = dit[X_JSON_KEY_OF_API_SECRET_KEY]
            X_ACCESS_TOKEN = dit[X_JSON_KEY_OF_ACCESS_TOKEN]
            X_ACCESS_SECRET_TOKEN = dit[X_JSON_KEY_OF_ACCESS_SECRET_TOKEN]

    except FileNotFoundError as __excep:
        print(__excep)
        raise XException_AuthenticationKeysNotFound()


def loadExtractorArgs() -> None :

    global BRAND_LIST__ , REFRESH_TIME__ , FILTER_RETWEETS__ , NO_OF_TWEETS_TO_EXTRACT__
    try :
        with open("Tweet_Extractor/base/assets/args.json") as setupdatafile :
            dit = load(setupdatafile)
            
            BRAND_LIST__ = dit["brands-list"]
            REFRESH_TIME__ = dit["refresh-time"]
            FILTER_RETWEETS__ = dit["filter-retweets"]
            NO_OF_TWEETS_TO_EXTRACT__ = dit["no-of-tweets-to-extract"]
    except :
        raise XException_ArgsNotFound()


def authenticateX() -> None :
    global X_AUTHENTICATION , X_API

    X_AUTHENTICATION = tweepy.OAuthHandler( X_API_KEY , X_API_SECRET_KEY)
    X_AUTHENTICATION.set_access_token(X_ACCESS_TOKEN , X_ACCESS_SECRET_TOKEN)

    X_API = tweepy.API(X_AUTHENTICATION)
