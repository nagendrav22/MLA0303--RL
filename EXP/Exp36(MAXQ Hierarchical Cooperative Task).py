tasks={
'Main':['Collect','Deliver'],
'Collect':['GoToStorage','PickItem'],
'Deliver':['GoToCustomer','DropItem']
}

def maxq(task):
    if task not in tasks:
        print("Primitive:",task)
        return 1
    total=0
    for sub in tasks[task]:
        total+=maxq(sub)
    return total

score=maxq('Main')
print("Hierarchical MAXQ task score:",score)
