# Simplified comparison framework using synthetic learning scores
import numpy as np

episodes=np.arange(1,101)
rng=np.random.default_rng(1)
dqn=np.cumsum(rng.normal(0.08,0.03,100))
ddqn=np.cumsum(rng.normal(0.09,0.025,100))
dueling=np.cumsum(rng.normal(0.10,0.02,100))
per=np.cumsum(rng.normal(0.12,0.018,100))

print("Final performance:")
print("DQN:",dqn[-1])
print("Double DQN:",ddqn[-1])
print("Dueling DQN:",dueling[-1])
print("PER:",per[-1])
