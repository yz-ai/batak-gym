from environments import Environment


class SimpleEnv(Environment):

    def __init__(self):
        super().__init__()

    def step(self, action):
        pass

    def reset(self, config):
        super().reset(config)


