import random, math

rates=[0.05,0.12,0.20,0.10]
N=4; T=5000

def reward(i): return 1 if random.random()<rates[i] else 0

# epsilon-greedy
counts=[0]*N; values=[0.0]*N
for t in range(T):
    a=random.randrange(N) if random.random()<0.1 else max(range(N),key=lambda i:values[i])
    r=reward(a); counts[a]+=1; values[a]+=(r-values[a])/counts[a]
eg_ctr=sum(counts[i]*values[i] for i in range(N))/T

# UCB
counts=[1]*N; values=[reward(i) for i in range(N)]
for t in range(N,T):
    a=max(range(N),key=lambda i:values[i]+math.sqrt(2*math.log(t+1)/counts[i]))
    r=reward(a); counts[a]+=1; values[a]+=(r-values[a])/counts[a]
ucb_ctr=sum(counts[i]*values[i] for i in range(N))/T

# Thompson Sampling
success=[1]*N; failure=[1]*N; clicks=0
for _ in range(T):
    samples=[random.betavariate(success[i],failure[i]) for i in range(N)]
    a=max(range(N),key=lambda i:samples[i]); r=reward(a); clicks+=r
    success[a]+=r; failure[a]+=1-r
ts_ctr=clicks/T
print("CTR - Epsilon Greedy:",eg_ctr)
print("CTR - UCB:",ucb_ctr)
print("CTR - Thompson Sampling:",ts_ctr)
