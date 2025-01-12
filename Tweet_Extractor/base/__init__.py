
from Tweet_Extractor.base.auth_keys import *
from Tweet_Extractor.base.import_lib import *

BRAND_LIST__ : set = { }
FILTER_RETWEETS__ : bool = True
REFRESH_TIME__ : int = 0
NO_OF_TWEETS_TO_EXTRACT__ = 10

X_AUTHENTICATION : tweepy.OAuthHandler
X_API : tweepy.API