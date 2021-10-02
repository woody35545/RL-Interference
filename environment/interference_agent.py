from environment.settings import setting
from MVC.model import data

import numpy as np
import random


class agent():
    def __init__(self, _max_user_number, _max_state_number, _max_action_number):
        self.max_user_number = _max_user_number
        self.Q_table_state_size = _max_state_number
        self.Q_table_action_size = _max_action_number ** _max_user_number
        self.Q_table = np.full((self.Q_table_state_size, self.Q_table_action_size), 0.)

    def do_random_action(self):
        frequency_list = [0] * self.max_user_number
        for i in range(self.max_user_number):
            frequency_list[i] = random.randrange(0, setting.MAX_FREQUENCY_TYPE_NUMBER)
        res_action = data.formmating_action(frequency_list)

        return res_action

    def do_argmax_action(self, _current_state):
        argmax_action_index = -1
        current_index = int(_current_state)
        temp = -1
        for i in range(self.Q_table_action_size):
            if temp < self.Q_table[current_index, i]:
                temp = self.Q_table[current_index, i]
                argmax_action_index = i
        res_action = (data.get_action_by_index(int(argmax_action_index)))
        if res_action == None or argmax_action_index == -1:
            res_action = self.do_random_action()
        else:
            res_action = str(data.get_action_by_index(int(argmax_action_index)))

        return str(res_action)

    def update_Q(self, current_state, next_state, action, reward):
        state_index = int(current_state)
        action_index = data.get_action_index(action)
        self.Q_table[state_index, action_index] = int(reward) + round(0.1 * self.get_maxQ(next_state), 2)
        return None

    def get_maxQ(self, _state):
        res_max_Q = 0
        for i in range(self.Q_table_action_size):
            if res_max_Q < self.Q_table[_state, i]:
                res_max_Q = self.Q_table[_state, i]
        return res_max_Q
