# -*- coding: utf-8 -*-
import re


class CommandParser:

    def __init__(self, commands):
        self.commands = commands + [{
                'aliases': ['help', u'помощь'],
                'description': u"справка о командах",
                'method': self.get_help
            }]
        self.build_regexp()

    def get_help(self):
        return "\n".join([", ".join([a for a in c['aliases']]) + ': ' + c['description'] for c in self.commands])

    def build_regexp(self):
        for command in self.commands:
            command.update({
                'regexp': "|".join(['(' + c + ')' for c in command['aliases']])
            })

    def parse_command(self, text):
        for command in self.commands:
            if re.match(command['regexp'], text.lower()):
                return command['method']()
        return u'Не могу понять :( используйте эти команды: \n' + self.get_help()
