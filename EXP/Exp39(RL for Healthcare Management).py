import random

states=['Low','Medium','High']
actions=['Schedule','Delay','Allocate']
Q={(s,a):0.0 for s in states for a in actions}

for _ in range(3000):
    s=random.choice(states)
    a=random.choice(actions)
    if s=='High' and a=='Allocate': reward=10
    elif s=='Low' and a=='Delay': reward=5
    else: reward=-1
    Q[(s,a)]+=0.1*(reward-Q[(s,a)])

policy={s:max(actions,key=lambda a:Q[(s,a)]) for s in states}
print("Learned healthcare policy:",policy)
print("Q-values:",Q)
