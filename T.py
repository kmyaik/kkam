import os
import random
import requests
from multiprocessing import Pool
print("Please make sure that you read README.md")
ID = input("Enter your Telegram id  : ")
TOKEN= input('Enter your telegram bot token  : ')
def check_username(username):
    response = requests.get(f"https://t.me/{username}").text
    if 'tgme_username_link' in response:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text=@{username}")
        print(f"\x1b[1;32mAvailable: {username}")
    else:
        print(f"\x1b[1;31mNOT Available: {username}")

if __name__ == '__main__':
    os.system('clear')
    MM = int(input('\x1b[1;31m [^]\x1b[1;36m AMOUNT OF USER :\x1b[1;37m'))
    os.system('clear')
    all_characters = '098_76_543_21AB_______CDEF_GHIKLMN_____________OPQSTVWSYZqwertyuioplkjhgfdsazxcvbnm_'
    username_length = 1

    with Pool() as pool:
        usernames = [''.join(random.choices(all_characters, k=username_length*6,)) for _ in range(MM)]
        pool.map(check_username, usernames)
