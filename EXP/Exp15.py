import random

episodes = 100
total_time = 0

for i in range(episodes):

    representative = random.choice(["Junior", "Senior"])

    if representative == "Senior":
        time = random.randint(3, 5)   
    else:
        time = random.randint(6, 10)  

    total_time += time

average_time = total_time / episodes

print("Total Calls:", episodes)
print("Average Call Handling Time:", average_time, "minutes")exp-
