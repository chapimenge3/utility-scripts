'''
Please use this script for educational purposes only. I am not responsible for any misuse of this script.

Description: This script checks if your TheMovieDB API Key is valid or not.

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
    api = '' or input("Enter your API Key: ")
    if not api:
        print(CLIColors.FAIL + "API Key cannot be empty" + CLIColors.ENDC)
        sys.exit()
    
    result = requests.get('https://api.themoviedb.org/3/configuration?api_key=' + api)
    if result.status_code == 200:
        # print with colors
        print(CLIColors.OKGREEN + "Your API Key is valid" + CLIColors.ENDC)
        print('Here is the complete response: ')
        print(result.json())
    else:
        print(CLIColors.FAIL + "Your API Key is invalid" + CLIColors.ENDC)
        print('Here is the complete response: ')
        print(result.json())

if __name__ == '__main__':
    main()
    