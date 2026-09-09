import random

hidden_states=['safe','victim','obstacle']
observations={'safe':'clear','victim':'signal','obstacle':'blocked'}
belief={s:1/3 for s in hidden_states}

for _ in range(5):
    state=random.choice(hidden_states)
    obs=observations[state]
    for s in belief:
        belief[s]=0.8 if observations[s]==obs else 0.1
    total=sum(belief.values())
    belief={s:v/total for s,v in belief.items()}
    print("Observation:",obs,"Belief:",{k:round(v,2) for k,v in belief.items()})
