"""RL environments for Card Games, using an API similar to OpenAI Gym."""

# -------------------------------------------------------------------------------
# Environment API
# -------------------------------------------------------------------------------

from environments.game_state import GameState
from environments.state import State


class Environment:
    """Abstract Environment interface.
    All concrete implementations of an environments should derive from this
    interface and implement the method stubs.
    """
    game_state: GameState

    def reset(self) -> State:
        """
        Reset the environments
        """
        self.game_state = GameState()

        player = self.game_state.players[self.game_state.current_player - 1]

        return State(player.hand, player.available_actions(),
                     self.game_state.rounds[0].history)

    def step(self, action):
        """Take one step in the game.
        Args:
          action: an action taken by an agent.
        Returns:
          state: State object, Containing full observation state.
          reward: float, Reward obtained from taking the action.
          done: bool, Whether the game is done.
        Raises:
          AssertionError: When an illegal action is provided.
        """
        raise NotImplementedError("Not implemented in Abstract Base class")
