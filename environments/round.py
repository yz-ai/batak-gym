from collections import namedtuple

History = namedtuple("History", ("played_card", "target_user"))


class Round:
    def __init__(self, round_number: int, players):
        self.__number = round_number
        self.players = players

        self.current_player = 1
        self.trump_broken = False
        self.history = []
