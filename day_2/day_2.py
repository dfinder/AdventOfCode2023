def min_amount(pulls:list,key:str) -> int:
    if len(pulls) == 1:
        return pulls[0][key]
    return max(pulls[0][key],min_amount(pulls[1:],key))

def eval(pulls:dict) -> bool:
    return pulls['red']<13 and pulls['green']<14 and pulls['blue']<15
def parse(line:str) -> int:
    id_split= line.split(":")
    id = int((id_split[0]).split(" ")[-1])
    pulls = id_split[1].split(";")
    final_pulls=list(map(parse_pulls,pulls))
    if all(list(map(eval,final_pulls))):
        return id
    return 0
def parse_2(line:str) -> int:
    id_split= line.split(":")
    id = int((id_split[0]).split(" ")[-1])
    pulls = id_split[1].split(";")
    final_pulls=list(map(parse_pulls,pulls))
    return min_amount(final_pulls,'red') * min_amount(final_pulls,'blue') * min_amount(final_pulls,'green')
def parse_pulls(line:str)-> dict:
    pull_dict = {'red':0,'blue':0,'green':0}
    itemized = line.split(",")
    for x in itemized:
        for y in pull_dict.keys():
            if y in x:
                pull_dict[y]=int(x.strip().split(' ')[0])
    return pull_dict
with open('./day_2.txt') as file_data:
    data = file_data.readlines()
    print(list(map(parse,data)))
    print(sum(list(map(parse_2,data))))