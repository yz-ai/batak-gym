class Agent(object):
    """Agent interface.
    All concrete implementations of an Agent should derive from this interface
    and implement the method stubs.
    ```python
    class MyAgent(Agent):
      ...
    agents = [MyAgent(config) for _ in range(players)]
    while not done:
      ...
      for agent_id, agent in enumerate(agents):
        action = agent.act(observation)
        if obs.current_player == agent_id:
          assert action is not None
        else
          assert action is None
      ...
    ```
    """

    def __init__(self, agent_id: int):
        r"""Initialize the agent.
        Args:
          config: dict, With parameters for the game. Config takes the following
            keys and values.
              - colors: int, Number of colors \in [2,5].
              - ranks: int, Number of ranks \in [2,5].
              - players: int, Number of players \in [2,5].
              - hand_size: int, Hand size \in [4,5].
              - max_information_tokens: int, Number of information tokens (>=0)
              - max_life_tokens: int, Number of life tokens (>=0)
              - seed: int, Random seed.
              - random_start_player: bool, Random start player.
          *args: Optional arguments
          **kwargs: Optional keyword arguments.
        Raises:
          AgentError: Custom exceptions.
        """
        self.id = agent_id

    def reset(self, config):
        r"""Reset the agent with a new config.
        Signals agent to reset and restart using a config dict.
        Args:
          config: dict, With parameters for the game. Config takes the following
            keys and values.
              - colors: int, Number of colors \in [2,5].
              - ranks: int, Number of ranks \in [2,5].
              - players: int, Number of players \in [2,5].
              - hand_size: int, Hand size \in [4,5].
              - max_information_tokens: int, Number of information tokens (>=0)
              - max_life_tokens: int, Number of life tokens (>=0)
              - seed: int, Random seed.
              - random_start_player: bool, Random start player.
        """
        raise NotImplementedError("Not implemeneted in abstract base class.")

    def act(self, observation):
        """Act based on an observation.
        Args:
          observation: dict, containing observation from the view of this agent.
            An example:
            {'current_player': 0,
             'current_player_offset': 1,
             'deck_size': 40,
             'discard_pile': [],
             'fireworks': {'B': 0,
                       'G': 0,
                       'R': 0,
                       'W': 0,
                       'Y': 0},
             'information_tokens': 8,
             'legal_moves': [],
             'life_tokens': 3,
             'observed_hands': [[{'color': None, 'rank': -1},
                             {'color': None, 'rank': -1},
                             {'color': None, 'rank': -1},
                             {'color': None, 'rank': -1},
                             {'color': None, 'rank': -1}],
                            [{'color': 'W', 'rank': 2},
                             {'color': 'Y', 'rank': 4},
                             {'color': 'Y', 'rank': 2},
                             {'color': 'G', 'rank': 0},
                             {'color': 'W', 'rank': 1}]],
             'num_players': 2}]}
        Returns:
          action: dict, mapping to a legal action taken by this agent. The following
            actions are supported:
              - { 'action_type': 'PLAY', 'card_index': int }
              - { 'action_type': 'DISCARD', 'card_index': int }
              - {
                  'action_type': 'REVEAL_COLOR',
                  'color': str,
                  'target_offset': int >=0
                }
              - {
                  'action_type': 'REVEAL_RANK',
                  'rank': str,
                  'target_offset': int >=0
                }
        """
        raise NotImplementedError("Not implemented in Abstract Base class")
