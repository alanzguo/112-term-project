from cardclass import *
#PLAYER class   
class Player(object):
    #initializes a player with a pocket,given two cards
    def __init__(self,card1,card2,name):
        self.pocket = []
        self.pocket.append(card1)
        self.pocket.append(card2)
        self.money = 9750
        self.status = "player"
        self.turnstatus = "check"
        self.blindstatus = "no blind"
        self.currentPlayerBet = 0
        self.name = name
        self.bestHand = []
        self.handtype = ""
        self.currentroundofbetting = 0
        self.drawCards = True
        self.revealCards = False
        self.lastMove = ""

    #makes a bet, adds the money to the pot and subtracts from the players
    #available money
    def makeBet(self,roundbet,bet,pot):
        actualBet = bet + roundbet
        pot += actualBet
        self.money -= actualBet
        
    #a function that sets the player's status to fold and empties his hand
    def playerFold(self):
        self.status = "fold"

    #function that calls the current bet
    def playerCall(self,pot,currentTurnBet,currentPlayerBet):
        self.money -= (currentTurnBet-currentPlayerBet)
        pot += (currentTurnBet-currentPlayerBet)
        self.turnstatus = "check"

    def newHand(self,card1,card2):
        self.pocket = []
        self.pocket.append(card1)
        self.pocket.append(card2)

    def bestHand(self,L,handType):
        self.handType = handType
        self.bestHand = L

    def drawPlayerCards(self,canvas,cx,cy,data):
        self.pocket[0].drawCard(canvas,cx-50,cy,data)
        self.pocket[1].drawCard(canvas,cx+50,cy,data)

    def drawPlayerCardBacks(self,canvas,cx,cy,data):
        image = data.cardImages[-1]
        canvas.create_image(cx-50,cy,image=image)
        canvas.create_image(cx+50,cy,image=image)

    @staticmethod
    def newPlayers():
        result = []
        deck = Card.generateDeck()
        for i in range(0,8):
            result.append(Player(deck[i],deck[i+8],"player"+str(i+1)))
            deck.pop(i)
            deck.pop(i+8)
        flop = []
        deck = deck[3:]
        flop.append(deck.pop(0))
        flop.append(deck.pop(0))
        flop.append(deck.pop(0))
        return result,deck,flop

    @staticmethod
    def newTurn(players):
        deck = Card.generateDeck()
        for player in players:
            player.newHand(deck[i],deck[i+8])
            deck.pop(i)
            deck.pop(i+8)
        flop = []
        deck = deck[3:]
        flop.append(deck.pop(0))
        flop.append(deck.pop(0))
        return flop

    def __repr__(self):
        p = self.name+": "+repr(self.pocket[0])+", "+repr(self.pocket[1])
        return "{"+p+"}"

class AI(Player):
    pass
