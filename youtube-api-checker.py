'''
Please use this script for educational purposes only. I am not responsible for any misuse of this script.

Description: This script checks if a YouTube API key is valid or not.

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
    api_key = '' or input("Enter your YouTube API key: ")
    if not api_key:
        print(CLIColors.FAIL + "API key cannot be empty" + CLIColors.ENDC)
        sys.exit()
    url = "https://www.googleapis.com/youtube/v3/channels?part=snippet&mine=true&key=" + api_key
    response = requests.get(url)
    if response.status_code == 200:
        print(CLIColors.OKGREEN + "API key is valid" + CLIColors.ENDC)
        print("Your YouTube channel ID is: " + response.json()['items'][0]['id'])
        print("Your YouTube channel name is: " + response.json()['items'][0]['snippet']['title'])
        print("Response: " + str(response.json()))
    else:
        print(CLIColors.FAIL + "API key is invalid" + CLIColors.ENDC)
    

if __name__ == "__main__":
    main()