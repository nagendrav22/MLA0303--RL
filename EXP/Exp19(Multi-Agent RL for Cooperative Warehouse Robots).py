import random

robots=[0,1,2]
tasks=[('A',2),('B',4),('C',6)]
assignments={}

for i,robot in enumerate(robots):
    assignments[robot]=tasks[i]

total=0
for robot,(task,distance) in assignments.items():
    reward=10-distance
    total+=reward
    print("Robot",robot,"->",task,"reward:",reward)
print("Total cooperative reward:",total)
