from fullcardanalysis import *
from cardclass import *
from playerclass import *

def dealFlop(data):
    data.deck.pop(0)
    data.deck.pop(0)
    data.deck.pop(0)
    data.river.append(data.deck.pop(0))
    data.river.append(data.deck.pop(0))
    data.river.append(data.deck.pop(0))

def dealTurn(data):
    data.deck.pop(0)
    data.river.append(data.deck.pop(0))

def dealRiver(data):
    data.deck.pop(0)
    data.river.append(data.deck.pop(0))

def allCheck(data):
    for player in data.players:
        if player.status != "fold":
            if player.turnstatus != "check": return False
    return True

def findStartingPlayer(data):
    for i in range(len(data.players)):
        if data.players[i].blindstatus == "big blind": return i

def isGameOver(data):
    counter = 0
    for player in data.players:
        if player.money != 0:
            counter += 1
    return counter == 1

def newTurn(data):
    data.drawRiver = False
    data.drawTurn = False
    data.drawFlop = False
    data.pot = 0
    data.potAtLastRound = 0
    for player in data.players:
        player.currentPlayerBet = 0
        player.money-250
        data.pot += 250
        player.status = "player"
        player.turnstatus = "check"
        player.drawCards = True
        player.revealCards = False
    data.deck = Card.generateDeck()
    for i in range(8):
        data.players[i].newHand(data.deck[i],data.deck[i+8])
        data.deck.pop(i)
        data.deck.pop(i+8)
    data.river = []
    data.river.append(data.deck.pop(0))
    data.river.append(data.deck.pop(0))
    data.river.append(data.deck.pop(0))
    data.submode = "flop"
    data.drawFlop = True

def getIndex(L,elem):
    for i in range(len(L)):
        if L[i] == elem: return i

def compareBestHands(data):
    playerIndex = 0
    bestHand = None
    bestHandType = None
    currentHand = []
    currentHandType = ""
    handTypes = ["high card","pair","two pair","three of a kind","straight","flush","full house","four of a kind", "straight flush"]
    for i in range(len(data.players)):
        if data.players[i].status != "fold":
            if bestHand == None and bestHandType == None:
                bestHand = data.players[i].bestHand
                bestHandType = data.players[i].handType
                playerIndex = i
            else:
                currentHandType=data.players[i].handType
                currentHand = data.players[i].bestHand
                if getIndex(handTypes,currentHandType)>getIndex(handTypes,bestHandType):
                    bestHandType = currentHandType
                    bestHand = currentHand
                    playerIndex = i
                elif currentHandType == bestHandType:
                    if currentHand[-1] > bestHand[-1]:
                        bestHandType = currentHandType
                        bestHand = currentHand
                        playerIndex = i
    return playerIndex
                    

def getBestHands(data):
    for player in data.players:
        player.bestHand,player.handType = cardAnalysis(player.pocket,data.river)
