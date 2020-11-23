#!/usr/bin/env python

import webbrowser
import os

def cls():
    os.system("clear")

def about():
    cls()
    url = "https://www.instagram.com/i.m.cbkali/"
    url1 = "https://thecyberagents.com/cbkali"
    url2 = "https://github.com/cb-kali"
    url3 = "https://hackingwithpythontools.blogspot.com/"
    
    
    print("""
    \n 1. Ingtagrame
    \n 2. The Cyber Agents
    \n 3. Github
    \n 4. Blog
    \n 0. All
    \n""")
    
    choose = int(input("\nChoose option: "))

    if choose == 1:
        webbrowser.open(url)
    elif choose == 2:
        webbrowser.open(url1)
    elif choose == 3:
        webbrowser.open(url2)
    elif choose == 4:
        webbrowser.open(url3)
    elif choose == 0:
        
        webbrowser.open(url3)
        webbrowser.open(url2)
        webbrowser.open(url1)
        webbrowser.open(url)
    else:
        print("Wronge Option")


def Ip():
    cls()
    ip = input("\nEnter IP addrest: ")

    print("""
    \n 1. IPinfo 
    \n 2. WhatmyIP
    \n 3. Whois
    \n 4. IP2Loaction
    \n 5. NetTool
    \n 6. g-force
    \n 0. All
    \n""")

    choose = int(input("\nChoose number: "))

    
    def ipinfo():
        url = "https://ipinfo.io/"
        webbrowser.open(url+ip)

    def WhatmyIP():
        url = "https://whatismyipaddress.com/ip/"
        webbrowser.open(url+ip)

    def whois():
        url = "https://whois.domaintools.com/"
        webbrowser.open(url+ip)

    def ip2location():
        url = "https://www.ip2location.com/demo/"
        webbrowser.open(url+ip)

    def nettool():
        url = "https://mxtoolbox.com/SuperTool.aspx?action=arin%3a"
        webbrowser.open(url+ip)

    def gforce():
        url = "https://www.g-force.ca/en/hosting/ip-whois?ip="
        webbrowser.open(url+ip)

    if choose == 1:
        ipinfo()

    elif choose == 2:
        WhatmyIP()

    elif choose == 3:
        whois()
    
    elif choose == 4:
        ip2location()

    elif choose == 5:
        nettool()
    
    elif choose == 6:
        gforce()
    
    elif choose == 0:
        ipinfo()
        WhatmyIP()
        whois()
        ip2location()
        nettool()
        gforce()
    else:
        print("wronge option")

def phone():
    cls()
    number = input("\nEnter a mobile number: ")

    print("""
    \n 1. sync.me logo
    \n 2. mobile number tracker
    \n 3. etrace
    \n 0. All
    \n""")

    def sy():
        url = "https://sync.me/search/?number="
        webbrowser.open(url+number)

    def mob():
        url = "http://www.mobilenumbertracker.com/"
        webbrowser.open(url)

    def et():
        url = "https://etrace.in/mobile-number-tracker/"
        webbrowser.open(url+number)

    Choose = int(input("\nChoose number: "))

    if Choose == 1:
        sy()
    elif Choose == 2:
        mob()
    elif Choose == 3:
        et()
    elif Choose == 0:
        sy()
        mob()
        et()
    else:
        print("Wronge option")

def Name():
    cls()

    name = input("\nEnter a full name: ")

    print("""
    \n 1. Facebook
    \n 2. Twitter
    \n 3. Tumblr
    \n 4. Instagram
    \n 5. GitHub
    \n 6. Myspace
    \n 0. All
    \n""")

    choose = int(input("\nChoose Number: "))
    
    def fb():
        url = "https://www.facebook.com/public/"
        webbrowser.open(url+name)


    def tw():
        url = "https://twitter.com/search?q="
        webbrowser.open(url+name)

    def tu():
        url = "https://www.tumblr.com/search/"
        webbrowser.open(url+name)

    def instagram():
        url = "https://www.instagram.com/"
        webbrowser.open(url+name)

    def git():
        url = "https://github.com/"
        webbrowser.open(url+name)

    def  myspace():
        url = "https://myspace.com/search?q="
        webbrowser.open(url+name)
    
    if choose == 1:
        fb()
    elif choose == 2:
        tw()
    elif choose == 3:
        tu()
    elif choose == 4:
        instagram()
    elif choose == 5:
        git()
    elif choose == 6:
        myspace()
    elif choose == 0:
        fb()
        tw()
        tu()
        instagram()
        git()
        myspace()
    else:
        print("Wronge option")


def Website():
    cls()
    print("""
    \n 1. Ping
    \n 2. Whois
    \n 3. WhoisLookup
    \n 0. All
    \n""")

    web = input("\nEnter website(exampel.com): ")

    def ping():
        url = "https://www.ultratools.com/tools/ping6"
        webbrowser.open(url)
    def whois():
        url = "https://who.is/whois/"
        webbrowser.open(url+web)
    def Whoislookup():
        url = "https://whois.domaintools.com/"
        webbrowser.open(url+web)

    choose = int(input("\nChoose option: "))

    if choose == 1:
        ping()
    elif choose == 2:
        whois()
    elif choose == 3:
        Whoislookup()
    elif choose == 0:
        ping()
        whois()
        Whoislookup()
    else:
        print("Wronge option")

def menu():
    cls()

    print("""
██╗███╗   ██╗███████╗ ██████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗     ██████╗  █████╗ ████████╗██╗  ██╗███████╗██████╗ ██╗███╗   ██╗ ██████╗ 
██║████╗  ██║██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║    ██╔════╝ ██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗██║████╗  ██║██╔════╝ 
██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██╔████╔██║███████║   ██║   ██║██║   ██║██╔██╗ ██║    ██║  ███╗███████║   ██║   ███████║█████╗  ██████╔╝██║██╔██╗ ██║██║  ███╗
██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║    ██║   ██║██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗██║██║╚██╗██║██║   ██║
██║██║ ╚████║██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║    ╚██████╔╝██║  ██║   ██║   ██║  ██║███████╗██║  ██║██║██║ ╚████║╚██████╔╝
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                                                                                    
\t cbkali
    """)

    print("""
    \n 1. IP
    \n 2. Phone Number
    \n 3. Name
    \n 4. Website
    \n 0. About me
    """)

    choose = int(input("Which process do you performe: "))

    if choose == 1:
        Ip()
    elif choose == 2:
        phone()
    elif choose == 3:
        Name()
    elif choose == 4:
        Website()
    elif choose == 0:
        about()
    else:
        print("Wrong option!!")
menu()
