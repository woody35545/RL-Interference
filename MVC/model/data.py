state_index_dictionary = {}
action_index_dictionary = {}
state_load = 0
action_load = 0


def get_state_index(_state):
    if not state_index_does_exist(_state):
        update_state_index_dictionray(_state)
    index_ = int(state_index_dictionary[int(_state)])
    return index_


def get_action_index(_action):
    if not action_index_does_exist(_action):
        update_action_index_dictionary(_action)
    index_ = int(action_index_dictionary[str(_action)])
    return index_


def get_state_by_index(_index):
    rev = get_state_index_dictionary_reversed()
    return rev.get(int(_index))


def get_action_by_index(_index):
    rev = get_action_index_dictionary_reversed()
    return rev.get(int(_index))


def action_load_up():
    global action_load
    action_load += 1


def state_load_up():
    global state_load
    state_load += 1


def state_index_does_exist(_state):
    if state_index_dictionary.get(int(_state)) == None:
        return False
    else:
        return True


def action_index_does_exist(_action):
    if action_index_dictionary.get(str(_action)) == None:
        return False
    else:
        return True


def update_state_index_dictionray(_state):
    state_index_dictionary[int(_state)] = int(state_load)
    state_load_up()


def update_action_index_dictionary(_action):
    action_index_dictionary[str(_action)] = int(action_load)
    action_load_up()


def get_state_index_dictionary_reversed():
    state_index_dictionary_rev = {v: k for k, v in state_index_dictionary.items()}
    return state_index_dictionary_rev


def get_action_index_dictionary_reversed():
    action_index_dictionary_rev = {v: k for k, v in action_index_dictionary.items()}
    return action_index_dictionary_rev


def deformatting_action(_action):
    res_frequency = [0] * len(_action)
    for i in range(len(_action)):
        res_frequency[i] = str(_action)[i]
    return res_frequency



def formmating_action(action_list):
    res_action = ""
    for i in range(len(action_list)):
        res_action += str(action_list[i])
    return res_action
