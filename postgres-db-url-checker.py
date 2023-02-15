'''
Please use this script for educational purposes only. I am not responsible for any misuse of this script.

Description: This script checks if a PostgreSQL database credentials are valid or not.

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
    import psycopg2
except Exception as e:
    if "No module named" in str(e):
        print("Please install psycopg2 module using pip install psycopg2")
        print('If you want me to install it for you, type yes or y')
        if input().lower() in ['yes', 'y']:
            os.system('pip install psycopg2')
            import psycopg2
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
    url = '' or input("Enter your PostgreSQL database Full Connection URL or Host URL: ")
    port = ''
    user = ''
    password = ''
    database = ''
    if not url:
        print(CLIColors.FAIL + "URL cannot be empty" + CLIColors.ENDC)
        sys.exit()
    
    # check if the url is full connection string or host url
    if '@' in url:
        # full connection string
        port = url.split('@')[1].split(':')[1].split('/')[0]
        user = url.split('@')[0].split(':')[0]
        password = url.split('@')[0].split(':')[1]
        database = url.split('@')[1].split(':')[1].split('/')[1]
        url = url.split('@')[1].split(':')[0]
    else:
        user = '' or input("Enter your PostgreSQL database username: ")
        if not user:
            print(CLIColors.FAIL + "Username cannot be empty" + CLIColors.ENDC)
            sys.exit()
        password = '' or input("Enter your PostgreSQL database password: ")
        if not password:
            print(CLIColors.FAIL + "Password cannot be empty" + CLIColors.ENDC)
            sys.exit()
        database = '' or input("Enter your PostgreSQL database name: ")
        if not database:
            print(CLIColors.FAIL + "Database name cannot be empty" + CLIColors.ENDC)
            sys.exit()
        port = '' or input("Enter your PostgreSQL database port: ")
        if not port:
            print(CLIColors.FAIL + "Port cannot be empty" + CLIColors.ENDC)
            sys.exit()
        port = int(port)
        
        try:
            
            connection = psycopg2.connect(
                host = url,
                user = user,
                password = password,
                database = database,
                port = port
            )
            if connection.is_connected():
                print(CLIColors.OKGREEN + "Your PostgreSQL database credentials are valid" + CLIColors.ENDC)
                sys.exit()
            else:
                print(CLIColors.FAIL + "Your PostgreSQL database credentials are invalid" + CLIColors.ENDC)
                sys.exit()
        except Exception as e:
            print(CLIColors.FAIL + "Your PostgreSQL database credentials are invalid" + CLIColors.ENDC)
            print("Error: " + str(e))
            sys.exit()


if __name__ == '__main__':
    main()
