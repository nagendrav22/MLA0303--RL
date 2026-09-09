import random, math

prices=[80,100,120,140]
true_demand=[0.8,0.7,0.5,0.3]

def sale(i): return random.random()<true_demand[i]

for method in ['epsilon-greedy','UCB','thompson']:
    revenue=[0]*4; counts=[0]*4; success=[1]*4; failure=[1]*4
    for t in range(5000):
        if method=='epsilon-greedy':
            a=random.randrange(4) if random.random()<0.1 or not any(counts) else max(range(4),key=lambda i:revenue[i]/max(1,counts[i]))
        elif method=='UCB':
            if t<4: a=t
            else: a=max(range(4),key=lambda i:revenue[i]/counts[i]+math.sqrt(2*math.log(t+1)/counts[i]))
        else:
            a=max(range(4),key=lambda i:random.betavariate(success[i],failure[i]))
        r=prices[a] if sale(a) else 0
        revenue[a]+=r; counts[a]+=1
        if method=='thompson':
            success[a]+=r>0; failure[a]+=r==0
    print(method,"total revenue:",sum(revenue))
