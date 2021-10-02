neg = -5
reward_table_loc0 = {0: 1, 1: 2, 2: 2, 3: 3}
reward_table_loc1 = {0: 1, 1: neg, 2: 2, 3: neg}
reward_table_loc2 = {0: 1, 1: 2, 2: neg, 3: neg}
reward_table_loc3 = {0: 2, 1: neg, 2: neg, 3: neg}
reward_table = [""] * 4

reward_table[0] = reward_table_loc0
reward_table[1] = reward_table_loc1
reward_table[2] = reward_table_loc2
reward_table[3] = reward_table_loc3
