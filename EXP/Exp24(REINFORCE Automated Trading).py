import random

actions=['BUY','SELL','HOLD']
theta=[0.0,0.0,0.0]

for _ in range(3000):
    m=max(theta); ex=[pow(2.71828,x-m) for x in theta]
    p=[x/sum(ex) for x in ex]
    a=random.choices(range(3),weights=p)[0]
    market=random.choice([1,-1])
    reward=market if actions[a]=='BUY' else -market if actions[a]=='SELL' else 0
    theta[a]+=0.01*reward

m=max(theta); ex=[pow(2.71828,x-m) for x in theta]
p=[x/sum(ex) for x in ex]
print(dict(zip(actions,[round(x,3) for x in p])))

