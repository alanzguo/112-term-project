from cardclass import *

#determines the highest card from a set of cards
def highCard(cards):
    highestCard = cards[0]
    for i in range(len(cards)):
        if cards[i] > highestCard:
            highestCard = cards[i]
    return highestCard
