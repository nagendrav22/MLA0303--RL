# Simplified chess: King moves on a 3x3 board toward the goal
states = [(r,c) for r in range(3) for c in range(3)]
actions = [(-1,0),(1,0),(0,-1),(0,1)]
goal = (2,2)

V = {s: 0.0 for s in states}
gamma = 0.9

for _ in range(50):
    newV = V.copy()
    for s in states:
        if s == goal:
            newV[s] = 10
            continue
        values = []
        for dr,dc in actions:
            ns = (s[0]+dr, s[1]+dc)
            if ns in V:
                reward = 10 if ns == goal else -1
                values.append(reward + gamma*V[ns])
        if values:
            newV[s] = max(values)
    V = newV

s=(0,0)
path=[s]
while s != goal:
    best=None
    best_val=-float("inf")
    for dr,dc in actions:
        ns=(s[0]+dr,s[1]+dc)
        if ns in V:
            reward=10 if ns==goal else -1
            val=reward+gamma*V[ns]
            if val>best_val:
                best_val=val; best=ns
    if best is None: break
    s=best; path.append(s)
print("Optimal path:", path)
print("State values:", V)
