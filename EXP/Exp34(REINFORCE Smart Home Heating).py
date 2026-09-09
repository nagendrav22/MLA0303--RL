import random

temps=list(range(18,27))
theta={t:0.0 for t in temps}

for _ in range(5000):
    t=random.choice(temps)
    comfort=-abs(t-22)
    energy=-0.1*abs(t-20)
    reward=comfort+energy
    theta[t]+=0.01*reward

best=max(temps,key=lambda t:theta[t])
print("Optimal temperature:",best,"°C")
print("Policy scores:",theta)
