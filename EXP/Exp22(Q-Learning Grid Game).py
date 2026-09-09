import random

n=5
start=0; goal=4; ghost=2
Q=[[0.0,0.0] for _ in range(n)] # 0 left, 1 right

for _ in range(3000):
    s=start
    for _ in range(20):
        a=random.randrange(2) if random.random()<0.1 else max(range(2),key=lambda x:Q[s][x])
        ns=max(0,s-1) if a==0 else min(n-1,s+1)
        reward=10 if ns==goal else (-10 if ns==ghost else -1)
        target=reward if ns==goal else reward+0.9*max(Q[ns])
        Q[s][a]+=0.2*(target-Q[s][a])
        s=ns
        if s in [goal,ghost]: break

print("Q-table:")
for row in Q: print([round(x,2) for x in row])
