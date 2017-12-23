from cardclass import *
from pairanalysis import *
from threeofakindanalysis import *
#uses formerly established pair and three-of-a-kind detection methods to
#identify a full house

#analyzes five-card subsets for the presence of a "full house", a set of cards
#that contains exactly 1 pair of unique values

def isFullHouseFromSubsets(threeCardSubsets,twoCardSubsets):
    three = isThreeOfAKindFromSubsets(threeCardSubsets)
    if three == None: return None
    newTwoCardSubset = []
    for i in range(len(twoCardSubsets)):
        if three[0] in twoCardSubsets[i] or three[1] in twoCardSubsets[i] or three[2] in twoCardSubsets[i]:
            continue
        else:
            newTwoCardSubset.append(twoCardSubsets[i])
    two = isPairFromSubsets(newTwoCardSubset)
    if two == None: return None
    fullhouse = three + two
    if two[0] != three[0]:
        return fullhouse
