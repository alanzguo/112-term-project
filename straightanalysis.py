from cardclass import *
from flushanalysis import *

#analysis for straights in a set of cards

#following functions test for a straight within a set of five-card subsets
def isStraightFromSubsets(fiveCardSubsets):
    straightList = []
    for i in range(len(fiveCardSubsets)):
        cards = sortCards(fiveCardSubsets[i])
        if isStraight(fiveCardSubsets[i]):
            straightList.append(cards)
    if straightList == []: return None
    else:
        highestStraight = straightList[0]
        for i in range(len(straightList)):
            cards = straightList[i]
            if cards[-1] > highestStraight[-1]:
                highestStraight = cards
        return highestStraight

#checks for a near straight from 4-card subsets
def isAlmostStraightFromSubsets(fourCardSubsets):
    straightList = []
    for i in range(len(fourCardSubsets)):
        cards = sortCards(fourCardSubsets[i])
        if isAlmostStraight(cards):
            return True

#recursively checks for a straight in a sorted set of five cards
def isStraight(cards):
    if len(cards) == 1: return True
    else:
        if cards[1].findValue()-cards[0].findValue() == 1:
            return isStraight(cards[1:])
        else: return False

def isSortedCards(cards):
    for i in range(len(cards)-1):
        if cards[i] > cards[i+1]: return False
    return True

def sortCards(cards):
    while not isSortedCards(cards):
        for i in range(len(cards)-1):
            if cards[i] > cards[i+1]:
                cards[i],cards[i+1] = cards[i+1],cards[i]
    return cards

#recursively checks for a near-straight in a sorted card list,
#used in AI card analysis if there are four cards,
#with no more than a 1 skip-space between them in total it returns true
def isAlmostStraight(cards,difference=0):
    if len(cards) == 1: return difference <= 1
    else:
        if cards[1].findValue()-cards[0].findValue() == 1: 
            return isAlmostStraight(cards[1:],difference=difference)
        elif cards[1].findValue()-cards[0].findValue() == 2:
            return isAlmostStraight(cards[1:],difference=difference+1)
        else: return False
        
#returns an ordered version of the subset
def makeStraight(cards):
    a = copy.copy(cards)
    result = []
    cardIn = True
    result.append(lowestCard(a))
    counter = 1
    while cardIn and counter < 5:
        cardIn = False
        lowCard=lowestCard(a)
        cardsOneUp = cardsOneUpFromAnotherCard(result[-1])
        for i in range(len(cardsOneUp)):
            if cardsOneUp[i] in a:
                result.append(cardsOneUp[i])
                cardIn = True
        a.remove(lowCard)
        counter += 1
        if not cardIn: return None
    return result

#returns lowest card in a list
def lowestCard(cards):
    lowCard = cards[0]
    for i in range(len(cards)):
        if cards[i] < lowCard: lowCard = cards[i]
    return lowCard

#returns the four suits of a single card
def cardsOneUpFromAnotherCard(card):
    valueIndex = card.findValue() + 1
    value = Card.values[valueIndex]
    result = []
    for suit in Card.suits:
        result.append(Card(value,suit))
    return result

def isStraightFlushFromSubsets(fiveCardSubsets):
    straightFlushList = []
    for i in range(len(fiveCardSubsets)):
        cards = makeStraight(fiveCardSubsets[i])
        if isStraight(fiveCardSubsets[i]) and isFlush(fiveCardSubsets[i]):
            straightFlushList.append(cards)
    if straightFlushList == []: return None
    else:
        highestStraightFlush = straightFlushList[0]
        for i in range(len(straightFlushList)):
            cards = straightFlushList[i]
            if cards[-1] > highestStraightFlush[-1]:
                highestStraightFlush = cards
        return highestStraightFlush
    
#test cases:   
#cards=[Card("8","Hearts"),Card("10","Hearts"),Card("9","Hearts"),Card("Jack","Hearts"),Card("Queen","Hearts")]
#cards1 = makeStraight(cards)
#print(cards1)
#print(isStraight(cards1))
