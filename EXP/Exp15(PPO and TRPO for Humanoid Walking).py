# Minimal policy-update demonstration (educational simulation)
import numpy as np

policy=np.array([0.5,0.5]) # action probabilities
old=policy.copy()
advantage=np.array([1.0,-0.5])
clip=0.2

for _ in range(20):
    ratio=policy/(old+1e-8)
    clipped=np.clip(ratio,1-clip,1+clip)
    objective=np.minimum(ratio*advantage,clipped*advantage).sum()
    grad=np.array([advantage[0],advantage[1]])*0.01
    policy+=grad
    policy=np.maximum(policy,0); policy/=policy.sum()

print("PPO-style updated policy:",policy)
print("TRPO would additionally constrain the KL divergence between old and new policies.")

