#coding=utf-8
#!/usr/bin/python2
#This Script Write By Tech Baba
#Do Not Copy This Script :)
try:
    import os
    import sys
    import time
    import urllib
    import platform
    import requests
except ImportError:
    os.system('pip2 install requests') #Module Not found Eror :(

#Loding Funcation :)
def baba(word):
    lix = ["[\033[1;92m■\033[1;97m□□□□□□□□□□□□□]","[\033[1;93m■■\033[1;97m□□□□□□□□□□□□]", "[\033[1;94m■■■\033[1;97m□□□□□□□□□□□]", "[\033[1;96m■■■■\033[1;97m□□□□□□□□□□]", "[\033[1;95m■■■■■\033[1;97m□□□□□□□□□]", "[\033[1;97m■■■■■■\033[1;97m□□□□□□□□]", "[\033[1;93m■■■■■■■\033[1;97m□□□□□□□]", "[\033[1;91m■■■■■■■■\033[1;97m□□□□□□]", "[\033[1;96m■■■■■■■■■\033[1;97m□□□□□]", "[\033[1;92m■■■■■■■■■■\033[1;97m□□□□]", "[\033[1;94m■■■■■■■■■■■\033[1;97m□□□]", "[\033[1;95m■■■■■■■■■■■■\033[1;97m□□]", "[\033[1;93m■■■■■■■■■■■■■\033[1;97m□]", "[\033[1;92m■■■■■■■■■■■■■■\033[1;97m]"]
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.09)
            sys.stdout.flush()
            
            logo = """
\033[1;97m
▒█░░░▄░░▒█░░▄█▀▄─▒▄█▀▀█▐██░▐█▀▀
▒█░░▒█░░▒█░▐█▄▄▐█▒▀▀█▄▄░█▌░▐█▀▀
░▒▀▄▀▒▀▄▀░░▐█─░▐█▒█▄▄█▀▐██░▐█──
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
||\033[0;97\033[0;41mWELCOME TO WASIF CREATION
||\033[0;97m\033[0;42mWhatsaap ||03451772008
||\033[0;97m\033[0;44mCreated \033[1;97mBy \033[1;93mWASIF
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈"""
    
    def home(): #main menu
    os.system("clear")
    print logo #raw
    print 47*("-")
    baba("   Bypass Processing => ")
    os.system("clear")
    print logo
    

if __name__ == '__main__':
    home()
