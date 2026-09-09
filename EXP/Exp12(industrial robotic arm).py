import numpy as np

actions=['left','right','up','down']
preferences=np.zeros(len(actions))
lr=0.1

for episode in range(1000):
    probs=np.exp(preferences)/np.sum(np.exp(preferences))
    a=np.random.choice(len(actions),p=probs)
    reward=1 if a in [1,2] else -0.2
    preferences[a]+=lr*reward

probs=np.exp(preferences)/np.sum(np.exp(preferences))
print("Learned action probabilities:")
for a,p in zip(actions,probs): print(a,round(float(p),3))
