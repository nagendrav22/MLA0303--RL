import math

grid_size=4
goal=(3,3)
states=[(r,c) for r in range(grid_size) for c in range(grid_size)]
V={s:0 for s in states}
actions=[(-1,0),(1,0),(0,-1),(0,1)]

for _ in range(50):
    new={}
    for s in states:
        if s==goal: new[s]=0; continue
        vals=[]
        for dr,dc in actions:
            ns=(s[0]+dr,s[1]+dc)
            if ns in V: vals.append(1+V[ns])
        new[s]=min(vals) if vals else math.inf
    V=new

s=(0,0); path=[s]
while s!=goal:
    s=min([(s[0]+dr,s[1]+dc) for dr,dc in actions if (s[0]+dr,s[1]+dc) in V],
          key=lambda x:V[x])
    path.append(s)
print("Optimal path:",path)
print("Minimum steps:",V[(0,0)])
