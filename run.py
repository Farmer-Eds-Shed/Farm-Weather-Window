"""Farm Weather Window."""
import requests
import os
import json
import time
from colorama import init as colorama_init
from colorama import Fore
from colorama import Back
from colorama import Style
from texttable import Texttable
from art import tprint


def owm_location(town, cc):
    """Open Weather Map Location API."""
    api_key = os.getenv('OWM_API_KEY')
    try:
        response = requests.get(
            "https://api.openweathermap.org/geo/1.0/direct?"
            f"q={town},{cc},ireland&appid={api_key}"
            )
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        raise SystemExit(response.text)
    except requests.exceptions.RequestException:
        raise SystemExit("Connection Error: please try again later.")
    data = json.loads(response.text)
    global lat
    global lon
    lat = data[0]['lat']
    lon = data[0]['lon']


def owm_api():
    """Open Weather Map API."""
    api_key = os.getenv('OWM_API_KEY')
    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/onecall?"
            f"units=metric&lat={lat}&lon={lon}&appid={api_key}"
            )
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        raise SystemExit(response.text)
    except requests.exceptions.RequestException:
        raise SystemExit("Connection Error: please try again later.")
    global data
    data = json.loads(response.text)


class Forecast:
    """class to build forecast object."""

    def __init__(self, day):
        """Map API variables."""
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
    """Clear the Screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


def set_location():
    """Print set location screen."""
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
    """Print the main Menu."""
    print(Fore.YELLOW)
    tprint('Farm Weather Window', font="straight")
    print('A dedicated forecast by farm activity.')
    print(Style.RESET_ALL)
    menu_options = {
        1: 'Weather Forecast',
        2: 'Silage Window',
        3: 'Hay Window',
        4: 'Slurry Window',
        5: 'Spray Window',
        6: 'Change Location',
        7: 'Refresh Weather Data',
        8: 'Exit',
    }
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def days():
    """7 Days function."""
    days = ['Today', 'Tomorrow'] + [Forecast(i).day for i in range(2, 7)]
    return days


def rain():
    """Rain 7 days."""
    rain = [Forecast(i).rain for i in range(0, 7)]
    return rain


def clouds():
    """Clouds 7 days."""
    clouds = [Forecast(i).clouds for i in range(0, 7)]
    return clouds


def wind():
    """Wind 7 days."""
    wind = [Forecast(i).wind for i in range(0, 7)]
    return wind


def temp():
    """Temp 7 days."""
    temp = [Forecast(i).temp for i in range(0, 7)]
    return temp


def uvi():
    """UVI 7 days."""
    uvi = [Forecast(i).uvi for i in range(0, 7)]
    return uvi


def table(window, num_days):
    """
    Print table for weather window.

    Takes 2 Parameters for Start of Window and Number of days.
    """
    t = Texttable()
    data_type = ['t']
    for _ in range(num_days):
        data_type.append('t')
    t.set_cols_dtype(data_type)  # format all cells as string
    t.add_rows([
        [''] + days()[window: window + num_days],
        ['Temp C'] + temp()[window: window + num_days],
        ['rain mm'] + rain()[window: window + num_days],
        ['cloud %'] + clouds()[window: window + num_days],
        ['Wind ms'] + wind()[window: window + num_days],
        ['UVI'] + uvi()[window: window + num_days]
        ])
    print(t.draw())
    print(Style.RESET_ALL)


def week_forecast():
    """7 day weather forecast."""
    clean()
    tprint('7 Day Forecast', font="straight")
    print(Back.BLUE)
    table(0, 7)
    print(Style.RESET_ALL)
    input("Press Enter to continue...")


def silage():
    """
    Silage forecast function.

    Prints table if there are 3 consecutive days.
    with less than 0.3mm of rain.
    """
    clean()
    print('The next available window to make silage is:')
    print('')
    windows = []
    for i in range(5):
        # checking the conditions
        if (
            rain()[i] <= 0.3
            and rain()[i + 1] <= 0.3
            and rain()[i + 2] <= 0.3
        ):
            windows.append(i)
    print(Back.GREEN)
    try:
        table(windows[0], 3)
    except IndexError:
        print(
            Back.RED +
            "Sorry no window available to make silage this week."
            )
    print(Style.RESET_ALL)
    input("Press Enter to continue...")


def hay():
    """
    Hay forecast function.

    Prints table if there are 5 dry consecutive days.
    Prints warning if weather is to be overcast.
    """
    clean()
    print('The next available window to make hay is:')
    print('')
    windows = []
    for i in range(3):
        # checking the conditions
        if (
            rain()[i] <= 0.1
            and rain()[i + 1] <= 0.1
            and rain()[i + 2] <= 0.1
            and rain()[i + 3] <= 0.1
            and rain()[i + 4] <= 0.1
        ):
            windows.append(i) 
    print(Back.GREEN)
    try:
        table(windows[0], 5)
        cloud = (
                int(clouds()[windows[0]]) +
                int(clouds()[windows[0] + 1]) +
                int(clouds()[windows[0] + 2]) +
                int(clouds()[windows[0] + 3]) +
                int(clouds()[windows[0] + 4])
            )
        if (cloud / 5 >= 50):
            print(
                Back.RED +
                "Warning: Overcast weather may require extra theading "
                "and / or time."
                )
    except IndexError:
        print(
            Back.RED +
            "Sorry no window available to make hay this week."
            )
    print(Style.RESET_ALL)
    input("Press Enter to continue...")


def slurry():
    """
    Slurry forecast function.

    Prints table if there is a day with less than 0.5mm of rain
    followed ba a day with less than 2mm.
    """
    clean()
    print('The next available window to spread slurry is:')
    print('')
    windows = []
    for i in range(6):
        # checking the conditions
        if (
            rain()[i] <= 0.5
            and rain()[i + 1] <= 2
        ):
            windows.append(i)
    print(Back.GREEN)
    try:
        table(windows[0], 2)
    except IndexError:
        print(
            Back.RED +
            "Sorry no window available to spread slurry this week."
            )
    print(Style.RESET_ALL)
    input("Press Enter to continue...")


def spray():
    """
    Spray forecast function.

    Prints table if there is a day with less than 0.5mm of rain
    and wind speed below 5 ms followed by a day with less than 2mm.
    """
    clean()
    print('The next available window to spray is:')
    print('')
    windows = []
    for i in range(6):
        # checking the conditions
        if (
            rain()[i] <= 0.5
            and rain()[i + 1] <= 2
            and wind()[i] <= 5
        ):
            windows.append(i)
    print(Back.GREEN)
    try:
        table(windows[0], 2)
    except IndexError:
        print(
            Back.RED +
            "Sorry no window available to spray this week."
            )
    print(Style.RESET_ALL)
    input("Press Enter to continue...")


if __name__ == '__main__':
    colorama_init()
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
            set_location()
            owm_api()
            print("Refreshing Weather Data")
            time.sleep(2)
        elif option == 7:
            owm_api()
            print("Refreshing Weather Data")
            time.sleep(2)
        elif option == 8:
            print('End Program')
            exit()
        else:
            print(
                Fore.RED +
                'Please enter a number between 1 and 8.'
                + Style.RESET_ALL
                )
            time.sleep(2)
