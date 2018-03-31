# -*- coding: utf-8 -*-
import re
from vk_api.longpoll import VkEventType


class EventProcessor:

    def __init__(self, vk, weather_provider):
        self.vk = vk
        self.incoming_events = vk.get_incoming_events()
        self.weather_provider = weather_provider
        self.commands = [
            {
                'name': 'help',
                'aliases': ['help', u'помощь'],
                'description': u"справка о командах",
                'method': self.get_help
            },
            {
                'name': 'now',
                'aliases': ['now', u'сейчас'],
                'description': u"Выводит погоду в данный момент",
                'method': self.get_weather_now
            }
        ]
        self.build_regexp()

    def get_weather_now(self):
        raw = self.weather_provider.get_weather_by_city('kudymkar')
        main_data = raw.get('main')
        wind_data = raw.get('wind')
        if not main_data:
            return u"Не удалось получить данные"
        res = u"""
            Сейчас в Кудымкаре
            Температура: %s
            Влажность воздуха: %s %%
            Атмосферное давление: %s
            Ветер: %s м/с
        """ % (main_data.get('temp'), main_data.get('humidity'), float(main_data.get('pressure')) / 1.33322, wind_data.get('speed'))
        return res

    def get_help(self):
        return "\n".join([", ".join([a for a in c['aliases']]) + ': ' + c['description'] for c in self.commands])

    def build_regexp(self):
        for command in self.commands:
            command.update({
                'regexp': "|".join(['(' + c + ')' for c in command['aliases']])
            })

    def parse_command(self, message):
        for command in self.commands:
            if re.match(command['regexp'], message.lower()):
                return command['method']()
        return u'Не могу понять :( используйте эти команды: \n' + self.get_help()

    def process_new_message(self, event):
        self.vk.write_msg(event.user_id, self.parse_command(event.text))

    def process_events(self):
        for event in self.incoming_events:
            if event.type == VkEventType.MESSAGE_NEW:
                self.process_new_message(event)





