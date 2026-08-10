import random
class SimpleChess:
    def __init__(self):
        self.reset()
    def reset(self):
        # Simplified board states
        self.state = "start"
        return self.state
    def get_actions(self, state):
        actions = {
            "start": ["attack", "defend"],
            "attack_state": ["capture", "retreat"],
            "defend_state": ["counter", "wait"]
        }
        return actions.get(state, [])
    def step(self, action):
        if self.state == "start":
            if action == "attack":
                self.state = "attack_state"
                reward = 5
            else:
                self.state = "defend_state"
                reward = 2
        elif self.state == "attack_state":
            if action == "capture":
                self.state = "win"
                reward = 100
            else:
                self.state = "lose"
                reward = -50
        elif self.state == "defend_state":
            if action == "counter":
                self.state = "win"
                reward = 80
            else:
                self.state = "lose"
                reward = -30
        done = self.state in ["win", "lose"]
        return self.state, reward, done
class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
    def get_q(self, state, action):
        return self.q_table.get((state, action), 0)
    def choose_action(self, env, state):
        actions = env.get_actions(state)
        if random.random() < self.epsilon:
            return random.choice(actions)
        q_values = [self.get_q(state, a) for a in actions]
        max_q = max(q_values)
        best_actions = [
            a for a, q in zip(actions, q_values)
            if q == max_q
        ]
        return random.choice(best_actions)
    def update(self, state, action, reward, next_state, env):
        next_actions = env.get_actions(next_state)
        if next_actions:
            future_q = max(
                [self.get_q(next_state, a)
                 for a in next_actions]
            )
        else:
            future_q = 0
        old_q = self.get_q(state, action)
        new_q = old_q + self.alpha * (
            reward + self.gamma * future_q - old_q
        )
        self.q_table[(state, action)] = new_q

env = SimpleChess()
agent = QLearningAgent()

episodes = 1000

for episode in range(episodes):

    state = env.reset()
    done = False

    while not done:

        action = agent.choose_action(env, state)

        next_state, reward, done = env.step(action)

        agent.update(
            state,
            action,
            reward,
            next_state,
            env
        )

        state = next_state

print("Learned Q-values:\n")

for key, value in agent.q_table.items():
    print(key, ":", round(value, 2))

print("\nOptimal Policy:\n")

for state in ["start", "attack_state", "defend_state"]:

    actions = env.get_actions(state)

    best_action = max(
        actions,
        key=lambda a: agent.get_q(state, a)
    )

    print(f"{state} --> {best_action}")
