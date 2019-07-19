import gym
import numpy as np
from gym import spaces


SPADES = 0
HEARTS = 1
CLUBS = 2
DIAMONDS = 3

PLAYER_COUNT = 4


class SimpleEnv:
    def __init__(self, set_size=13):
        self.set_size = set_size
        self.deck_size = self.set_size * PLAYER_COUNT
        self.deck = np.mgrid[0:4, 0:self.set_size].reshape(2, -1).T

    def step(self, action):
        # check if action is in available actions
        assert action in self.players[self.current_player]['available_actions']

        # append to current set
        if len(self.current_set['cards']) == 0:
            suit, value = action
            self.current_set['suit'] = suit

        self.current_set['cards'].append({
            'card': action,
            'player': self.current_player,
        })

        # remove from hand
        curr_player_hand = self.players[self.current_player]['hand']
        action_idx = np.where((curr_player_hand == action).all(axis=1))
        curr_player_hand = np.delete(curr_player_hand, action_idx, axis=0)
        self.players[self.current_player]['hand'] = curr_player_hand

        # check if decision is needed
        if len(self.current_set['cards']) == 4:
            # decide
            trump_present = False
            biggest = 0
            winner = 0
            suit = -1

            for curr in self.current_set['cards']:
                card = curr['card']
                player = curr['player']
                card_suit, card_value = card

                # set current suit
                if suit == -1:
                    suit = card_suit
                # check if trump present
                if card_suit == SPADES:
                    trump_present = True
                    biggest = 0
                # if trump present, other cards are not valuable
                if trump_present:
                    if card_suit == SPADES and card_value > biggest:
                        winner = player
                        biggest = card_value
                # if trump not present, only current suit is valuable
                else:
                    if card_suit == suit and card_value > biggest:
                        winner = player
                        biggest = card_value

            # assign winner to previous set
            self.current_set['winner'] = winner
            self.previous_set = np.copy(self.current_set)

            # initialize set
            self.current_set = {'cards': []}

        # pass to other player
        self.current_player = (self.current_player + 1) % PLAYER_COUNT

        # calculate available actionsfor next player
        current_player = self.players[self.current_player]
        player_hand = current_player['hand']
        avail_actions = np.empty((0, 2), dtype=int)

        # no cards present
        if len(self.current_set['cards']) == 0:
            avail_actions = np.copy(player_hand)
        else:
            # check if hand has suit
            for card in player_hand:
                suit, value = card
                card = card.reshape(1, -1)
                if suit == self.current_set['suit']:
                    avail_actions = np.append(avail_actions, card, axis=0)
            # no suit present go for trump
            if len(avail_actions) == 0:
                for card in player_hand:
                    suit, value = card
                    card = card.reshape(1, -1)
                    if suit == SPADES:
                        avail_actions = np.append(avail_actions, card, axis=0)
            # no trump every card playable
            if len(avail_actions) == 0:
                avail_actions = np.copy(player_hand)

        self.players[self.current_player] = current_player
        self.players[self.current_player]['hand'] = player_hand
        self.players[self.current_player]['available_actions'] = avail_actions

        return {
            'player': self.players[self.current_player],
            'current_set': self.current_set,
            'previous_set': self.previous_set,
        }

    def reset(self):
        # shuffle the deck
        np.random.shuffle(self.deck)

        # set players
        self.players = [
            {
                'index': idx // self.set_size,
                'hand': self.deck[idx:idx + self.set_size],
                'available_actions': self.deck[idx:idx + self.set_size],
            }
            for idx in np.arange(0, self.deck_size, self.set_size)
        ]

        # initialize current player and set
        self.current_player = np.random.randint(0, PLAYER_COUNT)
        self.current_set = {'cards': []}
        self.previous_set = []

        return {
            'player': self.players[self.current_player],
            'current_set': self.current_set,
            'previous_set': self.previous_set,
        }


env = SimpleEnv()

state = env.reset()
selected_idx = np.random.choice(len(state['player']['available_actions']))
action = state['player']['available_actions'][selected_idx]
print(state)
print(action)
state = env.step(action)
selected_idx = np.random.choice(len(state['player']['available_actions']))
action = state['player']['available_actions'][selected_idx]
print(state)
print(action)
state = env.step(action)
selected_idx = np.random.choice(len(state['player']['available_actions']))
action = state['player']['available_actions'][selected_idx]
print(state)
print(action)
state = env.step(action)
selected_idx = np.random.choice(len(state['player']['available_actions']))
action = state['player']['available_actions'][selected_idx]
print(state)
print(action)
state = env.step(action)
selected_idx = np.random.choice(len(state['player']['available_actions']))
action = state['player']['available_actions'][selected_idx]
print(state)
print(action)
state = env.step(action)
selected_idx = np.random.choice(len(state['player']['available_actions']))
action = state['player']['available_actions'][selected_idx]
print(state)
print(action)
state = env.step(action)
selected_idx = np.random.choice(len(state['player']['available_actions']))
action = state['player']['available_actions'][selected_idx]
print(state)
print(action)
state = env.step(action)
selected_idx = np.random.choice(len(state['player']['available_actions']))
action = state['player']['available_actions'][selected_idx]
print(state)
print(action)
state = env.step(action)
selected_idx = np.random.choice(len(state['player']['available_actions']))
action = state['player']['available_actions'][selected_idx]
print(state)
print(action)

