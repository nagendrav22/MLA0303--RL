import random

true_rates=[0.10,0.20,0.15,0.30]
counts=[0]*4
values=[0.0]*4
epsilon=0.1

for _ in range(10000):
    if random.random()<epsilon:
        arm=random.randrange(4)
    else:
        arm=max(range(4),key=lambda i:values[i])
    reward=1 if random.random()<true_rates[arm] else 0
    counts[arm]+=1
    values[arm]+= (reward-values[arm])/counts[arm]

print("Estimated CTR:",values)
print("Best advertisement:",max(range(4),key=lambda i:values[i])+1)
