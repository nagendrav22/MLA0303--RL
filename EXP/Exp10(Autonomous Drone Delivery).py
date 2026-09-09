import numpy as np
from collections import deque
import random
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

n_states=5; n_actions=2
model=Sequential([Dense(32,activation='relu',input_shape=(n_states,)),
                  Dense(32,activation='relu'),Dense(n_actions)])
model.compile(optimizer=Adam(0.001),loss='mse')

memory=deque(maxlen=5000); gamma=0.95
state=np.eye(n_states)[0]
for _ in range(1000):
    action=random.randrange(n_actions)
    next_i=min(4, np.argmax(state)+(1 if action else 0))
    next_state=np.eye(n_states)[next_i]
    reward=10 if next_i==4 else -1
    memory.append((state,action,reward,next_state,next_i==4))
    state=np.eye(n_states)[0] if next_i==4 else next_state

for _ in range(20):
    batch=random.sample(memory,min(32,len(memory)))
    X=[];Y=[]
    for s,a,r,ns,done in batch:
        target=model.predict(s.reshape(1,-1),verbose=0)[0]
        target[a]=r if done else r+gamma*np.max(model.predict(ns.reshape(1,-1),verbose=0)[0])
        X.append(s);Y.append(target)
    model.fit(np.array(X),np.array(Y),epochs=1,verbose=0)

print("DQN training completed.")
