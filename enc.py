import os, sys , platform
    
try:
    __import__("encryption")
except Exception as e:
    exit(str(e))
