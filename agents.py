import numpy as np

class RandomAgent():
    def __init__(self,player_number):   
        self.player_number = player_number
        self.available_actions = None

    def take_action(self,state):
        selected_idx = np.random.choice(len(state['player']['available_actions']))
        return state['player']['available_actions'][selected_idx]


class SimpleAgent():
    def __init__(self,player_number):   
        self.player_number = player_number
        self.available_actions = None

    def take_action(self,state):
        selected_idx = np.random.choice(len(state['player']['available_actions']))
        return state['player']['available_actions'][selected_idx]