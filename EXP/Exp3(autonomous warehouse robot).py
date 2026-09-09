states=['A','B','C','D','E']
actions=['left','right']
transitions={
 'A':{'right':'B'}, 'B':{'left':'A','right':'C'},
 'C':{'left':'B','right':'D'}, 'D':{'left':'C','right':'E'},
 'E':{'left':'D'}
}
reward=lambda s: 10 if s=='E' else -1

V={s:0 for s in states}
gamma=0.9
for _ in range(50):
    new={}
    for s in states:
        vals=[]
        for a in actions:
            if a in transitions.get(s,{}):
                ns=transitions[s][a]
                vals.append(reward(ns)+gamma*V[ns])
        new[s]=max(vals) if vals else 0
    V=new

print("State values:",V)
print("Best next actions:")
for s in states:
    choices=[]
    for a,ns in transitions.get(s,{}).items():
        choices.append((reward(ns)+gamma*V[ns],a,ns))
    if choices: print(s,max(choices))

