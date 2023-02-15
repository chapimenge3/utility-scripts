'''
Please use this script for educational purposes only. I am not responsible for any misuse of this script.

Description: This script checks if a Google Map API Key is valid or not.

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

def street_view(api_key):
    '''
    This functions checks for the street view api
    '''
    url = f"https://maps.googleapis.com/maps/api/streetview?size=600x300&location=40.720032,-73.988354&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        print(CLIColors.OKGREEN + "Your API Key is valid for Street View API" + CLIColors.ENDC)        
    else:
        print(CLIColors.FAIL + "Your API Key is invalid for Street View API" + CLIColors.ENDC)
    
    return

def static_maps(api_key):
    '''
    This functions checks for the static maps api
    '''
    url = f"https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        print(CLIColors.OKGREEN + "Your API Key is valid for Static Maps API" + CLIColors.ENDC)
    else:
        print(CLIColors.FAIL + "Your API Key is invalid for Static Maps API" + CLIColors.ENDC)

    return

def directions(api_key):
    '''
    This functions checks for the directions api
    '''
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood4&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        print(CLIColors.OKGREEN + "Your API Key is valid for Directions API" + CLIColors.ENDC)
    else:
        print(CLIColors.FAIL + "Your API Key is invalid for Directions API" + CLIColors.ENDC)
    
    return

def distance_matrix(api_key):
    '''
    This functions checks for the distance matrix api
    '''
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins=Seattle&destinations=San+Francisco&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        print(CLIColors.OKGREEN + "Your API Key is valid for Distance Matrix API" + CLIColors.ENDC)
    else:
        print(CLIColors.FAIL + "Your API Key is invalid for Distance Matrix API" + CLIColors.ENDC)
    
    return

def roads(api_key):
    '''
    This functions checks for the roads api
    '''
    url = f"https://roads.googleapis.com/v1/snapToRoads?path=-35.27801,149.12958|-35.28032,149.12907|-35.28099,149.12929|-35.28144,149.12984|-35.28194,149.13003|-35.28282,149.12956|-35.28302,149.12881|-35.28473,149.12836 &interpolate=true&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        print(CLIColors.OKGREEN + "Your API Key is valid for Roads API" + CLIColors.ENDC)
    else:
        print(CLIColors.FAIL + "Your API Key is invalid for Roads API" + CLIColors.ENDC)
    
    return

def routes(api_key):
    '''
    This functions checks for the routes api
    '''
    url = f"https://routes.googleapis.com/directions/v2:computeRoutes?key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        print(CLIColors.OKGREEN + "Your API Key is valid for Roads API" + CLIColors.ENDC)
    else:
        print(CLIColors.FAIL + "Your API Key is invalid for Roads API" + CLIColors.ENDC)
    
    return

def places(api_key):
    '''
    This functions checks for the places api
    '''
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=restaurant&name=harbour&key{api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        print(CLIColors.OKGREEN + "Your API Key is valid for Places API" + CLIColors.ENDC)
    else:
        print(CLIColors.FAIL + "Your API Key is invalid for Places API" + CLIColors.ENDC)
    
    return

def geocoding(api_key):
    '''
    This functions checks for the geocoding api
    '''
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        print(CLIColors.OKGREEN + "Your API Key is valid for Geocoding API" + CLIColors.ENDC)
    else:
        print(CLIColors.FAIL + "Your API Key is invalid for Geocoding API" + CLIColors.ENDC)
    
    return

def geolocation(api_key):
    '''
    This functions checks for the geolocation api
    '''
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        print(CLIColors.OKGREEN + "Your API Key is valid for Geolocation API" + CLIColors.ENDC)
    else:
        print(CLIColors.FAIL + "Your API Key is invalid for Geolocation API" + CLIColors.ENDC)
    
    return

def address_validation(api_key):
    '''
    This functions checks for the address validation api
    '''
    url = f"https://addressvalidation.googleapis.com/v1:validateAddress?key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        print(CLIColors.OKGREEN + "Your API Key is valid for Address Validation API" + CLIColors.ENDC)
    else:
        print(CLIColors.FAIL + "Your API Key is invalid for Address Validation API" + CLIColors.ENDC)
    
    return

def time_zones(api_key):
    '''
    This functions checks for the time zones api
    '''
    url = f"https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        print(CLIColors.OKGREEN + "Your API Key is valid for Time Zones API" + CLIColors.ENDC)
    else:
        print(CLIColors.FAIL + "Your API Key is invalid for Time Zones API" + CLIColors.ENDC)
    
    return


def main():
    map_key = '' or input("Enter your API Key: ")
    if map_key == '':
        print(CLIColors.FAIL + "You didn't enter any API Key" + CLIColors.ENDC)
        return

    # use threading and thread pool to speed up the process and set the max number of threads to 10
    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(directions, map_key)
        executor.submit(distance_matrix, map_key)
        executor.submit(roads, map_key)
        executor.submit(routes, map_key)
        executor.submit(places, map_key)
        executor.submit(geocoding, map_key)
        executor.submit(geolocation, map_key)
        executor.submit(address_validation, map_key)
        executor.submit(time_zones, map_key)

if __name__ == "__main__":
    main()