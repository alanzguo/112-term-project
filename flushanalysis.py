#analyzes five-card subsets for the presence of a "flush", or five cards of
#the same suit
from cardclass import *

def isFlushFromSubsets(fiveCardSubsets):
    for i in range(len(fiveCardSubsets)):
        cards = fiveCardSubsets[0]
        if isFlush(cards): return cards
    return None

#given five cards, determines whether or not a flush exists [recursively]
def isFlush(cards):
    if len(cards) == 1: return True
    else:
        if cards[0].suit == cards[1].suit:
            return isFlush(cards[1:])
        else: return False
        
#test cases
#cards=[Card("3","Hearts"),Card("Ace","Hearts"),Card("5","Hearts"),
#       Card("Jack","Hearts"),Card("Queen","Diamonds")]
#assert(not isFlush(cards))
#cards=[Card("3","Hearts"),Card("Ace","Hearts"),Card("5","Hearts"),
#       Card("Jack","Hearts"),Card("Queen","Hearts")]
#assert(isFlush(cards))
