import numpy as np

states=5; actions=3
actor=np.zeros((states,actions)); critic=np.zeros(states)
lr=0.1; gamma=0.9

for _ in range(2000):
    s=np.random.randint(states)
    a=np.argmax(actor[s])
    ns=max(0,min(states-1,s+np.random.choice([-1,0,1])))
    reward=10 if ns==0 else -abs(ns)
    td=reward+gamma*critic[ns]-critic[s]
    critic[s]+=lr*td
    actor[s,a]+=lr*td

print("Learned elevator policy:",np.argmax(actor,axis=1))
