import random

grid = [
    ['S',0,0,0],
    [0,1,1,0],
    [0,0,0,0],
    [0,0,0,'G']
]
start=(0,0); goal=(3,3)
Q={}
actions=[(-1,0),(1,0),(0,-1),(0,1)]

def valid(s):
    r,c=s
    return 0<=r<4 and 0<=c<4 and grid[r][c] != 1

for s in [(r,c) for r in range(4) for c in range(4) if valid((r,c))]:
    for a in range(4): Q[(s,a)]=0.0

alpha,gamma,eps=0.2,0.9,0.2
for _ in range(2000):
    s=start
    for _ in range(50):
        a=random.randrange(4) if random.random()<eps else max(range(4),key=lambda x:Q[(s,x)])
        dr,dc=actions[a]; ns=(s[0]+dr,s[1]+dc)
        if not valid(ns): ns=s
        reward=10 if ns==goal else -1
        target=reward if ns==goal else reward+gamma*max(Q[(ns,b)] for b in range(4))
        Q[(s,a)] += alpha*(target-Q[(s,a)])
        s=ns
        if s==goal: break

s=start; path=[s]
for _ in range(20):
    a=max(range(4),key=lambda x:Q[(s,x)])
    dr,dc=actions[a]; ns=(s[0]+dr,s[1]+dc)
    if not valid(ns): break
    path.append(ns); s=ns
    if s==goal: break
print("Learned path:",path)
