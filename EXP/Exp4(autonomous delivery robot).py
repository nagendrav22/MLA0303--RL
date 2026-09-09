states=['Warehouse','Junction','Customer','Return']
edges={
 'Warehouse':[('Junction',2)],
 'Junction':[('Customer',3),('Warehouse',2)],
 'Customer':[('Return',1)],
 'Return':[]
}
V={s:0 for s in states}
for _ in range(20):
    new={}
    for s in states:
        if not edges[s]: new[s]=0
        else: new[s]=min(cost+V[ns] for ns,cost in edges[s])
    V=new

s='Warehouse'; path=[s]; total=0
while edges[s]:
    ns,cost=min(edges[s],key=lambda x:x[1]+V[x[0]])
    path.append(ns); total+=cost; s=ns
print("Optimal path:",path)
print("Minimum travel cost:",total)
