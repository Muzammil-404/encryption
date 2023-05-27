import os,platform

os.system('git pull')

 

x=platform.architecture()[0]

if x=="32bit":

    print('Sorry 32 Bit Not Supported...')

elif x=="64bit":



    __import__("encryption")
