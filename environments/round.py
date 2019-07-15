from collections import namedtuple
from typing import List

import numpy as np

from .player import Player

History = namedtuple("History", ("played_card", "target_player"))


class Round:
    def __init__(self, round_number: int, players: List[Player]):
        self.__number = round_number
        self.players = players

        self.current_player = 1
        self.trump_broken = False
        self.history = []
        self.round_steps = 1

    def deal_cards(self):
        shuffled_deck = np.random.permutation(52) + 1
        # hand out cards to each player
        self.players[0].hand = np.sort(shuffled_deck[0:13])
        self.players[1].hand = np.sort(shuffled_deck[13:26])
        self.players[2].hand = np.sort(shuffled_deck[26:39])
        self.players[3].hand = np.sort(shuffled_deck[39:52])

    def new_action(self, action) -> bool:
        self.history.append(History(played_card=action, target_player=self.current_player))

        if self.current_player == 4:
            if self.round_steps == 13:
                return True
            else:
                self.round_steps += 1

        self.current_player += 1

        return False
