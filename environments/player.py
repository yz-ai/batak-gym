class Player:

    def __init__(self, player_id: int, game_score=0, round_score=0):
        self.__id = player_id
        self._hand = []
        self.game_score = game_score
        self.round_score = round_score

    @property
    def id(self):
        return self.__id

    @hand.setter
    def hand(self, new_hand):
        self._hand = new_hand

