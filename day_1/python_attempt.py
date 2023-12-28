import sys

def first_number(line:str)->str:
    return list(filter(lambda x:x.isnumeric(),line))[0]
def last_number(line:str)->str:
    return list(filter(lambda x:x.isnumeric(),line))[-1]
def translate_line(line:str)->int:
    return int(first_number(line)+last_number(line))
def translate_numbers(line:str)->str:
    number_map = {
        'one':'o1e',
        'two':'t2o',
        'three':'t3e',
        'four':'f4r',
        'five':'5e',
        'six':'6',
        'seven':'s7',
        'eight':'e8t',
        'nine':'ni9e'
    }
    for strnum,num in number_map.items():
        line=line.replace(strnum,num)
    return line
with open("./input.txt") as inp:
    lines=inp.readlines()
    translation = map(translate_line,map(translate_numbers,lines))
    print(sum(list(translation)))