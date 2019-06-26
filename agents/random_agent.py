"""Random Agent."""

import random
from agents import Agent


class RandomAgent(Agent):
    """Agent that takes random legal actions."""

    def reset(self, config):
        pass

    def __init__(self, config, *args, **kwargs):
        """Initialize the agent."""
        super().__init__(config, *args, **kwargs)
        self.config = config

    def act(self, observation):
        """Act based on an observation."""
        if observation['current_player_offset'] == 0:
            return random.choice(observation['legal_moves'])
        else:
            return None
