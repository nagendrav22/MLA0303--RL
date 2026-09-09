import numpy as np

# Learn a reusable parameter across several simple tasks
tasks=[1.0,2.0,3.0,4.0]
meta=0.0
for _ in range(500):
    task=np.random.choice(tasks)
    adapted=meta+0.2*(task-meta)
    meta+=0.01*(adapted-meta)

print("Meta-learned initialization:",round(float(meta),3))
for task in tasks:
    adapted=meta
    for _ in range(5):
        adapted+=0.2*(task-adapted)
    print("Task",task,"adapted parameter:",round(float(adapted),3))
