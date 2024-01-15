#okay so:
ranking = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
ranking.reverse()

#we need a hand type that implements a comparator
def hand_rank(hand): #This doesn't work because 2 pair == 3 of a kindgit
    cards, _ = hand 
    print(cards, [cards.count(x) for x in cards])
    return sum([cards.count(x) for x in cards])
def high_card(hand): #NEED TO FIX, WE NEED TO SORT AND POP
    cards, _ = hand 
    return sum([13**ranking.index(x) for x in cards])
class myComparator(tuple):
    def __lt__(self,other):
        #print((self,hand_rank(self),high_card(self)))
        #print((other,hand_rank(other),high_card(other)))
        if hand_rank(self) == hand_rank(other):
            #print(hand_rank(self))
            return high_card(self) < high_card(other)
        return hand_rank(self) < hand_rank(other)
    

with open("input.txt") as f:
    hands0 = [line.strip().split(" ") for line in f.readlines()]
    #print(hands0)
    hands = (list(map(lambda x: (list(x[0]),int(x[1])), hands0)))
    hands_sorted= sorted(hands,key=myComparator)
   #hands_sorted.reverse()
    hands_sorted.reverse()
    print(list(map(lambda x: (hand_rank (x),x),hands_sorted)))
    #print(sum(list(map(lambda x: x[1]*(hands_sorted.index(x)+1),hands_sorted))))