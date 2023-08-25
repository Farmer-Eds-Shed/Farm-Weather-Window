import requests
import os
import json
import time
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from texttable import Texttable
from art import *

colorama_init()


def owm_location(town, cc):
    """Open Weather Map Location API"""
    api_key = os.getenv('OWM_API_KEY')
    response = requests.get(
        "https://api.openweathermap.org/geo/1.0/direct?"
        f"q={town},{cc},ireland&appid={api_key}"
        )
    data = json.loads(response.text)
    global lat
    global lon
    lat = data[0]['lat']
    lon = data[0]['lon']


def owm_api():
    """ Open Weather Map API"""
    api_key = os.getenv('OWM_API_KEY')
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall?"
        f"units=metric&lat={lat}&lon={lon}&appid={api_key}"
        )
    global data
    data = json.loads(response.text)


class forecast:
    """class to build forecast object"""
    def __init__(self, day):
        dt = data['daily'][day]['dt']
        self.day = time.strftime('%A', time.localtime(dt))
        try:
            self.rain = round(data['daily'][day]["rain"], 1)
        except KeyError:
            self.rain = 0
        self.temp = round(data['daily'][day]['temp']['day'], 1)
        self.wind = round(data['daily'][day]['wind_speed'], 1)
        self.clouds = data['daily'][day]['clouds']
        self.uvi = round(data['daily'][day]['uvi'], 1)


def clean():
    """Clear the Screen"""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


def set_location():
    while (True):
        clean()
        tprint('~~~~Farm~~~~~~~~~~~', font="tarty3")
        tprint('~~~~~~~Weather~~~~~', font="tarty3")
        tprint('~~~~~~~~~~~~~Window', font="tarty3")
        print("")
        print("")
        town = input('Enter town name. (eg. Dublin) ')
        cc = input('Enter country code. (eg. ie) ')
        try:
            owm_location(town, cc)
            if town and cc != '':
                break
            else:
                print("")
                print("Town or Country cannot be blank")
                time.sleep(2)
        except IndexError:
            print("")
            print("location not found, Please try again")
            time.sleep(2)
    return town


def print_menu():
    """Print the main Menu"""
    tprint('Farm Weather Window', font="straight")
    print(f'A dedicated forecast for farm activity.')
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


def days():
    """7 Days function"""
    days = ['Today', 'Tomorrow'] + [forecast(i).day for i in range(2, 7)]
    return days


def rain():
    """Rain 7 days"""
    rain = [forecast(i).rain for i in range(0, 7)]
    return rain


def clouds():
    """Clouds 7 days"""
    clouds = [forecast(i).clouds for i in range(0, 7)]
    return clouds


def wind():
    """Wind 7 days"""
    wind = [forecast(i).wind for i in range(0, 7)]
    return wind


def temp():
    """Temp 7 days"""
    temp = [forecast(i).temp for i in range(0, 7)]
    return temp


def uvi():
    """UVI 7 days """
    uvi = [forecast(i).uvi for i in range(0, 7)]
    return uvi


def week_forecast():
    """Main weather forecast"""
    clean()
    t = Texttable()
    t.set_cols_dtype(['t', 't', 't', 't', 't', 't', 't', 't'])
    t.add_rows([
        [''] + days(),
        ['Temp C'] + temp(),
        ['rain mm'] + rain(),
        ['cloud %'] + clouds(),
        ['Wind ms'] + wind(),
        ['UVI'] + uvi()
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
    set_location()
    owm_api()
    while (True):
        clean()
        print_menu()
        print("")
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
            time.sleep(2)
        elif option == 7:
            print('End Program')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 7.')
            time.sleep(2)
