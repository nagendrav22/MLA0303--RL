import random

students=['Beginner','Intermediate','Advanced']
content=['Basic','Practice','Advanced']
Q={(s,c):0.0 for s in students for c in content}

for _ in range(3000):
    s=random.choice(students)
    c=random.choice(content)
    if s=='Beginner' and c=='Basic': reward=10
    elif s=='Intermediate' and c=='Practice': reward=10
    elif s=='Advanced' and c=='Advanced': reward=10
    else: reward=-2
    Q[(s,c)]+=0.1*(reward-Q[(s,c)])

for s in students:
    best=max(content,key=lambda c:Q[(s,c)])
    print(s,"-> recommended content:",best)
