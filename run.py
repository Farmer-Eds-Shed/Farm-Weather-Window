import requests
import os
import json
import time
from colorama import init as colorama_init
from colorama import Fore
from colorama import Back
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
    """Print set location screen"""
    while (True):
        clean()
        print(Fore.GREEN)
        tprint('~~~~Farm~~~~~~~~~~~', font="tarty3")
        tprint('~~~~~~~Weather~~~~~', font="tarty3")
        tprint('~~~~~~~~~~~~~Window', font="tarty3")
        print(Style.RESET_ALL)
        print("")
        town = input('Enter town name. (eg. Dublin) ')
        cc = input('Enter country code. (eg. ie) ')
        try:
            owm_location(town, cc)
            if town and cc != '':
                break
            else:
                print("")
                print(
                    Fore.RED +
                    "Town or Country cannot be blank."
                    + Style.RESET_ALL
                    )
                time.sleep(2)
        except IndexError:
            print("")
            print(
                Fore.RED +
                "location not found, Please try again."
                + Style.RESET_ALL)
            time.sleep(2)
    return town


def print_menu():
    """Print the main Menu"""
    print(Fore.YELLOW)
    tprint('Farm Weather Window', font="straight")
    print(f'A dedicated forecast for farm activity.')
    print(Style.RESET_ALL)
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
    """7 day weather forecast"""
    clean()
    tprint('7 Day Forecast', font="straight")
    t = Texttable()
    t.set_cols_dtype(['t', 't', 't', 't', 't', 't', 't', 't'])
    print(Back.BLUE)
    t.add_rows([
        [''] + days(),
        ['Temp C'] + temp(),
        ['rain mm'] + rain(),
        ['cloud %'] + clouds(),
        ['Wind ms'] + wind(),
        ['UVI'] + uvi()
        ])
    print(t.draw())
    print(Style.RESET_ALL)
    input("Press Enter to continue...")


def silage():
    """Silage forecast function"""
    clean()
    print('The next available window to make silage is:')
    print('')
    window = []
    for i in range(5):
        # checking the conditions
        if (
            rain()[i] <= 0.3
            and rain()[i + 1] <= 0.3
            and rain()[i + 2] <= 0.3
        ):
            window.append(i)
    try:
        d = window[0]
        t = Texttable()
        t.set_cols_dtype(['t', 't', 't', 't'])
        print(Back.GREEN)
        t.add_rows([
            [''] + days()[d:d+3],
            ['Temp C'] + temp()[d:d+3],
            ['rain mm'] + rain()[d:d+3],
            ['cloud %'] + clouds()[d:d+3],
            ['Wind ms'] + wind()[d:d+3],
            ['UVI'] + uvi()[d:d+3]
            ])
        print(t.draw())
        print(Style.RESET_ALL)
    except IndexError:
        print(
            Fore.BLACK +
            Back.RED +
            "Sorry no window available to make silage this week" +
            Style.RESET_ALL
            )
    print('')
    input("Press Enter to continue...")


def hay():
    """Hay forecast function"""
    clean()
    print('The next available window to make hay is:')
    print('')
    window = []
    for i in range(3):
        # checking the conditions
        if (
            rain()[i] <= 0.1
            and rain()[i + 1] <= 0.1
            and rain()[i + 2] <= 0.1
            and rain()[i + 3] <= 0.1
            and rain()[i + 4] <= 0.1
        ):
            window.append(i)
    try:
        d = window[0]
        t = Texttable()
        t.set_cols_dtype(['t', 't', 't', 't', 't', 't'])
        print(Back.GREEN)
        t.add_rows([
            [''] + days()[d:d+5],
            ['Temp C'] + temp()[d:d+5],
            ['rain mm'] + rain()[d:d+5],
            ['cloud %'] + clouds()[d:d+5],
            ['Wind ms'] + wind()[d:d+5],
            ['UVI'] + uvi()[d:d+5]
            ])
        print(t.draw())
        print(Style.RESET_ALL)
    except IndexError:
        print(
            Fore.BLACK +
            Back.RED +
            "Sorry no window available to make hay this week" +
            Style.RESET_ALL
            )
    print('')
    input("Press Enter to continue...")


def slurry():
    """Slurry forecast function"""
    clean()
    print('The next available window to spread slurry is:')
    print('')
    window = []
    for i in range(6):
        # checking the conditions
        if (
            rain()[i] <= 0.5
            and rain()[i + 1] <= 2

        ):
            window.append(i)
    try:
        d = window[0]
        t = Texttable()
        t.set_cols_dtype(['t', 't', 't'])
        print(Back.GREEN)
        t.add_rows([
            [''] + days()[d:d+2],
            ['Temp C'] + temp()[d:d+2],
            ['rain mm'] + rain()[d:d+2],
            ['cloud %'] + clouds()[d:d+2],
            ['Wind ms'] + wind()[d:d+2],
            ['UVI'] + uvi()[d:d+2]
            ])
        print(t.draw())
        print(Style.RESET_ALL)
    except IndexError:
        print(
            Fore.BLACK +
            Back.RED +
            "Sorry no window available to spread slurry this week" +
            Style.RESET_ALL
            )
    print('')
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
            print(
                Fore.RED +
                'Invalid input.'
                + Style.RESET_ALL)
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
            print(
                Fore.RED +
                'Please enter a number between 1 and 7.'
                + Style.RESET_ALL
                )
            time.sleep(2)
