import random

states=range(5); actions=[0,1] # 0=left, 1=right
goal=4
def step(s,a):
    ns=max(0,s-1) if a==0 else min(4,s+1)
    r=10 if ns==goal else -1
    return ns,r

def train(method,episodes=1000):
    Q={(s,a):0.0 for s in states for a in actions}
    alpha,gamma,eps=0.2,0.9,0.1
    for _ in range(episodes):
        s=0
        a=random.choice(actions) if random.random()<eps else max(actions,key=lambda x:Q[(s,x)])
        for _ in range(20):
            ns,r=step(s,a)
            na=random.choice(actions) if random.random()<eps else max(actions,key=lambda x:Q[(ns,x)])
            if method=='SARSA':
                target=r if ns==goal else r+gamma*Q[(ns,na)]
            else:
                target=r if ns==goal else r+gamma*max(Q[(ns,b)] for b in actions)
            Q[(s,a)]+=alpha*(target-Q[(s,a)])
            s,a=ns,na
            if s==goal: break
    return Q

for method in ['SARSA','Q-Learning']:
    Q=train(method)
    print(method,"best actions:",[max(actions,key=lambda a:Q[(s,a)]) for s in states])
