import random

actions = ["Low", "Medium", "High"]

value = {"Low": 0, "Medium": 0, "High": 0}

count = {"Low": 0, "Medium": 0, "High": 0}

for i in range(10):

    action = random.choice(actions)

    if action == "Low":
        reward = random.randint(2, 4)
    elif action == "Medium":
        reward = random.randint(5, 7)
    else:
        reward = random.randint(8, 10)

    count[action] += 1
    value[action] = value[action] + (reward - value[action]) / count[action]

    print("Cycle:", i + 1)
    print("Machine Setting:", action)
    print("Reward:", reward)
    print()

print("Value Function:")
for action in actions:
    print(action, "=", round(value[action], 2))
