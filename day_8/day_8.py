import math
from functools import reduce
with open("input.txt") as f:
    ur_directions=f.readline().strip()
    f.readline()#empty line
    nodes_raw=f.readlines()
    #print(nodes)
    depickler = lambda x: (x.split("=")[0].strip() , (x.split("=")[1].split(",")[0][2:],x.strip().split(",")[1][1:4]))
    nodes = dict(map(depickler,nodes_raw))
    #print(nodes)
    directions = list(ur_directions)
    #print(nodes['AAA'])
    current = list(set(filter(lambda x: "A" in x, nodes.keys())))
    
    #print(current)
    
    acc = len(current)*[0]
    #print(directions)
   
    for x,cur in enumerate(current):
        while(not "Z" in current[x]):
            if directions[acc[x] % len(directions)] == 'L':
                current[x] = nodes[current[x]][0]
            else:
                current[x] = nodes[current[x]][1]
            acc[x] = acc[x]+1
            print(current[x])
            print(acc)
            #print(current)
    print(reduce(math.lcm,acc))
