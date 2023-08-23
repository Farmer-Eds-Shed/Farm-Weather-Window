import requests
import os
import json
import time


def owm_api():
    """ Open Weather Map API"""
    lat = 53.6471
    lon = -6.6967
    api_key = os.getenv('OWM_API_KEY')
    response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}")
    global data
    data = json.loads(response.text)


class forecast:
    """class to build forecast object"""
    def __init__(self, day):
        dt = data['daily'][day]['dt']
        self.day = time.strftime('%A', time.localtime(dt))
        self.rain = data['daily'][day]['rain']
        self.temp = data['daily'][day]['temp']['day']
        self.wind = data['daily'][day]['wind_speed']
        self.clouds = data['daily'][day]['clouds']
        self.uvi = data['daily'][day]['uvi']


def clean():
    """Clear the Screen"""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


def print_menu():
    """Print the main Menu"""
    print('Welcome to Farm Weather Window.')
    print('A dedicated forecast based on farm activity.')
    print('Please select the farm Weater forecast window to check:')
    print('')
    menu_options = {
        1: 'Weather Forecast',
        2: 'Silage Window',
        3: 'Hay Window',
        4: 'Slurry Window',
        5: 'Spray Window',
        6: 'Refresh Weather Data',
        7: 'Change Location',
        8: 'Exit',
    }
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def week_forecast():
    """Main forecast function"""
    clean()
    print(forecast(0).day)
    print(f'rain {forecast(0).rain}')
    print('Handle option \'Forecast\'')
    input("Press Enter to continue...")


def silage():
    """Silage forecast function"""
    clean()
    print('Handle option \'Silage\'')
    input("Press Enter to continue...")


def hay():
    """Hay forecast function"""
    clean()
    print('Handle option \'Hay\'')
    input("Press Enter to continue...")


def slurry():
    """Slurry forecast function"""
    clean()
    print('Handle option \'Slurry\'')
    input("Press Enter to continue...")


def spray():
    """Spray forecast function"""
    clean()
    print('Handle option \'Spray\'')
    input("Press Enter to continue...")


if __name__ == '__main__':
    while (True):
        owm_api()
        clean()
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            week_forecast()
        elif option == 2:
            silage()
        elif option == 3:
            hay()
        elif option == 4:
            slurry()
        elif option == 5:
            spray()
        elif option == 6:
            owm_api()
            print("Refreshing Weather Data")
            time.sleep(3)
        elif option == 8:
            print('End Program')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 8.')