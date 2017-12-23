from cardclassfortermproject import *
#PLAYER class   
class Player(object):
    #initializes a player with a pocket,given two cards
    def __init__(self,card1,card2,name):
        self.pocket = []
        self.pocket.append(card1)
        self.pocket.append(card2)
        self.money = 10000
        self.status = "player"
        self.turnstatus = "check"
        self.blindstatus = "no blind"
        self.currentPlayerBet = 0
        self.name = name

    #makes a bet, adds the money to the pot and subtracts from the players
    #available money
    def makeBet(self,bet,pot):
        pot += bet
        self.money -= pot
        
    #a function that sets the player's status to fold and empties his hand
    def playerFold(self):
        self.pocket = []
        self.status = "folded"

    #function that calls the current bet
    def playerCall(self,pot,currentTurnBet,currentPlayerBet):
        self.money -= (currentBet-currentPlayerBet)
        pot += (currentTurnBet-currentPlayerBet)
        self.turnstatus = "check"
        
    @staticmethod
    def newHand():
        result = []
        deck = Card.generateDeck()
        for i in range(0,8):
            result.append(Player(deck[i],deck[i+8],"player"+str(i+1)))
            deck.pop(i)
            deck.pop(i+8)
        flop = []
        deck.pop(0)
        deck.pop(0)
        deck.pop(0)
        flop.append(deck.pop(0))
        flop.append(deck.pop(0))
        flop.append(deck.pop(0))
        return result,deck,flop

    def __repr__(self):
        p = self.name+": "+repr(self.pocket[0])+", "+repr(self.pocket[1])
        return "{"+p+"}"
