# -*- coding: utf-8 -*-

import urllib.request
import socket
import os
import curl
import time
import urllib.error
from colorama import Fore, Style, init
init()
print(f'{Fore.MAGENTA}     ===========================')
print(f'{Fore.CYAN}        || Создано MMFARSE ||')
print(f'{Fore.MAGENTA}     ===========================')
print(Style.RESET_ALL)

time.sleep(3)
def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'https': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('https://vk.com') 
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
       # print('Error code: ', e.code)
        return e.code
    except Exception as detail:
       # print("ERROR:", detail)
        return True
    return False

def main():
    delayz = int(input('Задержка?: '))
    print(Style.RESET_ALL)
    socket.setdefaulttimeout(delayz)
    prl = open('prlist.txt')
    proxyList = prl

    folder = os.path.dirname(os.path.abspath(__file__)) 
    filepath = os.path.join(folder, "valid_proxy.txt", "NO_valid_proxy.txt")
    f1 = open('NO_valid_proxy.txt', 'a')
    l1 = '# -*- coding: utf-8 -*- \n  \n  \nМожно продать школьныкам в качетве валида))))\n \n \n'
    f1.write(str(l1) + '\n')
    f1.close()

    for currentProxy in proxyList:
        if is_bad_proxy(currentProxy):
            print(time.strftime("%X", time.localtime()) + ' | ' + f"{Fore.RED}NO %s" % (currentProxy))
            print(Style.RESET_ALL)
            f2 = open('NO_valid_proxy.txt', 'a')
            f2.write(str(currentProxy) + '\n')
        else:
            print(time.strftime("%X", time.localtime()) + ' | ' + f"{Fore.GREEN}YES %s" % (currentProxy))
            print(Style.RESET_ALL)
            f = open('valid_proxy.txt', 'a')
            f.write(str(currentProxy) + '\n')

if __name__ == '__main__':
    main() 