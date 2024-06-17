import os
from cryptography.fernet import Fernet


def generate_key():
    key=Fernet.generate_key()
    with open("secret.key","wb") as key_file:
        key_file.write(key)

def load_key():
    with open("secret.key","rb") as key_file:
        return key_file.read()
    
def read_man_pass():
    with open("manager_password.txt","rb") as p:
        set_password=cipher.decrypt(p.read()).decode()
    return set_password

if not os.path.exists("secret.key"):
    generate_key()

key=load_key()
cipher=Fernet(key)

if os.path.exists("manager_password.txt"):
    pass
else:
    with open("manager_password.txt",'wb') as f:
        set_password=input("Enter a password for your password manager:")
        f.write(cipher.encrypt(set_password.encode()))

option=int(input("Enter 1 to add a new password:\nEnter 2 to view existing passwords:\nEnter 3 to change manage password:"))
if(option==1):
    site=input("Enter site for which password is saved:")
    username=input("Enter username:")
    password=input("Enter your password:")
    with open("passwords.txt",'a') as f:
        f.writelines(f"{site}:{username}:{password}\n")
    print("Your password has been saved")
elif(option==2):
    password=input("Enter manager password:")
    set_password=read_man_pass()
    if password==set_password:
        print("OK")
        with open("passwords.txt",'r') as f:
            passwords=f.readlines()
            for line in passwords:
                site, username, password=line.strip().split(':')
                print(f"{site}:{username}:{password}")
    else:
        print("Wrong password")
elif(option==3):
    cur_pass=input("Enter current password:")
    set_password=read_man_pass()
    if cur_pass==set_password:
        new_pass=input("Enter new password:")
        with open("manager_password.txt",'wb') as f:
            f.write(cipher.encrypt(new_pass.encode()))
        print("Manager password has been changed")
    else:
        print("Current password is wrong")

        
    
