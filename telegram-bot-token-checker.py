'''
Please use this script for educational purposes only. I am not responsible for any misuse of this script.

Description: This script checks if your Telegram API Key is valid or not.

Author: Chapi Menge
Contact:
    Twitter: @chapimenge3
    Instagram: @chapimenge3
    Telegram: @chapimenge
    LinkedIn: https://www.linkedin.com/in/chapimenge/
    Github: https://github.com/chapimenge3
'''

import os
import sys
try:
    import requests
except Exception as e:
    if "No module named" in str(e):
        print("Please install requests module using pip install requests")
        print('If you want me to install it for you, type yes or y')
        if input().lower() in ['yes', 'y']:
            os.system('pip install requests')
            import requests
        else:
            sys.exit()


class CLIColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def check_token(token):
    try:
        url = f'https://api.telegram.org/bot{token}/getMe'
        response = requests.get(url)
        if response.status_code == 200:
            print(CLIColors.OKGREEN + "API key is valid" + CLIColors.ENDC)
            print("Your Telegram username is: " + response.json()['result']['username'])
            print('Link to your Telegram profile: ' + f'https://t.me/{response.json()["result"]["username"]}')
            
    except print(0):
        pass

def main():
    token = '' or input('Enter your Telegram API Key: ')
    if not token:
        print(CLIColors.FAIL + "API key cannot be empty" + CLIColors.ENDC)
        sys.exit()
    
    check_token(token)
    

if __name__ == '__main__':
    main()
    
    