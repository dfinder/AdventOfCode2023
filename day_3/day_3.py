import functools

from operator import *


with open("./day_3_test.txt") as f:
    matrix = f.readlines()
    foldr = lambda func, acc, xs: functools.reduce(lambda x, y: func(y, x), xs[::-1], acc)
    symbols = [(x,y) for x,row in enumerate(matrix) for y,i in enumerate(row.strip()) if not (i.isnumeric() or i=='.') ]
    numbers = [(x,y,int(i))for x,row in enumerate(matrix) for y,i in enumerate(row) if i.isnumeric() ]
    merged_list = []
    orig_iter = iter(numbers)
    previous_tuple=next(orig_iter)
    for next_tuple in orig_iter:
        (x0,y0,z0)=previous_tuple
        (x1,y1,z1)=next_tuple
        if (x1==x0) and (y1==y0+len(str(z0))): 
            if(previous_tuple in merged_list):
                merged_list.remove(previous_tuple)
            merged_list.append((x0,y0,z0*10+z1))
            previous_tuple=(x0,y0,z0*10+z1)
        else: 
            merged_list.append(next_tuple)
            previous_tuple=next_tuple
    
    #print(merged_list)
    checksum = 0
    total_list=[]
    for row,col,val in merged_list:
        surrounding_points = []
        lenz=len(str(val))
        if row!=0:
            for i in range(col,col+lenz):
                surrounding_points.append((row-1,i))
            if col!=0:
                surrounding_points.append((row-1,col-1))
            if col+lenz!=len(matrix[0]):
                surrounding_points.append((row-1,col+lenz))
        if col!=0:
            surrounding_points.append((row,col-1))
        if col+lenz!=len(matrix[0]):
            surrounding_points.append((row,col+lenz))
        if row!=len(matrix)-1:
            for i in range(col,col+lenz):
                surrounding_points.append((row+1,i))
            if col!=0:
                surrounding_points.append((row+1,col-1))
            if col+lenz!=len(matrix[0]):
                surrounding_points.append((row+1,col+lenz))
        
        surrounding_points = set(surrounding_points)
        if any([i in symbols for i in surrounding_points]):
            checksum+=val 
            adjacency_list=[(x,y,matrix[x][y]) for (x,y) in surrounding_points if (x,y) in symbols]

            total_list.append(((row,col,val),adjacency_list))
            print("---")
            print((row,col,val))
            print(surrounding_points)

#    print(len(matrix))
    print(checksum)
#    print(symbols)
    print(total_list)
    merge_one = [(val,adj[0]) for ((r,c,val),adj) in total_list]
    merge_two = [(val,x,y,c) for (val,(x,y,c)) in merge_one]
    reduction = {}
    for (val,x,y,c) in merge_two:
        if (x,y) in reduction.keys():
            reduction[(x,y)].append(val)
        else:
            reduction[(x,y)]=[val]

    print(reduction)
    checksum_2 = 0
    for (x,y) in reduction.keys():
        if len(reduction[(x,y)])==2:
            checksum_2+=(reduction[(x,y)][0]*reduction[(x,y)][1])
            print(reduction[(x,y)])
    print(checksum_2)
           
    #print(merge_two)
#    print(sum([x for (_,_,x) in total_list]))

    #part 2
