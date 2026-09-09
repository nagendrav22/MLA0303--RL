import random

temperatures=[18,20,22,24,26]
Q={t:0.0 for t in temperatures}

for _ in range(2000):
    t=random.choice(temperatures)
    comfort=-abs(t-22)
    energy=-0.2*abs(t-18)
    reward=comfort+energy
    Q[t]+=0.1*(reward-Q[t])

best=max(Q,key=Q.get)
print("Learned temperature settings:",Q)
print("Best setting:",best,"°C")

