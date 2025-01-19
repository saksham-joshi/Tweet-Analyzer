from Tweet_Visualizer.base import *

generateIndexHtmlTemplate  = lambda : render_template("index.html" , total_website_visitors= TOTAL_WEBSITE_VISITORS__ , total_data_fetches= TOTAL_DATA_FETCHES__)

def updateIndeHtmlTemplate() :
   generateIndexHtmlTemplate()

def incrementTotalDataFetches() : 
   global TOTAL_DATA_FETCHES__
   TOTAL_DATA_FETCHES__ += 1