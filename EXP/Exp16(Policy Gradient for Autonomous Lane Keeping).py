import numpy as np

lanes=['left','center','right']
theta=np.zeros(3)

for _ in range(1000):
    p=np.exp(theta)/np.sum(np.exp(theta))
    a=np.random.choice(3,p=p)
    reward=1 if a==1 else -0.5
    theta[a]+=0.05*reward

p=np.exp(theta)/np.sum(np.exp(theta))
print("Lane action probabilities:",dict(zip(lanes,np.round(p,3))))

