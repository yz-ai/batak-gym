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
        current_player_hand = self.players[self.current_player]['hand']
        print(current_player_hand.shape)
        print(current_player_hand)
        print(tuple(action))
        print(current_player_hand == tuple(action))

        # check if decision is needed
        if len(self.current_set) == 4:
            # decide
            trump_present = False
            biggest = 0
            winner = 0
            suit = -1

            for curr in self.current_set['cards']:
                card, player = curr
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
                # if trump not present, only current suit is valuable
                else:
                    if card_suit == suit and card_value > biggest:
                        winner = player

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
        player_available_actions = current_player['available_actions']

        # no cards present
        if len(self.current_set['cards']) == 0:
            player_available_actions = np.copy(player_hand)
        else:
            # check if hand has suit
            for card in player_hand:
                suit, value = card
                if suit == self.current_set['suit']:
                    player_available_actions = np.append(player_available_actions, card)
            # no suit present go for trump
            if len(player_available_actions) == 0:
                for card in player_hand:
                    suit, value = card
                    if suit == SPADES:
                        player_available_actions.append(card)
            # no trump every card playable
            if len(player_available_actions) == 0:
                player_available_actions = np.copy(player_hand)

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
                'index': idx,
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
state = env.step(action)

print(state)