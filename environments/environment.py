"""RL environments for Card Games, using an API similar to OpenAI Gym."""

# -------------------------------------------------------------------------------
# Environment API
# -------------------------------------------------------------------------------

import random
import numpy as np


class Environment:
    """Abtract Environment interface.
    All concrete implementations of an environments should derive from this
    interface and implement the method stubs.
    """

    # 0-12 SPADES (2-3-4-5-6-7-8-9-10-J-Q-K-A)
    # 13-25 CLUBS (2-3-4-5-6-7-8-9-10-J-Q-K-A)
    # 26-38 HEARTS (2-3-4-5-6-7-8-9-10-J-Q-K-A)
    # 39-51 DIAMONDS (2-3-4-5-6-7-8-9-10-J-Q-K-A)

    idx2card = {
        0: '2S', 1: '3S', 2: '4S', 3: '5S', 4: '6S', 5: '7S', 6: '8S', 7: '9S', 8: '10S', 9: 'JS', 10: 'QS', 11: 'KS', 12: 'AS',
        13: '2C', 14: '3C', 15: '4C', 16: '5C', 17: '6C', 18: '7C', 19: '8C', 20: '9C', 21: '10C', 22: 'JC', 23: 'QC', 24: 'KC', 25: 'AC',
        26: '2H', 27: '3H', 28: '4H', 29: '5H', 30: '6H', 31: '7H', 32: '8H', 33: '9H', 34: '10H', 35: 'JH', 36: 'QH', 37: 'KH', 38: 'AH',
        39: '2D', 40: '3D', 41: '4D', 42: '5D', 43: '6D', 44: '7D', 45: '8D', 46: '9D', 47: '10D', 48: 'JD', 49: 'QD', 50: 'KD', 51: 'AD'}

    card2idx = {card: idx for idx, card in idx2card.items()}
    suit_indices = {"S": list(range(0, 13)), "C": list(range(13, 26)), "H": list(range(26, 39)),
                    "D": list(range(39, 52))}

    def _deal_cards(self):
        shuffled_deck = np.random.permutation(52) + 1
        # hand out cards to each player
        self.currentHands = {
            1: np.sort(shuffled_deck[0:13]),
            2: np.sort(shuffled_deck[13:26]),
            3: np.sort(shuffled_deck[26:39]),
            4: np.sort(shuffled_deck[39:52])
        }

    def reset(self, config):
        """Reset the environments with a new config.
        Signals environments handlers to reset and restart the environments using
        a config dict.
        Args:
          config: dict, specifying the parameters of the environments to be
            generated.
        Returns:
          observation: A dict containing the full observation state.
        """

        self._deal_cards()

    def step(self, action):
        """Take one step in the game.
        Args:
          action: dict, mapping to an action taken by an agent.
        Returns:
          observation: dict, Containing full observation state.
          reward: float, Reward obtained from taking the action.
          done: bool, Whether the game is done.
          info: dict, Optional debugging information.
        Raises:
          AssertionError: When an illegal action is provided.
        """
        raise NotImplementedError("Not implemented in Abstract Base class")


# -------------------------------------------------------------------------------
# Hanabi Agent API
# -------------------------------------------------------------------------------



