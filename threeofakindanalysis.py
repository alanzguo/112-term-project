from cardclass import *

#analyzes three-card subsets for the presence of a "three-of-a-kind", returns
#the largest three-of-a-kind available
def isThreeOfAKindFromSubsets(threeCardSubsets):
    threeList = []
    for i in range(len(threeCardSubsets)):
        if isThreeOfAKind(threeCardSubsets[i]):
            threeList.append(threeCardSubsets[i])
    if threeList == []:return None
    else:
        highestThree = threeList[0]
        for i in range(len(threeList)):
            cards = threeList[i]
            if cards[0] > highestThree[0]:
                highestThree = cards
        return highestThree

def isThreeOfAKind(cards):
    if cards[0].value == cards[1].value and cards[1].value == cards[2].value:
        return True
#test cases:
#cards = [Card("2","Hearts"),Card("2","Diamonds"),Card("2","Spades")]
#print(isThreeOfAKind(cards))
