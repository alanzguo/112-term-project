from cardclass import *

#analyzes two-card subsets for the presence of a pair, returns the highest pair
def isPairFromSubsets(twoCardSubsets):
    pairList = []
    for i in range(len(twoCardSubsets)):
        cards = twoCardSubsets[i]
        if isPair(cards):
            pairList.append(cards)
    if pairList == []: return None
    else:
        highestPair = pairList[0]
        for i in range(len(pairList)):
            cards = pairList[i]
            if cards[0] > highestPair[0]:
                highestPair = cards
        return highestPair

def isTwoPairFromSubsets(twoCardSubsets):
    pairList = []
    for i in range(len(twoCardSubsets)):
        cards = twoCardSubsets[i]
        if isPair(cards):
            pairList.append(cards)
    if len(pairList) < 2: return None
    else:
        highestPair = pairList[0]
        for i in range(len(pairList)):
            cards = pairList[i]
            if cards[0] > highestPair[0]:
                highestPair = cards
        pairList.remove(highestPair)
        secondHighestPair = pairList[0]
        for i in range(len(pairList)):
            cards = pairList[i]
            if cards[0] > secondHighestPair[0]:
                secondHighestPair = cards
        twoPair = []
        twoPair.append(highestPair)
        twoPair.append(secondHighestPair)
        return twoPair

#given a list of two cards, returns true if the two cards have the same value
def isPair(cards):
    return cards[0].value == cards[1].value

#print(isPair([Card("2","Hearts"),Card("2","Diamonds")]))
