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
    response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?units=metric&lat={lat}&lon={lon}&appid={api_key}")
    global data
    data = json.loads(response.text)


class forecast:
    """class to build forecast object"""
    def __init__(self, day):
        dt = data['daily'][day]['dt']
        self.day = time.strftime('%A', time.localtime(dt))
        try:
            self.rain = round(data['daily'][day]['rain'], 1)
        except KeyError:
            self.rain = 0
        self.temp = round(data['daily'][day]['temp']['day'], 1)
        self.wind = round(data['daily'][day]['wind_speed'], 1)
        self.clouds = round(data['daily'][day]['clouds'], 1)
        self.uvi = round(data['daily'][day]['uvi'], 1)


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
    days = ['', 'Today', 'Tomorrow'] + [forecast(i).day for i in range(2, 7)]
    return days


def rain():
    """Rain 7 days"""
    rain = ['rain mm'] + [forecast(i).rain for i in range(0, 7)]
    return rain


def clouds():
    """Clouds 7 days"""
    clouds = ['cloud %'] + [forecast(i).clouds for i in range(0, 7)]
    return clouds


def wind():
    """Wind 7 days"""
    wind = ['Wind ms'] + [forecast(i).wind for i in range(0, 7)]
    return wind


def temp():
    """Temp 7 days"""
    temp = ['Temp C'] + [forecast(i).temp for i in range(0, 7)]
    return temp


def uvi():
    """UVI 7 days """
    uvi = ['UVI'] + [forecast(i).uvi for i in range(0, 7)]
    return uvi


def week_forecast():
    """Main weather forecast"""
    clean()
    t = Texttable()
    t.set_cols_dtype(['t', 't', 't', 't', 't', 't', 't', 't'])
    t.add_rows([
        days(),
        temp(),
        rain(),
        clouds(),
        wind(),
        uvi()
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
        clean()
        town = input('Enter town name. (eg. Dublin)')
        cc = input('Enter country code. (eg. ie)')
        try:
            owm_location(town, cc)
            if town and cc != '':
                break
            else:
                print("")
                print("Town or Country cannot be blank")
                time.sleep(1)
        except IndexError:
            print("")
            print("location not found, Please try again")
            time.sleep(1)
    # Enter location for weather forecast.
    owm_api()
    while (True):
        clean()
        print_menu(town)
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
            time.sleep(1)