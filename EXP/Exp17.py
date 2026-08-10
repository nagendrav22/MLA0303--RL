import gym

env = gym.make("MountainCar-v0")

state = env.reset()

print("Starting MountainCar Simulation")

for i in range(20):

    action = env.action_space.sample()

    state, reward, done, info = env.step(action)

    print("Step:", i + 1)
    print("Action:", action)
    print("Reward:", reward)

    if done:
        print("Goal Reached!")
        break

env.close()
