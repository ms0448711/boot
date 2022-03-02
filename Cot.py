# -*- coding: utf-8 -*
#!/usr/bin/python
#####################################
##Jenderal92 - AjibarangCrew -  Priv8##
#### PS: CHANGE Your Threads pool on line 69 to make script more faster :)
#### code by Jenderal92 thanks to h0d3_g4n - KILL THE NET####
##############[LIBS]###################
import requests, re, urllib2, os, sys, codecs, random               
from multiprocessing.dummy import Pool                          
from time import time as timer  
import time
import json                     
from platform import system 
from colorama import Fore                               
from colorama import Style                              
from pprint import pprint                               
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)

ktnred = '\033[31m'
ktngreen = '\033[32m'
ktn3yell = '\033[33m'
ktn4blue = '\033[34m'
ktn5purp = '\033[35m'
ktn6blueblue = '\033[36m'
ktn7grey = '\033[37m'
CEND = '\033[0m' 

def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

        x = """      _  ___ ____          ____       _       ___  
     | |/ _ \___ \        |  _ \ _ __(_)_   _( _ ) 
  _  | | (_) |__) |  _____| |_) | '__| \ \ / / _ \ 
 | |_| |\__, / __/  |_____|  __/| |  | |\ V / (_) |
  \___/   /_/_____|       |_|   |_|  |_| \_/ \___/ 
Jenderal92 - BotMet Auto Exploiter Bot 2k20!!!

Youtube : Logic Internet
ICQ : https://icq.im/Shin403

 [+] 1. PHP Unit Unit Priv8
 [+] 2. PHP Unit Get Twilo+Get Env+Upload Shell
 [+] 3. Dork Maker
 [+] 4. Dork Scanner
 [+] 5. AnonymousFox V4
 [+] 6. kil3rDz Bot
 [+] 7. Zone-h Mass Poster
 [+] 8. 3xBeast V2
 [+] 9. Get Smtp On .env
 [+] 10. Get Ip From Domain
 [+] 11. Duplicate Domain
 [+] 12. Reverse Ip
 [+] 13. Joomla Brute
 [+] 14. Opencart Brute
 [+] 15. JEx BotV4
 [+] 16. JEx BotV5
 [+] 17. Zombie BotV12
 [+] 18. Zombie BotV13
 [+] 19. CMS
 [+] 20. Extrax Email
 [+] 21. WPShellUpload
 [+] 22. JaguarV3
 [+] 23. instagram Cracker
 [+] 24. Raiz0WorM
 [+] 25. More Last Updated!!!
 
			                  """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)


logo()


choice=raw_input(' \n\033[32m[!]\033[32m[+] Enter Number : ')
if choice=='1':
  t=raw_input('\033[34m [+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/UnitYoung && chmod +x unit.py && python unit.py")
   if system() == 'Windows':
    os.system('cd All/UnitYoung && unit.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='2':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan  ==> list.txt [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/Lar && chmod +x lar.py && lar.py")
   if system() == 'Windows':
    os.system('cd All/Lar && lar.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='3':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan  ==> list.txt [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/Dork && chmod +x dorkmaker.py && dorkmaker.py")
   if system() == 'Windows':
    os.system('cd All/Dork && dorkmaker.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='4':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan  ==> list.txt  [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/Dork && chmod +x dorkscanner.py && dorkscanner.py")
   if system() == 'Windows':
    os.system('cd All/Dork && dorkscanner.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='5':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan ==> list.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/Anon && chmod +x Shellv4.py && Shellv4.py")
   if system() == 'Windows':
    os.system('cd All/Anon && Shellv4.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='6':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/Smtp && chmod +x smtp.py && python smtp.py")
   if system() == 'Windows':
    os.system('cd All/Smtp && smtp.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='7':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/kil3rDz && chmod +x kil3r.py && python kil3r.py")
   if system() == 'Windows':
    os.system('cd All/kil3rDz && kil3r.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='8':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/ZhPost && chmod +x zh.py && python zh.py")
   if system() == 'Windows':
    os.system('cd All/ZhPost && zh.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='9':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/3xBeast && chmod +x default.py && python default.py")
   if system() == 'Windows':
    os.system('cd All/3xBeast && default.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='10':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/Ipdup && chmod +x ipgrab.py && python ipgrab.py")
   if system() == 'Windows':
    os.system('cd All/Ipdup && ipgrab.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='11':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/Ipdup && chmod +x duplicate.py && python duplicate.py")
   if system() == 'Windows':
    os.system('cd All/Ipdup && duplicate.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='12':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/RevIp && chmod +x reverseip.py && python reverseip.py")
   if system() == 'Windows':
    os.system('cd All/RevIp && reverseip.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='13':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/BruteJoomla && chmod +x joomla.py && python joomla.py")
   if system() == 'Windows':
    os.system('cd All/BruteJoomla && joomla.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='14':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/OpcBrute && chmod +x opc.py && python opc.py")
   if system() == 'Windows':
    os.system('cd All/OpcBrute && opc.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='15':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/V4Jex && chmod +x JEx.py && python JEx.py")
   if system() == 'Windows':
    os.system('cd All/V4Jex && JEx.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='16':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/V5jex && chmod +x latest.py && python latest.py")
   if system() == 'Windows':
    os.system('cd All/V5jex && latest.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='17':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/ZOMBIEV12 && chmod +x V12.py && python V12.py")
   if system() == 'Windows':
    os.system('cd All/ZOMBIEV12 && V12.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='18':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/ZOMBIEV13 && chmod +x v13.py && python v13.py")
   if system() == 'Windows':
    os.system('cd All/ZOMBIEV13 && v13.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='19':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/Cms && chmod +x CMS.py && python CMS.py")
   if system() == 'Windows':
    os.system('cd All/Cms && CMS.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='20':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/ExtraxEmail && chmod +x extraxmail.py && python extraxmail.py")
   if system() == 'Windows':
    os.system('cd All/ExtraxEmail && extraxmail.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='21':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/WPShellUpload && chmod +x auto-upload.py && python auto-upload.py")
   if system() == 'Windows':
    os.system('cd All/WPShellUpload && auto-upload.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='22':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/JaguarV3 && chmod +x end.py && python end.py")
   if system() == 'Windows':
    os.system('cd All/JaguarV3 && end.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='23':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/instagramCracker && chmod +x instagram.py && python instagram.py")
   if system() == 'Windows':
    os.system('cd All/instagramCracker && instagram.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='24':
  t=raw_input(' \033[34m[+] Buka Dan Jalankan [y/n] ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd All/Raiz0WorM && chmod +x private.py && python private.py")
   if system() == 'Windows':
    os.system('cd All/Raiz0WorM && private.py')
   else:
    print('\033[31mError Anjing !!!')
  elif t=='n':
   main()
  else :
   print('\033[31mError Anjing !!!')
if choice=='25':
  t=raw_input(' \033[31m[+] No Updates?, Contact Owner !!! ')