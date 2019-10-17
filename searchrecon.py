#!/usr/bin/env python

import sys
sys.path.append('./library')

from selenium import webdriver
from pyvirtualdisplay import Display
import os
import time
import pyfiglet
from termcolor import colored
import requests

info = """
            Author: Johan Du
            Date Created: 10/11/2019
            Date Update: 10//11/2019
            Description: Search recon information
"""

def menu():
    print """
    1.  Search directory path of arescode result (http-https)
    2.  Search redirect for javascript and redirect code (http-https)
    """
    return raw_input('[+] Choosen: ')

def check_code(resCode):
    resCode = int(resCode)
    if resCode >= 100 and resCode < 200:
        return '1xx'
    elif resCode >= 200 and resCode < 300:
        return '2xx'
    elif resCode >= 400 and resCode < 500:
        return '4xx'
    elif resCode >= 500:
        return '5xx'
    

def searchArescode(domain):

    # Checking for http
    try:
        url = 'http://' + domain
        #print '[-] Checking http schema'
        #print colored('Original: ', 'yellow') + url
        res_http = requests.get(url)
        #check_url = res_http.request.url.strip('/')
        #if not url == check_url:
            #print colored('Redirect: ', 'yellow') + res_http.request.url
        if not res_http.history:
            print colored('[*] Search for http:', 'yellow') + colored(' <arescode_result_http>/' + check_code(res_http.status_code) + '/' + str(res_http.status_code) + '/' + domain, 'blue')
        else:
            print colored('[*] Search for http:', 'yellow') + colored(' <arescode_result_http>/' + '3xx/' + domain, 'blue')
         
    except Exception as error:
        print colored('[*] Search for http:', 'yellow') + colored(' <arescode_result_http>/' + 'error/' + domain, 'blue')
        print colored('[-] Error for http: ', 'yellow') + colored(error, 'red')

    print '\n'
    
    # Checking for https
    try:
        url = 'https://' + domain
        #print '[-] Checking https schema'
        #print colored('Original: ', 'yellow') + url
        res_https = requests.get(url)
        #check_url = res_https.request.url.strip('/')
        #if not url == check_url:
            #print colored('Redirect: ', 'yellow') + res_https.request.url
        if not res_https.history:
            print colored('[*] Search for https:', 'yellow') + colored(' <arescode_result_https>/' + check_code(res_https.status_code) + '/' + str(res_https.status_code) + '/' + domain, 'blue')
        else:
            print colored('[*] Search for https:', 'yellow') + colored(' <arescode_result_https>/' + '3xx/' + domain, 'blue')

    except Exception as error:
        print colored('[*] Search for https:', 'yellow') + colored(' <arescode_result_https>/' + 'error/' + domain, 'blue')
        print colored('[+] Error for https: ', 'yellow') + colored(error, 'red')

def searchRedirect(domain):
    display = Display(visible=0)
    display.start()

    # checking for http
    #print "Checking http"
    url_http = 'http://' + domain

    #print "[!] Checking redirect header"
    res_http = requests.get(url_http)
    if res_http.history:
        print colored('[*] Search for http of redirect code: ', 'yellow') + 'Yes'
        print colored('Original: ', 'yellow') + url_http
        print colored('Redirect: ', 'yellow') + res_http.request.url
    else:
        print colored('[+] Search for http of redirect code: ', 'yellow') + 'No'
        print colored('Original: ', 'yellow') + url_http
    
    #print "[!] Checking redirect javascript"
    driver = webdriver.Firefox()
    driver.get(url_http)
    try:
        alert = driver.switch_to_alert()
        alert.dismiss()
    except:
        pass
    time.sleep(3)
    if res_http.request.url != driver.current_url:
        print colored('[*] Search for http of javascript redirect: ', 'yellow') + 'Yes'
        print colored('Original: ', 'yellow') + url_http
        print colored('Redirect: ', 'yellow') + driver.current_url
    else:
        print colored('[*] Search for http of javascript redirect : ', 'yellow') + 'No'
        print colored('Original: ', 'yellow') + url_http
    driver.close()

    print "\n"
    # checking for https
    #print "Checking https"
    url_https = 'https://' + domain

    #print "[!] Checking redirect header"
    res_https = requests.get(url_https)
    if res_https.history:
        print colored('[+] Search for https of redirect cocde : ', 'yellow') + 'Yes'
        print colored('Original: ', 'yellow') + url_https
        print colored('Redirect: ', 'yellow') + res_https.request.url

    else:
        print colored('[+] Search for https of redirect code: ', 'yellow') + 'No'
        print colored('Original: ', 'yellow') + url_https

    #print "[!] Checking redirect javascript"
    driver = webdriver.Firefox()
    driver.get(url_https)
    try:
        alert = driver.switch_to_alert()
        alert.dismiss()
    except:
        pass
    time.sleep(3)
    if res_https.request.url != driver.current_url:
        print colored('[+] Search for https of javascript redirect: ', 'yellow') + 'Yes'
        print colored('Original: ', 'yellow') + url_https
        print colored('Redirect: ', 'yellow') + driver.current_url
    else:
        print colored('[+] Search for https of javascript redirect: ', 'yellow') + 'No'
        print colored('Original: ', 'yellow') + url_https
    driver.close()

    display.stop()

def main():
    
    while True:
        os.system('clear')

        ascii_banner = pyfiglet.figlet_format("Searchrecon")
        print ascii_banner
        print colored(info, 'yellow')
    
        choosen = menu()
    
        if choosen == '1':
            domain = raw_input('[+] Enter domain: ')
            print "\n"
            searchArescode(domain)
            return
        elif choosen == '2':
            domain = raw_input('[+] Enter domain: ')
            print "\n"
            searchRedirect(domain)
            return 
        else:
            continue

if __name__ == '__main__':
    main()
