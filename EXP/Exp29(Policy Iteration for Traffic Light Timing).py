states=['Low','Medium','High']
actions=['Short','Long']
reward={
('Low','Short'):5,('Low','Long'):2,
('Medium','Short'):1,('Medium','Long'):6,
('High','Short'):-4,('High','Long'):8
}
policy={s:'Short' for s in states}

for _ in range(10):
    V={s:reward[(s,policy[s])] for s in states}
    stable=True
    for s in states:
        best=max(actions,key=lambda a:reward[(s,a)])
        if best!=policy[s]: policy[s]=best; stable=False
    if stable: break

print("Optimal traffic-light policy:",policy)
print("State rewards:",V)
