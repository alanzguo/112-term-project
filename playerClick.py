import random
from rungameLogic import *
from aicardanalysis import *

def playerClick(event,data):
    player = data.players[0]
    x,y = event.x,event.y
    data.drawFlop == True
    if isGameOver(data):
        data.mode = "gameover"
        pass
    if ((y-(data.height-125))**2+(x-data.width//2)**2)**(1/2) < 20 and data.currentBet+data.currentRoundBet<player.money:
        data.currentBet += 250
    if ((y-(data.height-75))**2+(x-data.width//2)**2)**(1/2) < 20 and data.currentBet > 0:
        data.currentBet -= 250
    if y<data.height-80 and y>data.height-120 and x>data.width//2+35 and x<data.width//2+145 and data.currentRoundBet+data.currentBet<=player.money and player.currentroundofbetting < 2:
        player.money -= (data.currentBet+data.currentBetToCall)
        data.pot += (data.currentBet + data.currentBetToCall)
        data.currentBetToCall = data.currentBet
        player.currentPlayerBet = data.currentBet
        data.currentBet = 0
        for players in data.players:
            if players.status == "player":
                players.turnstatus = "call"
        player.turnstatus = "check"
        data.AIIsPlaying = True
        data.timer = 0
        data.currentRoundBet = 0
        player.currentroundofbetting += 1
    elif y<data.height-80 and y>data.height-120 and x>data.width//2+175 and x<data.width//2+285:
        data.pot += abs(data.currentBetToCall-player.currentPlayerBet)
        player.money -= abs(data.currentBetToCall-player.currentPlayerBet)
        player.currentPlayerBet = data.currentBetToCall
        player.turnstatus = "check"
        player.currentroundofbetting += 1
        data.AIIsPlaying = True
        data.timer = 0
    elif y<data.height-80 and y>data.height-120 and x>data.width//2+315 and x<data.width//2+425:
        player.turnstatus = "check"
        player.currentroundofbetting += 1
        data.AIIsPlaying = True
        data.timer = 0
        data.potAtLastRound = data.currentRoundBet
    elif y<data.height-80 and y>data.height-120 and x<data.width//2-35 and x>data.width//2-145:
        player.status = "fold"
        player.currentroundofbetting += 1
        data.AIIsPlaying = True
        data.timer = 0
        data.potAtLastRound = data.currentRoundBet
        
def changeModes(data):
    if data.submode=="flop" and allCheck(data):
        data.currentBetToCall = 0
        data.players[0].currentroundofbetting = 0
        dealTurn(data)
        data.submode = "turn"
        data.drawTurn = True
    elif data.submode == "turn" and allCheck(data):
        data.currentBetToCall = 0
        data.players[0].currentroundofbetting = 0
        dealRiver(data)
        data.submode = "river"
        data.drawRiver = True
        for player in data.players:
            player.revealCards = True
    elif data.submode == "river" and allCheck(data):
        data.currentBetToCall = 0
        data.players[0].currentroundofbetting = 0
        for players in data.players:
            players.currentPlayerBet = 0
        getBestHands(data)
        winner = compareBestHands(data)
        data.players[winner].money += data.pot
        newTurn(data)
        for player in data.players:
            player.revealCards = False

def runAITurns(data):
    for player in data.players[1:]:
        if player.status != "fold":
            AITurn(player,data)
    changeModes(data)

def AITurn(AI,data):
    raiseLevel = AICardAnalysis(AI.pocket,data.river,data.submode)
    if raiseLevel == None or raiseLevel == "low":
        if AI.turnstatus == "check":
            AI.turnstatus = "check"
            AI.lastMove = "check"
        elif data.currentBetToCall <= 500 and AI.turnstatus == "call":
            data.pot += data.currentBetToCall
            AI.money -= data.currentBetToCall
            AI.turnstatus = "check"
            AI.currentPlayerBet = data.currentBetToCall
            AI.lastMove = "call"
        else:
            AI.status = "fold"
            AI.lastMove = "fold"
            AI.drawCards = False
    else:
        AIMakeBetBasedOnCardAnalysis(AI,data,raiseLevel)

def AIMakeBetBasedOnCardAnalysis(AI,data,betLevel):
    bet = 0
    if betLevel == "very high": bet,margin = random.choice([3500,3250,3000,2750,2500]),5000
    elif betLevel == "high": bet,margin = random.choice([2500,2250,2000,1750,1500]),1000
    elif betLevel == "mid": bet,margin = random.choice([1250,1000,750]),1000
    elif betLevel == "low": bet,margin = random.choice([500,250]),750
    if AI.turnstatus == "check" and data.players[0].currentroundofbetting < 2:
        if data.currentBetToCall == 0:
            data.currentBetToCall = bet
            data.pot += bet
            AI.money -= bet
            for players in data.players:
                players.turnstatus = "call"
            AI.turnstatus = "check"
            AI.currentPlayerBet = bet
            AI.lastMove = "raise"
    elif AI.turnstatus == "call":
        if data.players[0].currentroundofbetting == 1:
            if data.currentBetToCall < bet and data.currentBetToCall > 0:
                data.currentBetToCall = bet
                data.pot += bet
                AI.money -= bet
                for players in data.players:
                    players.turnstatus = "call"
                AI.turnstatus = "check"
                AI.currentPlayerBet = bet
                AI.lastMove = "raise"
            elif data.currentBetToCall > bet and data.currentBetToCall-bet<=margin:
                data.pot += data.currentBetToCall
                AI.money -= data.currentBetToCall
                AI.turnstatus = "check"
                AI.currentPlayerBet = data.currentBetToCall
                AI.lastMove = "call"
        elif data.players[0].currentroundofbetting != 1:
            if data.currentBetToCall > bet and data.currentBetToCall-bet<=margin:
                data.pot += data.currentBetToCall-AI.currentPlayerBet
                AI.money -= data.currentBetToCall-AI.currentPlayerBet
                AI.turnstatus = "check"
                AI.currentPlayerBet = data.currentBetToCall
                AI.lastMove = "call"
            else:
                AI.status = "fold"
                AI.lastMove = "fold"
                AI.drawCards = False

def helpMousePressed(event,data):
    x,y=event.x,event.y
    if x < data.width-35 and x > data.width-165 and y>30 and y<70:
        data.mode = "gameplay"

def splashMousePressed(event,data):
    x,y=event.x,event.y
    if x<data.width//3+115 and x>data.width//3-115 and y<data.height//2+40 and y>data.height//2-40:
        data.mode = "gameplay"
    elif x<data.width*2//3+115 and x>data.width*2//3-115 and y<data.height//2+40 and y>data.height//2-40:
        data.mode = "helpscreen"

