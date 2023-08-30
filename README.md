# Farm Weather Window
Farm Weather Window is a forecast tool to predict windows in the coming week to perform specific farm tasks. Many farm tasks have specific weather requirements including wind, percipitation levels and cloudcover.

Live Site: [Farm Weather Window](https://farm-weather-window-7024a2604c2c.herokuapp.com/)

![Main Menu](docs/readme_imgs/main_menu.png)

## Features

### Title and Set Location scrren

On first loading of the program the user is prompted for a town name and country code.
This uses the Open Weather Map Geolocation API to determin latitude and longitude for the main Forecast API.
This screen can be re-called at any time from the main menu. 

![Set Location](docs/readme_imgs/set_location.png)

### Options menu

Once a location has been established the main menu loads, where the user can select the desired forecast.
They may also choose to refresh the weather data, change location or end the program.

![Main Menu](docs/readme_imgs/main_menu.png)

###  Weather Forecast

The Weather Forecast option loads a standard 7 day forecast.
The weather data is pulled from the Open Weather Map One Call API.

![Forecast](docs/readme_imgs/forecast.png)

### Silage Window

Silage making requires 3 days with low rainfall amounts.
If available the Silage Window option will show the next weather window to make silage.
Otherwise will state that there is no window available in the comming week.

![Silage Forecast](docs/readme_imgs/silage_forecast.png)

### Hay Window

Hay making requires 5 days with close to 0 rainfall and idealy should have bright days. 
If available the Hay Window option will show the next weather window to make hay.
An aditional warning that extra theading may be required is displayed if the days will be very overcast.
Otherwise will state that there is no window available in the comming week.

![Hay Forecast](docs/readme_imgs/hay_forecast.png)

### Slurry Window

Slurry Spreading requires low rainfall on day of spreading and a forecast for the following day without heavy rain.
If available the Slurry Window option will show the next weather window to spread slurry.
Otherwise will state that there is no window available in the comming week.

![Slurry Forecast](docs/readme_imgs/slurry_forecast.png)

### Spray Window

Spraying requires low rainfall and very little wind.
If available the Spray Window option will show the next weather window for spraying crops.
Otherwise will state that there is no window available in the comming week.

![Spray Forecast](docs/readme_imgs/spray_forecast.png)

### Future Features

This program works as a proof of concept but I have delibretly left out some features to simplify the demonstration.

- Seasons, you can't make hay in winter in Ireland, but additional variables like seasons or hours of day light would make demonstration of the app imposible outside of the summer months.
- Multiple overlapping windows per week are possible and are currently stored in a list but I've choosen not to display due to the limited space on an 80 X 24 charecter terminal but would make mor sense if this project were converted to a backend for a web app.

Some additional future features should also include.

- Farm specific weather warnings like blight and grass tetany.  
- Additional farming tasks.



## Data Model


## Testing

### PEP8 Testing


### Input Testing
All user inputs were tested thoroughly to ensure all input data is handled correctly and appropriate feedback is given to the user as follows:




### Other Testing

## Libraries and Technologies Used

### Python Libraries:



### Programs Used




## Known Bugs



## Fixed Bugs



## Deployment

The site was deployed via [Heroku](https://dashboard.heroku.com/apps), and the live link can be found here: 

Before deploying to Heroku pip3 freeze > requirements.txt was used to add all the dependencies required to the requirements.txt file.




## Credits 
### Resources Used


## Acknowledgments
