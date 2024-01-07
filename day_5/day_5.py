import functools
def range_translation(triplets,x):
    for drange,srange,rlen in triplets:
        if x in range(srange,srange+rlen):
            return x-srange+drange 
    return x

def recursive_mapping(list_of_maps,seed):
    if len(list_of_maps)==0:
        return seed
    return recursive_mapping(list_of_maps[1:],range_translation(list_of_maps[0],seed))

with open("./input.txt") as f:
    mylines = f.read().split(":")
    mylines_processed = [x.split('\n\n')[0].strip().split("\n") for x in mylines][1:]
    numeriziser = lambda x: tuple(map(int,x.split(" ")))
    seeds=numeriziser(mylines_processed[0][0])
    maps=[[numeriziser(x) for x in i] for i in mylines_processed[1:]]
    starts = seeds[0::2]
    ranges = seeds[1::2]
    seed_ranges = [range(i,i+ranges[ix]) for ix,i in enumerate(starts)]
    #print(seed_ranges[0])
    print(min(min([recursive_mapping(maps,x) for x in i]) for i in seed_ranges))
