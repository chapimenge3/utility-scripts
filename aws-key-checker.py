'''
Please use this script for educational purposes only. I am not responsible for any misuse of this script.

Description: This script checks if AWS Api key are valid or not.

Author: Chapi Menge
Contact:
    Twitter: @chapimenge3
    Instagram: @chapimenge3
    Telegram: @chapimenge
    LinkedIn: https://www.linkedin.com/in/chapimenge/
    Github: https://github.com/chapimenge3
'''
import sys
import os
try:
    import boto3
except Exception as e:
    if "No module named" in str(e):
        print("Please install boto3 module using pip install boto3")
        print('If you want me to install it for you, type yes or y')
        if input().lower() in ['yes', 'y']:
            os.system('pip install boto3')
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
    aws_access_key_id = '' or input('Enter your access key: ')
    if not aws_access_key_id:
        print(CLIColors.FAIL + 'Access key is required' + CLIColors.ENDC)
        sys.exit()
    aws_secret_access_key = '' or input('Enter your secret key: ')
    if not aws_secret_access_key:
        print(CLIColors.FAIL + 'Secret key is required' + CLIColors.ENDC)
        sys.exit()

    iam = boto3.client('iam', aws_access_key_id=aws_access_key_id,
                       aws_secret_access_key=aws_secret_access_key)

    # get user account details using the keys
    try:
        user = iam.get_user()
        print(CLIColors.OKGREEN + 'Valid keys' + CLIColors.ENDC)
        print('User: ', user['User']['UserName'])
        print('User ID: ', user['User']['UserId'])
        print('ARN: ', user['User']['Arn'])
    except Exception as e:
        if 'InvalidClientTokenId' in str(e):
            print(CLIColors.FAIL + 'Invalid keys' + CLIColors.ENDC)
        else:
            print(CLIColors.FAIL + 'Unknown error' + CLIColors.ENDC)
            print(e)


if __name__ == '__main__':
    main()
