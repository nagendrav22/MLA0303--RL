import random

locations=['A','B','C']
belief={x:1/3 for x in locations}
observations={'A':'near-wall','B':'open','C':'near-wall'}

for step in range(5):
    actual=random.choice(locations)
    obs=observations[actual]
    for loc in locations:
        belief[loc]=0.8 if observations[loc]==obs else 0.1
    total=sum(belief.values())
    belief={k:v/total for k,v in belief.items()}
    best=max(belief,key=belief.get)
    print("Step",step+1,"observation:",obs,"estimated location:",best)

print("Final belief:",belief)

