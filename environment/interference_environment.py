from environment.settings import setting
from environment import interference_reward, interference_table as interference
from MVC.model import data, object_users
import random


class environment():
    def __init__(self, _max_user_number):
        self.max_user_number = _max_user_number
        self.env_users = object_users.users(_max_user_number)
        self.env_current_state = -1
        self.env_users.init_random()
        self.set_current_state(self.get_total_interference())

    def reset(self):
        for i in range(self.max_user_number):
            generate_user_location = random.randrange(0, setting.MAX_USER_LOCATION_TYPE_NUMBER)
            generate_user_frequency = random.randrange(0, setting.MAX_FREQUENCY_TYPE_NUMBER)
            self.env_users.set_user(i, generate_user_location, generate_user_frequency)
        self.set_current_state(self.get_total_interference())
        return self.get_current_state()

    def get_next_state(self, _action):
        self.update_environment(_action)
        res_next_state = self.get_total_interference()
        self.set_current_state(res_next_state)
        return res_next_state

    def step(self, _action):
        res_next_state_ = self.get_next_state(_action)
        res_reward_ = self.reward(_action)
        res_is_done = self.is_done(_action)
        return res_next_state_, res_reward_, res_is_done

    def observe(self, _action):
        res_observed_state_ = None
        return res_observed_state_

    def render(self):
        None

    def reward(self, _action):
        res_reward = 0
        action_to_frequency_list = data.deformatting_action(_action)
        for i in range(self.max_user_number):
            reward_table_ = interference_reward.reward_table[self.env_users.get_user_location(i)]
            res_reward += reward_table_[int(action_to_frequency_list[i])]
        return res_reward

    def is_done(self, _action):
        if self.get_current_state() == setting.TERMITATE_STATE:
            return True
        else:
            return False

    def get_current_state(self):
        return int(self.env_current_state)

    def set_current_state(self, _state):
        self.env_current_state = int(_state)

    def get_total_interference(self):
        res_total_interference = 0
        for i in range(self.max_user_number):
            interference_table_ = interference.interference_table[self.env_users.get_user_location(i)]
            res_total_interference += interference_table_[self.env_users.get_user_frequency(i)]
        return int(res_total_interference)

    def update_environment(self, _action):
        action_to_frequency_list = data.deformatting_action(_action)
        for i in range((self.max_user_number)):
            self.env_users.set_user_frequency(i, action_to_frequency_list[i])
