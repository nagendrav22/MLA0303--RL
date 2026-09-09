import numpy as np

actions=['forward','backward','left','right','stop']
theta=np.zeros(len(actions))
lr=0.05

for _ in range(2000):
    probs=np.exp(theta)/np.sum(np.exp(theta))
    a=np.random.choice(len(actions),p=probs)
    reward=1 if a==4 else (-0.1 if a in [0,1] else -0.2)
    theta[a]+=lr*reward*(1-probs[a])
    for i in range(len(actions)):
        if i!=a: theta[i]-=lr*reward*probs[i]

probs=np.exp(theta)/np.sum(np.exp(theta))
print(dict(zip(actions,np.round(probs,3))))
