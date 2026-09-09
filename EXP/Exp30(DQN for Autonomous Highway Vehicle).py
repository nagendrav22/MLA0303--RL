import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

states=5; actions=3
model=Sequential([Dense(32,activation='relu',input_shape=(states,)),
                  Dense(32,activation='relu'),Dense(actions)])
model.compile(optimizer='adam',loss='mse')

X=np.eye(states)
Y=np.zeros((states,actions))
for s in range(states):
    Y[s,min(2,s%3)]=10 if s==4 else 1
model.fit(X,Y,epochs=100,verbose=0)

print("Predicted action values:")
print(np.round(model.predict(X,verbose=0),2))

