# -*- coding: utf-8 -*-
from event_processor import EventProcessor
from settings import TOKEN, OPENWEATHER_API_KEY
from bot.vk_api_wrapper import VkAPI
from weather_api import WeatherAPI


def main():
    EventProcessor(VkAPI(token=TOKEN), WeatherAPI(api_key=OPENWEATHER_API_KEY)).process_events()


if __name__ == '__main__':
    main()


