lines_procesing = lambda x: x.split(":")[1].split("|")
card_processing = lambda x: x.replace("  "," ").strip().split(" ")
type_processing = lambda x: map(int,card_processing(x))
import math
with open("input.txt") as f:
    lines =f.readlines()
    lines_processed= [math.floor(2**(len(set(type_processing(lines_procesing(x)[0])).intersection(set(type_processing(lines_procesing(x)[1]))))-1)) for x in lines]
    #print(sum(lines_processed))
    lines_processed_2 = [len(set(type_processing(lines_procesing(x)[0])).intersection(set(type_processing(lines_procesing(x)[1])))) for x in lines]
    #print(lines_processed_2)

 
    new_process=[1]*len(lines_processed_2)
    print(new_process)
    new_process[0]=1
    for n in range(0,len(lines_processed_2)):
        print(lines_processed_2[0:n+1])
        
        first = new_process[n]

        print(first)
        for i in range(n+1,min(n+lines_processed_2[n]+1,len(new_process))):
            new_process[i] += first
            print("We win "+str(first)+" tickets for card "+str(i+1))
        print(new_process)

    print(sum(new_process))