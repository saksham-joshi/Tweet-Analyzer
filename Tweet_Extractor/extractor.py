from Tweet_Extractor.setup import *

def setupTweetExtractor() -> None :
    loadAuthenticationData()
    authenticateX()
    loadExtractorArgs()

class XExtractor :

    def __init__(this, __brand_name : str) :
        this._brandname = "#" + __brand_name
        this._query = XExtractor.prepareQuery(__brand_name)

    @staticmethod
    def prepareQuery(__brand_name : str) -> str :
        return f"#{__brand_name} {"-filter:retweets" if FILTER_RETWEETS__ else ""}"



