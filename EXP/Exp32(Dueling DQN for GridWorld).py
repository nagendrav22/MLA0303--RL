import numpy as np
from tensorflow.keras import Model
from tensorflow.keras.layers import Input,Dense,Lambda
import tensorflow as tf

inp=Input(shape=(16,))
x=Dense(64,activation='relu')(inp)
value=Dense(1)(x)
adv=Dense(4)(x)
q=Lambda(lambda z:z[0]+z[1]-tf.reduce_mean(z[1],axis=1,keepdims=True))([value,adv])
model=Model(inp,q); model.compile(optimizer='adam',loss='mse')

X=np.eye(16)
Y=np.random.rand(16,4)
model.fit(X,Y,epochs=50,verbose=0)
print("Dueling DQN model trained.")
print("Best actions:",np.argmax(model.predict(X,verbose=0),axis=1))

