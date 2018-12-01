from keras.models import load_model, Sequential   
from keras.layers import Dense 
from keras.optimizers import Adam
import numpy as np
import random

class DQN:
    def __init__(self, input_size, output_size, memory_size, learning_rate, batch_size):
        self.input_size = input_size
        self.output_size = output_size
        self.memory_size = memory_size
        self.learning_rate = learning_rate
        self.epsilon = 1
        self.train_start = batch_size
        self.batch_size = batch_size

        self.model = self.make_model()
        self.target_model = self.make_model()

        self.update_target_model()
        self.memory=[]
        self.run_start = 1000

    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights())

    def make_model(self):
        model=Sequential()
        model.add(Dense(50, input_dim= self.input_size, activation= 'relu')) # input layer
        model.add(Dense(50, activation='relu')) # hidden layer
        model.add(Dense(50, activation='relu')) # hidden layer
        model.add(Dense(self.output_size)) # output layer
        model.compile(loss = "mean_squared_error", optimizer = Adam(lr = self.learning_rate))
        return model

    def get_action(self,state):
        if random.random()<self.epsilon:
            action = random.randrange(self.output_size)
            #print("r",end=" ")
            return action
        else:
            self.q_value = self.model.predict(state.reshape(1, len(state)))
            #print(self.q_value[0],np.argmax(self.q_value[0]),end=" ")
            return np.argmax(self.q_value[0])

    def getQvalue(self, reward, next_target, done):
        if done:
            return reward
        else:
            return reward + 0.99 * np.amax(next_target)

    def save_data(self, state, action, reward, new_state, done):
        if len(self.memory)>self.memory_size:
            self.memory.pop(0)
        self.memory.append((state, action, reward, new_state, done))

    def train_model(self):
        mini_batch = random.sample(self.memory, self.batch_size)
        X_batch = np.empty((0, self.input_size), dtype=np.float64)
        Y_batch = np.empty((0, self.output_size), dtype=np.float64)

        for i in range(self.batch_size):
            states = mini_batch[i][0]
            actions = mini_batch[i][1]
            rewards = mini_batch[i][2]
            next_states = mini_batch[i][3]
            dones = mini_batch[i][4]

            q_value = self.model.predict(states.reshape(1, len(states)))
            self.q_value = q_value

            next_target = self.target_model.predict(next_states.reshape(1, len(next_states)))
            next_q_value = self.getQvalue(rewards, next_target, dones)

            X_batch = np.append(X_batch, np.array([states.copy()]), axis=0)
            Y_sample = q_value.copy()
            Y_sample[0][actions] = next_q_value
            Y_batch = np.append(Y_batch, np.array([Y_sample[0]]), axis=0)

            if dones:
                X_batch = np.append(X_batch, np.array([next_states.copy()]), axis=0)
                Y_batch = np.append(Y_batch, np.array([[rewards] * self.output_size]), axis=0)

        self.model.fit(X_batch, Y_batch, batch_size=self.batch_size, epochs=1, verbose=0)

    def save_model(self):
        self.model.save('model.h5')

    def load_model(self):
        self.model = load_model('model.h5')
        self.target_model = load_model('model.h5')
