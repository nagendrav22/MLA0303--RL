# Simplified MAXQ-style hierarchical decomposition
tasks={
'CleanHouse':['CleanRoom1','CleanRoom2'],
'CleanRoom1':['Vacuum','Dust'],
'CleanRoom2':['Vacuum','Dust']
}

def execute(task):
    if task in tasks:
        for sub in tasks[task]:
            execute(sub)
    else:
        print("Executing primitive task:",task)

execute('CleanHouse')
