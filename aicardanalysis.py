from cardclass import *
from straightanalysis import *
from flushanalysis import *
from fourofakindanalysis import *
from fullhouseanalysis import *
from threeofakindanalysis import *
from pairanalysis import *
from highcardanalysis import *


#card analysis
def createCardList(pocket, river):
    Cards = []
    for card in pocket:
        Cards.append(card)
    for card in river:
        Cards.append(card)
    return Cards

#powerset, so that the subsets of all cards are returned
def powerset(L):
    if L == []: return [[]]
    else:
        subsets = []
        for subset in powerset(L[1:]):
            subsets += [subset]
            subsets += [[L[0]] + [subset]]
        return subsets

def powerset1(s):
    x = len(s)
    result = []
    for i in range(1 << x):
        result+= [[s[j] for j in range(x) if (i & (1 << j))]]
    return result

#returns all five-card subsets, in order to search for straights and flushes,
#royal straight flushes, and full houses
def fiveCardSubsets(powersetOfCards):
    result = []
    for i in range(len(powersetOfCards)):
        if len(powersetOfCards[i]) == 5: result.append(powersetOfCards[i])
    return result

#returns all four-card subsets, in order to search for four-of-a-kind hands
def fourCardSubsets(powersetOfCards):
    result = []
    for i in range(len(powersetOfCards)):
        if len(powersetOfCards[i]) == 4: result.append(powersetOfCards[i])
    return result

#returns all four-card subsets, in order to search for three-of-a-kind hands
def threeCardSubsets(powersetOfCards):
    result = []
    for i in range(len(powersetOfCards)):
        if len(powersetOfCards[i]) == 3: result.append(powersetOfCards[i])
    return result

#returns all two-card subsets, in order to search for pairs
def twoCardSubsets(powersetOfCards):
    result = []
    for i in range(len(powersetOfCards)):
        if len(powersetOfCards[i]) == 2: result.append(powersetOfCards[i])
    return result


#completely analyzes the best option for any given set of 2 player pocket cards
#and the given river
def AICardAnalysis(pocket,river,submode):
    cards = createCardList(pocket, river)
    cardset = powerset1(cards)
    fiveCardSubset = fiveCardSubsets(cardset)
    fourCardSubset = fourCardSubsets(cardset)
    threeCardSubset = threeCardSubsets(cardset)
    twoCardSubset = twoCardSubsets(cardset)
    bestHand,handtype = [highCard(cards)],"high card"
    betType = None
    if isPairFromSubsets(twoCardSubset) != None:
        betType = "low"
    if isTwoPairFromSubsets(twoCardSubset) != None:
        betType = "low"
    if isAlmostStraightFromSubsets(fourCardSubset) and submode != "river":
        betType = "low"
    if isThreeOfAKindFromSubsets(threeCardSubset) != None:
        if submode == "flop": betType = "mid"
        else: betType = "low"
    if isFlushFromSubsets(fourCardSubset):
        if submode == "flop": betType = "mid"
        elif submode == "turn": betType = "low"
    if isStraightFromSubsets(fiveCardSubset) != None:
        betType = "mid"
    if isFlushFromSubsets(fiveCardSubset) != None:
        betType = "mid"
    if isFullHouseFromSubsets(threeCardSubset,twoCardSubset) != None:
        betType = "high"
    if isFourOfAKindFromSubsets(fourCardSubset) != None:
         betType = "high"
    if isStraightFlushFromSubsets(fiveCardSubset) != None:
        betType = "very high"
    print(betType)
    return betType

#test cases:
#pocket1 = [Card("3","Hearts"),Card("2","Hearts")]
#river1 = [Card("4","Hearts"),Card("5","Hearts"),Card("6","Hearts"),Card("10","Diamonds"),Card("Jack","Spades")]
#print(AICardAnalysis(pocket1,river1,"flop"))

#pocket2 = [Card("King","Hearts"),Card("Queen","Hearts")]
#river2 = [Card("King","Diamonds"),Card("King","Spades"),Card("Queen","Diamonds"),Card("2","Diamonds"),Card("3","Spades")]
#print(AICardAnalysis(pocket2,river2,"flop"))


