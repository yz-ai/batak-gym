from environments import Player


class GameState:
    def __init__(self, min_win_count=101, player_count=4):
        self.__min_win_count = min_win_count
        self.__round_count = 0

        self.__init_players(player_count)

    def __init_players(self, player_count):
        self.players = [Player(index) for index in range(player_count)]
