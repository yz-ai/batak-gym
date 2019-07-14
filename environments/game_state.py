from typing import List

from .player import Player
from .round import Round


class GameState:
    def __init__(self, player_count: int = 4, min_win_count: int = 101):
        self.__min_win_count = min_win_count
        self.__round_count = 0
        self.rounds: List[Round] = []

        self.__init_players(player_count)

    def __init_players(self, player_count):
        self.players = [Player(index) for index in range(player_count)]

    def new_round(self, round_number: int):
        new_round = Round(round_number, self.players)

        new_round.deal_cards()
        self.rounds.append(new_round)
