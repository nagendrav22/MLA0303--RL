import random

states=['Clean','Dirty','Goal']
actions=['clean','move']
Q={(s,a):0.0 for s in states for a in actions}
returns={(s,a):[] for s in states for a in actions}

for episode in range(3000):
    s='Dirty'; episode_data=[]
    for _ in range(10):
        a=random.choice(actions)
        if s=='Dirty' and a=='clean':
            ns='Clean'; r=10
        elif a=='move':
            ns='Goal'; r=5 if s=='Clean' else -2
        else:
            ns=s; r=-1
        episode_data.append((s,a,r)); s=ns
        if s=='Goal': break
    G=0
    visited=set()
    for s,a,r in reversed(episode_data):
        G=0.9*G+r
        if (s,a) not in visited:
            returns[(s,a)].append(G)
            Q[(s,a)]=sum(returns[(s,a)])/len(returns[(s,a)])
            visited.add((s,a))

print("Learned Q-values:",Q)
print("Best action in Dirty state:",max(actions,key=lambda a:Q[('Dirty',a)]))
