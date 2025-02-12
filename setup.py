


#=====| Installation of all required libraries |=====#
from os import system
system("pip install -r requirements.txt")








# #=====| Saving authentication keys |=====#
# from Tweet_Extractor.base.auth_keys import *
# from json import dump
# print('''
# +====================================================================================================+   
# |      Hey there! Saksham Joshi(https://sakshamjoshi.vercel.app) this side,                          |
# |        Now to complete the setup you have to enter authentication keys which you can               |
# |        find at "https://developer.x.com/en/products/x-api". Follow the below step:                 |
# |                                                                                                    |
# |        [+] Step 1: Visit the above link.                                                           |
# |        [+] Step 2: Scroll down and choose your plan among Free, Basic, Pro and Enterprise.         |
# |        [+] Step 3: Login to X and if already, visit "https://developer.x.com/en/portal/dashboard". |
# |        [+] Step 4: Now create a new project which will create new authentication keys.             |
# |        [+] Step 5: Enter your new keys below.                                                      |
# +====================================================================================================+
# ''')

# try :
#     with open("Tweet_Extractor/base/assets/auth.json") as file :
#         if input("\n Authentication keys are already set before. If you overwrite them, the old data will be lost!\n\t Press 'N' or 'n' to not overwrite them else press anything else :_") in ['N' ,'n'] : pass
#         else : raise FileNotFoundError()
# except : 
#     with open("Tweet_Extractor/base/assets/auth.json", 'w') as keyfile :
#         dit : dict = {}

#         dit[X_JSON_KEY_OF_API_KEY] = input("\n ==> Enter the API Key :-_")
#         dit[X_JSON_KEY_OF_API_SECRET_KEY] = input(" ==> Enter the API Secret Key :-_")
#         dit[X_JSON_KEY_OF_ACCESS_TOKEN] = input(" ==> Enter the Access Token :-_")
#         dit[X_JSON_KEY_OF_ACCESS_SECRET_TOKEN] = input(" ==> Enter the Access Secret Token :-_")

#         dump(dit , keyfile , indent=4)
#         print("\n <==| Authentication keys saved succesfully! |==>")





#==========| Final Message |==========#
print("""
            +-----------------------------+      
            |    Setup done perfectly!    |
            +-----------------------------+      
""")
