import gym
import numpy as np
from gym import spaces
from agents import RandomAgent, SimpleAgent


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
        self.done = False

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
            self.previous_set = {**self.current_set}

            # initialize set
            self.current_set = {'cards': [], 'winner': -1}

            # winner is the player
            self.current_player = winner

            self.done = True
        else:
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

        # if cards are finished
        if len(player_hand) == 0 and not self.done:
            self.deal()
        else:
            curr_idx = self.current_player
            self.players[curr_idx] = current_player
            self.players[curr_idx]['hand'] = player_hand
            self.players[curr_idx]['available_actions'] = avail_actions


        #print(self.current_player)
        #print(self.previous_set)


        return {
            'current_player': self.current_player,
            'player': self.players[self.current_player],
            'current_set': self.current_set,
            'previous_set': self.previous_set,
        }, self.done
        
        """{
            'current_player': self.current_player,
            'reward': reward,
            'total_reward' : self.players[self.current_player]['total_win']
        }"""

    def reset(self):
        # initialize starting player and set
        self.starting_player = np.random.randint(0, PLAYER_COUNT)
        self.current_set = {'cards': [], 'winner': -1}
        self.previous_set = {**self.current_set}

        # deal
        self.deal()

        return {
            'player': self.players[self.current_player],
            'current_set': self.current_set,
            'previous_set': self.previous_set,
        }

    def deal(self):
        # shuffle the deck
        np.random.shuffle(self.deck)

        # set players
        self.players = [
            {
                'hand': self.deck[idx:idx + self.set_size],
                'available_actions': self.deck[idx:idx + self.set_size],
                'total_win' : 0
            }
            for idx in np.arange(0, self.deck_size, self.set_size)
        ]

        # change starting player
        self.starting_player = (self.starting_player + 1) % PLAYER_COUNT
        self.current_player = self.starting_player

    def give_winner(self):
        assert len(self.current_set['cards']) == 0, "This phase not over yet!"
        self.done = False
        return self.previous_set['winner']


env = SimpleEnv()

state = env.reset()
episode = 4

random_agents = []
for idx in range(3):
    random_agents.append(RandomAgent(idx))
my_agent = SimpleAgent(3)
my_agent._build_model()
state_rep = []
done = False
winner = 0
print('My agent number :',my_agent.player_number)
my_win = 0
for i in np.arange(env.set_size*4*500):
    selected_player = env.current_player



    if(selected_player == my_agent.player_number):
        state_rep = []
        for i in [x['card'] for x in state['current_set']['cards']]:
            for y in i :
                state_rep.append(y)
        for i in range((4-len(state['current_set']['cards']))*2):
            state_rep.append(14)
        for i in [i for i in state['player']['available_actions']]:
            for y in i :
                state_rep.append(y)
        for i in range((13-len(state['player']['available_actions']))*2):
            state_rep.append(14)

        action = my_agent.select_action(state_rep,state)
        state,done = env.step(state['player']['available_actions'][action])
    else:
        state,done = env.step(random_agents[selected_player].take_action(state))
    
    if (done):
        winner = env.give_winner()
        #print(winner)
        reward = 0
        if(winner == my_agent.player_number):
            my_win +=1
            reward = 1
        my_agent.remember(state_rep,action,reward)
        my_agent.learn_from_memory(1)
        state = env.reset()
        done = False
    

        
        

    #print(state['current_player'])
    #print(state['current_set'])
    #print(state['previous_set'])
    #print(reward)
    #print("----------------")
print(my_win)