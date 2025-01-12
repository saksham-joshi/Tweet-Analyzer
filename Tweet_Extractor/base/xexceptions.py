
class XException_AuthenticationKeysNotFound (Exception) :

    def __init__(this) :
        this._message = "\n | Reason: Unable to find authentication keys like Api key, Access token etc.\n | Solution: Run 'setup.py' in root directory!"
        super().__init__(this._message)
    
    def __str__(this) : return this._message

class XException_ArgsNotFound (Exception) :

    def __init__(this) :
        this._message = "\n | Reason: Cannot find 'args.json' which contains arguments to customize working of the Project."
        super().__init__(this._message)
    
    def __str__(this) : return this._message