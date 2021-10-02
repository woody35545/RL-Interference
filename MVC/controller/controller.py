from environment.settings import setting
from environment import interference_agent, interference_environment
from MVC.view.console_view import *
from user_setting import *
import random

epsilone = EPSILONE
decaying = DECAYING
max_user_number = MAX_USER_NUMBER
max_frequency_number = setting.MAX_FREQUENCY_TYPE_NUMBER
max_episode_number = setting.DEFAULT_MAX_EPISODE_NUM
max_action_number = setting.MAX_FREQUENCY_TYPE_NUMBER
max_state_number = MAX_USER_NUMBER + 1
env = interference_environment.environment(max_user_number)
agent = interference_agent.agent(max_user_number, max_state_number, max_action_number)


def run():
    episode_number = 0
    for i in range(max_episode_number):
        current_state = env.reset()
        done = False
        rALL = 0
        try_number = 0
        decaying_epsilone()
        while not done:
            if get_epsilone() > random.random():
                action = agent.do_random_action()
            else:
                action = agent.do_argmax_action(current_state)
            next_state, reward, done = env.step(action)
            agent.update_Q(current_state, next_state, action, reward)
            rALL += reward
            current_state = next_state
            try_number += 1
            if done == True:
                show_results(episode_number, try_number, rALL)

                episode_number += 1


def decaying_epsilone():
    global epsilone
    if epsilone > 0.01:
        epsilone -= decaying


def get_epsilone():
    return epsilone


def show_results(episode_number, try_number, rALL):
    width_ = 17
    p(str("episode[" + str(episode_number) + "]").ljust(15))
    p(str("try:" + str(try_number)).ljust(8))
    p(str("reward:" + str(rALL)).ljust(14))
    pl(str("epsilone:" + str(round(get_epsilone(), 2))).ljust(width_))
