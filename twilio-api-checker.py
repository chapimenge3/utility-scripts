'''
Please use this script for educational purposes only. I am not responsible for any misuse of this script.

Description: This script checks if your Twilio Account SID and Auth Token are valid or not.

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
    if str(e) == "No module named requests":
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
    account_sid = '' or input("Enter your Account SID: ")
    if not account_sid:
        print(CLIColors.FAIL + "Account SID cannot be empty" + CLIColors.ENDC)
        sys.exit()
    auth_token = '' or input("Enter your Auth Token: ")
    if not auth_token:
        print(CLIColors.FAIL + "Auth Token cannot be empty" + CLIColors.ENDC)
        sys.exit()
    
    url = "https://api.twilio.com/2010-04-01/Accounts.json"
    response = requests.get(url, auth=(account_sid, auth_token))
    if response.status_code == 200:
        # print with colors
        print(CLIColors.OKGREEN + "Your Account SID and Auth Token are valid" + CLIColors.ENDC)
        result = response.json()
        print("Your Account SID belongs to: " + result['accounts'][0]['friendly_name'])
        print('Here is the complete response: ')
        print(result)
    else:
        print(CLIColors.FAIL + "Your Account SID and Auth Token are invalid" + CLIColors.ENDC)
        print("Status Code: " + str(response.status_code))
        print("Reason: " + response.reason)
        print("Here is the complete response: ")
        print(response.text)
        
if __name__ == '__main__':
    main()