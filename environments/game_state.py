from typing import List

from .player import Player
from .round import Round


class GameState:
    def __init__(self, min_win_count: int = 101):
        self.__min_win_count = min_win_count
        self.__round_count = 0
        self.rounds: List[Round] = []

        self.__init_players()
        self.__new_round()

    def __init_players(self, player_count: int = 4):
        self.players = [Player(index) for index in range(player_count)]

    def __new_round(self):
        self.__round_count += 1
        new_round = Round(self.__round_count, self.players)

        new_round.deal_cards()
        self.rounds.append(new_round)

        return False

    def make_action(self, action):
        done = False

        is_new_round = self.rounds[self.__round_count].new_action(action)

        if is_new_round:
            done = self.__new_round()

        return done

    @property
    def current_player(self) -> int:
        return self.rounds[self.__round_count].current_player

    @property
    def round_history(self) -> List[int]:
        return self.rounds[self.__round_count].history
