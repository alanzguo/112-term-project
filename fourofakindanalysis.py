from cardclass import *

#analyzes four-card subsets for the presence of a four-of-a-kind

def isFourOfAKindFromSubsets(fourCardSubsets):
    fourList = []
    for i in range(len(fourCardSubsets)):
        if isFourOfAKind(fourCardSubsets[i]):
            cards = fourCardSubsets[i]
            fourList.append(cards)
    if fourList == []: return None
    else:
        highestFour = fourList[0]
        for i in range(len(fourList)):
            cards = fourList[i]
            if cards[0] > highestFour[0]:
                highestFour = cards
        return cards

def isFourOfAKind(cards):
    if cards[0] == cards[1] and cards[2] == cards[3] and cards[1] == cards[2]:
        return True
