import requests
import os
import json


def owm_api():
    """ Open Weather Map API"""
    lat = 53.6471
    lon = -6.6967
    api_key = os.getenv('OWM_API_KEY')
    response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}")
    data = json.loads(response.text)
    print(data["daily"][1]["rain"])


def print_menu():
    """Print the main Menu"""
    print('Welcome to Farm Weather Window')
    print('A dedicated forecast based on farm activity')
    print('Please select the farm Weater forecast window to check')
    print('')
    menu_options = {
        1: 'Silage Window',
        2: 'Hay Window',
        3: 'Slurry Window',
        4: 'Spray Window',
        5: 'Exit',
    }
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def silage():
    """Silage forecast function"""
    print('Handle option \'Silage\'')


def hay():
    """Hay forecast function"""
    print('Handle option \'Hay\'')


def slurry():
    """Slurry forecast function"""
    print('Handle option \'Slurry\'')


def spray():
    """Spray forecast function"""
    print('Handle option \'Spray\'')


if __name__ == '__main__':
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            silage()
        elif option == 2:
            hay()
        elif option == 3:
            slurry()
        elif option == 4:
            spray()
        elif option == 5:
            print('End Program')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')