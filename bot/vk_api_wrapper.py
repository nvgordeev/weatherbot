from vk_api import VkApi
from vk_api.longpoll import VkLongPoll


class VkAPI:

    def __init__(self, token):
        self._api = VkApi(token=token)
        self._longpoll = VkLongPoll(self._api)

    def write_msg(self, user_id, s):
        self._api.method('messages.send', {'user_id': user_id, 'message': s})

    def get_incoming_events(self):
        return (e for e in self._longpoll.listen() if e.to_me)

