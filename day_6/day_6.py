from functools import reduce 
def meets_distance(pause,time,distance):
    return distance<(time-pause)*pause
def distances(lower,upper,time,distance):
    if not meets_distance(lower,time,distance):
        print("Can't make it in "+str(lower)+" time")
        return distances(lower+1,upper,time,distance)
    if not meets_distance(upper,time,distance):
        print("Can't make it in "+str(upper)+" time")
        return distances(lower,upper-1,time,distance)
    if meets_distance(lower,time,distance) and meets_distance(upper,time,distance):
        return (upper-lower+1)
def distances_2(time,distance):
    i=0
    while not meets_distance(i,time,distance):
        i=i+1
    return (time-2*i)+1

times = [58,99,64,69]
distance=[478,2232,1019,1071]
#times = [7,15,30]
#distance=[9,40,200]  

print(list(map( lambda x,y: distances(0,x,x,y), times,distance)))
print(reduce((lambda x,y: x*y), list(map( lambda x,y: distances(0,x,x,y), times,distance))))
 

#part 2:

time = 58996469
distance=478223210191071
print(distances_2(time,distance))