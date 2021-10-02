from MVC.view.console_view import *
from environment.settings import setting
import random


class users:
    def __init__(self, _max_user_number):
        self.max_user_number = int(_max_user_number)
        self.user_location = [0] * self.max_user_number
        self.user_frequency = [0] * self.max_user_number

    def get_user_info(self, _index):
        pl(f"users[{_index}].location = {self.user_location[_index]}")
        pl(f"users[{_index}].frequency = {self.user_frequency[_index]}")

    def get_user_location(self, _index):
        return int(self.user_location[_index])

    def set_user_location(self, _index, _location):
        self.user_location[int(_index)] = _location

    def set_user_frequency(self, _index, _frequency):
        self.user_frequency[_index] = _frequency

    def get_user_frequency(self, _index):
        return int(self.user_frequency[int(_index)])

    def get_max_user_number(self):
        return int(self.max_user_number)

    def set_user(self, _index, _location, _frequency):
        self.set_user_location(_index, _location)
        self.set_user_frequency(_index, _frequency)

    def init_random(self):
        for i in range(self.max_user_number):
            random_location = random.randrange(0, setting.MAX_USER_LOCATION_TYPE_NUMBER)
            random_frequency = random.randrange(0, setting.MAX_FREQUENCY_TYPE_NUMBER)
            self.set_user(i, random_location, random_frequency)
