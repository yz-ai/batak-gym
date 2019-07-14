"""RL environments for Card Games, using an API similar to OpenAI Gym."""

# -------------------------------------------------------------------------------
# Environment API
# -------------------------------------------------------------------------------

import random

from environments.game_state import GameState
from environments.state import State


class Environment:
    """Abstract Environment interface.
    All concrete implementations of an environments should derive from this
    interface and implement the method stubs.
    """
    game_state: GameState

    def __init__(self, player_count=4):
        self.player_count = player_count

    def reset(self) -> State:
        """
        Reset the environments
        """
        self.game_state = GameState(self.player_count)
        self.game_state.new_round(1)

        return State(self.game_state.players[0].hand, self.game_state.rounds[0].history)

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
