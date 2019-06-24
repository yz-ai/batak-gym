"""RL environments for Card Games, using an API similar to OpenAI Gym."""

from __future__ import absolute_import
from __future__ import division


# -------------------------------------------------------------------------------
# Environment API
# -------------------------------------------------------------------------------


class Environment:
    """Abtract Environment interface.
    All concrete implementations of an environments should derive from this
    interface and implement the method stubs.
    """

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
        raise NotImplementedError("Not implemented in Abstract Base class")

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



