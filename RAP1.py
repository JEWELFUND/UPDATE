import os, platform
try:
        import requests
except:
        os.system('pip2 install requests')
 
import requests
bit = platform.architecture()[0]
if bit == "64bit":
        from number64 import RAP
        reg()
elif bit == "32bit":
        from number32 import RAP
        reg()
