from typing import List

from environments.environment import Environment
from environments.state import State

from agents import RandomAgent


class SimpleEnv(Environment):
    agents: List[RandomAgent]

    def __init__(self):
        super().__init__()

    def step(self, action):
        current_player = self.game_state.current_player
        done = self.__make_action(action)

        if not done:
            done = self.__make_other_agents_actions(current_player)

        new_state = self.__get_new_state()

        return new_state, 0, done

    def reset(self) -> State:
        return super().reset()

    def make_env(self):
        self.agents = [RandomAgent(index + 1) for index in range(3)]

    def __make_action(self, action) -> bool:
        done = self.game_state.make_action(action)

        return done

    def __make_other_agents_actions(self, current_player) -> bool:
        index = 0
        done = False

        while not done and self.game_state.current_player != current_player:
            state = self.__get_new_state()
            action = self.agents[index].act(state)
            done = self.__make_action(action)

        return done

    def __get_new_state(self):
        player_info = self.game_state.players[self.game_state.current_player - 1]

        return State(player_info.hand, player_info.available_actions(), self.game_state.round_history)
