# Shortest-route policy using value iteration
states=['A','B','C','D','E']
graph={
'A':[('B',2),('C',5)],
'B':[('A',2),('D',2)],
'C':[('A',5),('D',1)],
'D':[('B',2),('C',1),('E',3)],
'E':[]
}
goal='E'
V={s:0 for s in states}
for _ in range(100):
    V={s:(0 if s==goal else min(c+V[n] for n,c in graph[s])) for s in states}

s='A'; path=[s]; cost=0
while s!=goal:
    n,c=min(graph[s],key=lambda x:x[1]+V[x[0]])
    path.append(n); cost+=c; s=n
print("Optimal taxi route:",path)
print("Cost:",cost)

