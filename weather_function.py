

import requests
import json


class Weather:
    def __init__(self, location):
        self._location = location
        self.api = '9664eaa67153b698bb3ef8f0027a078f'

    def grab_temperature(self, search_bar, location_title, label, temp, weather_icon, gui):
        try:
            self.location_data = json.loads(requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={self._location}&APPID={self.api}').text)

            self.description = str(self.location_data['weather'][0]['description']).capitalize()
            self.temp = self.location_data['main']['temp']

            location_title.setText(str(self._location).capitalize())
            label.setText(f'{self.description}')

            temp.setText(f'{(int((self.temp - 273.15) * 9/5 + 32))}°F')
            temp.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                               "font: 87 90pt \"Arial Black\";")

            #img
            if 'clear' in self.description.lower():
                weather_icon.setPixmap(gui.QPixmap("icons/sunny.png"))
            elif 'rain' in self.description.lower():
                weather_icon.setPixmap(gui.QPixmap("icons/rain_icon.png"))
            elif 'cloud' in self.description.lower():
                weather_icon.setPixmap(gui.QPixmap("icons/cloud_icon.png"))
            elif 'snow' in self.description.lower():
                weather_icon.setPixmap(gui.QPixmap("icons/snow_icon.png"))

        except:
            search_bar.setText('')
            search_bar.setPlaceholderText('Wrong location')


