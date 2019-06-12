import gym
import numpy as np
from gym import spaces


TRUMP_AUTO = 'TRUMP_AUTO'
TRUMP_PLAYER = 'TRUMP_PLAYER'

RULE_BIGGER_CARD = 'RULE_BIGGER_CARD'
RULE_BIDDING_OPEN = 'RULE_BIDDING_OPEN'

class BatakEnv:
  def __init__(self, bidding=False, trump=TRUMP_AUTO, rules=[], deck_size=52):
    self.bidding = bidding
    self.trump = trump
    self.rules = rules
    self.deck_size = deck_size * 4 // 4
