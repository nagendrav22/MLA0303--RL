import random

prob_high = 0.5

learning_rate = 0.05

for i in range(100):

    if random.random() < prob_high:
        action = "High"
        reward = random.randint(8, 15)
    else:
        action = "Low"
        reward = random.randint(4, 8)

    if action == "High":
        prob_high = prob_high + learning_rate * (reward / 20)
    else:
        prob_high = prob_high - learning_rate * (reward / 20)

    prob_high = max(0, min(1, prob_high))

print("Final Probability of High Risk Investment:", round(prob_high, 2))
