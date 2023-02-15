'''
Please use this script for educational purposes only. I am not responsible for any misuse of this script.

Description: This script checks if your 2Factor.in Api key are valid or not.

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

def main():
    api_key = '' or input("Enter your Api Key: ")
    if not api_key:
        print(CLIColors.FAIL + "Api Key cannot be empty" + CLIColors.ENDC)
        sys.exit()
    
    url = f'https://2factor.in/API/V1/{api_key}/SMS/+12024463369/AUTOGEN/OTP1'
    response = requests.get(url)
    if response.status_code == 200:
        # print with colors
        print(CLIColors.OKGREEN + "Your Api Key is valid" + CLIColors.ENDC)
        result = response.json()
        print('Here is the complete response: ')
        print(result)
    else:
        print(CLIColors.FAIL + "Your Api Key is invalid" + CLIColors.ENDC)
        
if __name__ == '__main__':
    main()
    