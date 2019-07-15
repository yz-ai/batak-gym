from typing import List


class State:
    def __init__(self, hand: List[int], available_actions: List[int], history):
        self.hand = hand
        self.available_actions = available_actions
        self.history = history

    @property
    def vectorized_state(self) -> List[int]:
        raise NotImplementedError("Not implemented in Abstract Base class")
