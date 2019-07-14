from collections import namedtuple
from typing import List

import numpy as np

from .player import Player

History = namedtuple("History", ("played_card", "target_user"))


class Round:
    # 0-12 SPADES (2-3-4-5-6-7-8-9-10-J-Q-K-A)
    # 13-25 CLUBS (2-3-4-5-6-7-8-9-10-J-Q-K-A)
    # 26-38 HEARTS (2-3-4-5-6-7-8-9-10-J-Q-K-A)
    # 39-51 DIAMONDS (2-3-4-5-6-7-8-9-10-J-Q-K-A)

    idx2card = {
        0: '2S', 1: '3S', 2: '4S', 3: '5S', 4: '6S', 5: '7S', 6: '8S', 7: '9S', 8: '10S', 9: 'JS', 10: 'QS', 11: 'KS',
        12: 'AS',
        13: '2C', 14: '3C', 15: '4C', 16: '5C', 17: '6C', 18: '7C', 19: '8C', 20: '9C', 21: '10C', 22: 'JC', 23: 'QC',
        24: 'KC', 25: 'AC',
        26: '2H', 27: '3H', 28: '4H', 29: '5H', 30: '6H', 31: '7H', 32: '8H', 33: '9H', 34: '10H', 35: 'JH', 36: 'QH',
        37: 'KH', 38: 'AH',
        39: '2D', 40: '3D', 41: '4D', 42: '5D', 43: '6D', 44: '7D', 45: '8D', 46: '9D', 47: '10D', 48: 'JD', 49: 'QD',
        50: 'KD', 51: 'AD'}

    card2idx = {card: idx for idx, card in idx2card.items()}
    suit_indices = {
        "S": list(range(0, 13)),
        "C": list(range(13, 26)),
        "H": list(range(26, 39)),
        "D": list(range(39, 52))}

    def __init__(self, round_number: int, players: List[Player]):
        self.__number = round_number
        self.players = players

        self.current_player = 1
        self.trump_broken = False
        self.history = []

    def deal_cards(self):
        shuffled_deck = np.random.permutation(52) + 1
        # hand out cards to each player
        self.players[0].hand = np.sort(shuffled_deck[0:13])
        self.players[1].hand = np.sort(shuffled_deck[13:26])
        self.players[2].hand = np.sort(shuffled_deck[26:39])
        self.players[3].hand = np.sort(shuffled_deck[39:52])
