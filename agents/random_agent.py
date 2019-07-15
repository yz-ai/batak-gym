"""Random Agent."""

import random
from agents import Agent
from environments.state import State


class RandomAgent(Agent):
    """Agent that takes random legal actions."""

    def reset(self, config):
        pass

    def __init__(self, agent_id: int):
        """Initialize the agent."""
        super().__init__(agent_id)

    def act(self, state: State) -> int:
        """Act based on an state"""
        return random.choice(state.available_actions)
