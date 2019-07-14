from environments.environment import Environment
from environments.state import State


class SimpleEnv(Environment):

    def __init__(self):
        super().__init__()

    def step(self, action):
        pass

    def reset(self) -> State:
        return super().reset()
