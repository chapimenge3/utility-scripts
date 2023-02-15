'''
Please use this script for educational purposes only. I am not responsible for any misuse of this script.

Description: This script checks if a MongoDB database credentials are valid or not.

Author: Chapi Menge
Contact:
    Twitter: @chapimenge3
    Instagram: @chapimenge3
    Telegram: @chapimenge
    LinkedIn: https://www.linkedin.com/in/chapimenge/
    Github: https://github.com/chapimenge3
'''
import sys
import subprocess
try:
    from pymongo import MongoClient
    
except Exception as e:
    if "No module named" in str(e) :
        print("Please install pymongo module using pip install pymongo")
        print('If you want me to install it for you, type yes or y')
        if input().lower() in ['yes', 'y']:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pymongo"])
            from pymongo import MongoClient
        else:
            sys.exit()
    else:
        print("Error: " + str(e))
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
    url = '' or input("Enter your MongoDB database Full Connection URL: ")
    if not url:
        print(CLIColors.FAIL + "URL cannot be empty" + CLIColors.ENDC)
        sys.exit()
    try:
        client = MongoClient(url, serverSelectionTimeoutMS=1000)
        info = client.server_info()
        print(CLIColors.OKGREEN + "Connection successful" + CLIColors.ENDC)
        print(CLIColors.OKGREEN + "Server Info: " + str(info) + CLIColors.ENDC)
    except Exception as e:
        print(CLIColors.FAIL + "Connection failed" + CLIColors.ENDC)
        print(CLIColors.FAIL + "Error: " + str(e) + CLIColors.ENDC)

if __name__ == '__main__':
    main()
    