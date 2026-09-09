graph={
'A':['B','C'],'B':['D'],'C':['D'],'D':['E'],'E':[]
}
rules={'A':'start','B':'intersection','C':'intersection','D':'intersection','E':'destination'}

def safe_path(node,path):
    if node=='E': return path+[node]
    for nxt in graph[node]:
        if nxt not in path:
            result=safe_path(nxt,path+[node])
            if result:return result
    return None

path=safe_path('A',[])
print("Safe route:",path)
print("Traffic rules respected:",all(rules[x] in ['start','intersection','destination'] for x in path))
