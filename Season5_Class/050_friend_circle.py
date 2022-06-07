n=int(input())
nodes=list(range(n))
father=list(range(n))
 
m=int(input())
edges=[]
for i in range(m):
    edge=[int(i) for i in input().split(' ')]
    edges.append(edge)
for edge in edges:
    head=edge[0]
    tail=edge[1]
    father[tail]=head
for node in nodes:
    while True:
        # 对于每个节点，找它的父节点，看他的父节点的父节点是谁，直到找到父节点跟节点相同，说明到头
        father_of_node=father[node]
        if father_of_node!=father[father_of_node]:
            father[node]=father[father_of_node]
        else:
            break
dic={}
for i,f in enumerate(father):
    dic[f]=[]
print(len(dic))