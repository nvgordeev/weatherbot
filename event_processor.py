from vk_api.longpoll import VkEventType

from command_parser import CommandParser
from render import render


class EventProcessor:

    def __init__(self, vk, weather_provider):
        self.vk = vk
        self.incoming_events = vk.get_incoming_events()
        self.weather_provider = weather_provider
        self.parser = CommandParser([
            {
                'aliases': ['now', 'сейчас'],
                'description': "Выводит погоду в данный момент",
                'default_params': 'Кудымкар',
                'method': self.get_weather_now
            }
        ])

    def get_weather_now(self, city_name):
        raw = self.weather_provider.get_weather_by_city(city_name)
        main_data = raw.get('main')
        wind_data = raw.get('wind')
        if not main_data:
            return "Не удалось получить данные"
        params = {
            'city_name': raw.get('name'),
            'temp': main_data.get('temp'),
            'humidity': main_data.get('humidity'),
            'pressure': int(float(main_data.get('pressure')) / 1.33322),
            'wind_speed': wind_data.get('speed')
        }
        return render('weather.txt', params)

    def process_new_message(self, event):
        self.vk.write_msg(event.user_id, self.parser.parse_command(event.text))

    def process_events(self):
        for event in self.incoming_events:
            if event.type == VkEventType.MESSAGE_NEW:
                self.process_new_message(event)





