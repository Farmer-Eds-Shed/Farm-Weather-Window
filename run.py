import requests
import os
import json
import time
from texttable import Texttable


def owm_location(town, cc):
    """Open Weather Map Location API"""
    api_key = os.getenv('OWM_API_KEY')
    response = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={town},{cc},ireland&appid={api_key}")
    data = json.loads(response.text)
    global lat
    global lon
    lat = data[0]['lat']
    lon = data[0]['lon']


def owm_api():
    """ Open Weather Map API"""
    api_key = os.getenv('OWM_API_KEY')
    response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}")
    global data
    data = json.loads(response.text)


class forecast:
    """class to build forecast object"""
    def __init__(self, day):
        dt = data['daily'][day]['dt']
        self.day = time.strftime('%A', time.localtime(dt))
        try:
            self.rain = data['daily'][day]['rain']
        except KeyError:
            self.rain = 0
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


def print_menu(town):
    """Print the main Menu"""
    print('Welcome to Farm Weather Window.')
    print(f'A dedicated forecast for farm activity in {town}.')
    print('Please select the farm weather forecast window to check:')
    print('')
    menu_options = {
        1: 'Weather Forecast',
        2: 'Silage Window',
        3: 'Hay Window',
        4: 'Slurry Window',
        5: 'Spray Window',
        6: 'Refresh Weather Data',
        7: 'Exit',
    }
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def week_forecast():
    """Main forecast function"""
    clean()
    t = Texttable()
    t.add_rows([
        [
            '',
            'Today',
            'Tomorrow',
            forecast(2).day,
            forecast(3).day,
            forecast(4).day,
            forecast(5).day,
            forecast(6).day
            ],
        [
            'Rain mm',
            forecast(0).rain,
            forecast(1).rain,
            forecast(2).rain,
            forecast(3).rain,
            forecast(4).rain,
            forecast(5).rain,
            forecast(6).rain
            ],
        [
            'Cloud %',
            forecast(0).clouds,
            forecast(1).clouds,
            forecast(2).clouds,
            forecast(3).clouds,
            forecast(4).clouds,
            forecast(5).clouds,
            forecast(6).clouds
            ],
        [
            'Wind ms',
            forecast(0).wind,
            forecast(1).wind,
            forecast(2).wind,
            forecast(3).wind,
            forecast(4).wind,
            forecast(5).wind,
            forecast(7).wind
            ]
        ])
    print(t.draw())
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
        town = input('Enter town name. (eg. Dublin)')
        cc = input('Enter country code. (eg. ie)')
        try:
            owm_location(town, cc)
            if town and cc != '':
                break
            else:
                print("Town or Country cannot be blank")
        except IndexError:
            print("location not found")
    # Enter location for weather forecast.
    while (True):
        owm_api()
        clean()
        print_menu(town)
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
        elif option == 7:
            print('End Program')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 7.')