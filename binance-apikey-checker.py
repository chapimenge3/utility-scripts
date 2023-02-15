'''
Please use this script for educational purposes only. I am not responsible for any misuse of this script.

Description: This script checks if binance Api key are valid or not.

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

def check_binance_cred(api_key, secret_key, base_url):
    print(f"{CLIColors.OKBLUE}Checking Api key for {base_url}...{CLIColors.ENDC}")
    headers = {
        'X-MBX-APIKEY': api_key
    }
    params = {
        'timestamp': 0
    }
    try:
        response = requests.get(base_url + 'api/v3/account', headers=headers, params=params)
        if response.status_code == 200:
            print(f"{CLIColors.OKGREEN}Valid Api key{CLIColors.ENDC}")
        else:
            print(f"{CLIColors.FAIL}Invalid Api key{CLIColors.ENDC}")
    except Exception as e:
        print(f"{CLIColors.FAIL}Invalid Api key{CLIColors.ENDC}")
        print(e)

def main():
    api_key = '' or input("Enter your binance api key: ")
    if not api_key:
        print("Please enter a valid api key")
        sys.exit()
    secret_key = '' or input("Enter your binance secret key: ")
    if not secret_key:
        print("Please enter a valid secret key")
        sys.exit()
    
    base_url = 'https://api.binance.com/'
    check_binance_cred(api_key, secret_key, base_url)
    testnet_base_url = 'https://testnet.binance.vision/'
    check_binance_cred(api_key, secret_key, testnet_base_url)
    
    
if __name__ == '__main__':
    main()
    