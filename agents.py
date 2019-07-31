import numpy as np
import random
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
from keras import losses

class RandomAgent():
    def __init__(self,player_number):   
        self.player_number = player_number
        self.available_actions = None

    def take_action(self,state):
        selected_idx = np.random.choice(len(state['player']['available_actions']))
        return state['player']['available_actions'][selected_idx]


class SimpleAgent():
    def __init__(self,player_number):   
        self.player_number = player_number
        self.available_actions = None
        self.reward = 0
        self.state_size = 8+26
        self.action_size = 13
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95    # discount rate
        self.epsilon = 0.1  # exploration rate
        self.learning_rate = 0.001
        self.epsilon_decrease = 0.002
        self.epsilon_decay = 0.02
        self.epsilon_min = 0.02
        self.model = None


    def take_action(self,state):
        selected_idx = np.random.choice(len(state['player']['available_actions']))
        return state['player']['available_actions'][selected_idx]
    
    def take_reward(self,reward):
        self.reward = reward

    def _build_model(self):
        self.model = Sequential()
        self.model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        self.model.add(Dense(24, activation='relu'))
        self.model.add(Dense(self.action_size, activation='linear'))
        self.model.compile(loss=losses.mean_squared_error,
                           optimizer=optimizers.Adam(lr=self.learning_rate))

    def remember(self, state, action, reward):
        state = np.array([state])
        self.memory.append((state, action, reward))

    def select_action(self, state,state_p):
        available_act = state_p['player']['available_actions']
        state = np.array([state])  
        q_values_for_actions = self.model.predict(state)[0][:len(available_act)]

        a_probs = np.ones(len(q_values_for_actions), dtype=float) * self.epsilon / len(q_values_for_actions)
        best_action = np.argmax(q_values_for_actions)
        a_probs[best_action] += (1 - self.epsilon)
        action = np.random.choice(np.arange(len(a_probs)), p=a_probs)
        return action

    def learn_from_memory(self, batch_size):
        if len(self.memory)>batch_size:
            minibatch = random.sample(self.memory, batch_size)
            for state, action, reward in minibatch:
                target = reward

                predicted_q_values = self.model.predict(state)  # [[predicted_q_value_of_action_1,predicted_q_value_of_action_2]]

                q_values_for_training = predicted_q_values
                q_values_for_training[0][action] = target       # new action q values(for training)

                self.model.fit(state, q_values_for_training, epochs=1, verbose=0)  #trainig with new q values
            if self.epsilon > self.epsilon_min:
                self.epsilon *= self.epsilon_decay
