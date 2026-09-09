import gymnasium as gym
import numpy as np

env=gym.make("FrozenLake-v1",is_slippery=False)
Q=np.zeros((env.observation_space.n,env.action_space.n))
alpha,gamma,epsilon=0.8,0.95,0.1

for _ in range(5000):
    s,_=env.reset()
    done=False
    while not done:
        a=env.action_space.sample() if np.random.rand()<epsilon else np.argmax(Q[s])
        ns,r,terminated,truncated,_=env.step(a)
        done=terminated or truncated
        Q[s,a]+=alpha*(r+gamma*np.max(Q[ns])*(not done)-Q[s,a])
        s=ns

s,_=env.reset(); path=[s]
for _ in range(30):
    a=np.argmax(Q[s]); s,r,t,tr,_=env.step(a); path.append(s)
    if t or tr: break
print("Learned state sequence:",path)
env.close()

