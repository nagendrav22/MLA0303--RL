# Simplified PPO-style lane decision simulation
import numpy as np

lanes=['left','middle','right']
policy=np.ones(3)/3
for _ in range(1000):
    a=np.random.choice(3,p=policy)
    reward=1.0 if a==1 else 0.2
    policy[a]+=0.01*reward
    policy=np.clip(policy,0,1); policy/=policy.sum()

print("PPO-style lane policy:",dict(zip(lanes,np.round(policy,3))))

