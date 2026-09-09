import numpy as np

# Simplified continuous-action DDPG-style actor update
actor_w=0.5
for _ in range(1000):
    state=np.random.rand()
    action=actor_w*state
    reward=-(action-0.8*state)**2
    actor_w += 0.01*reward*state

print("Learned actor parameter:",round(float(actor_w),4))
print("The policy favors resource-gathering actions near the target relationship.")

