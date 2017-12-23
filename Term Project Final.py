# ALAN GUO
# TERM PROJECT: "TEXAS HOLD 'EM GAME & AI IMPLEMENTATION"
# MENTOR: Matthew Salim

#importing modules and other files
import random
from tkinter import *
from cardclass import *
from playerclass import *
from fullcardanalysis import *
from drawing import *
from rungameLogic import *
from playerClick import *


def init(data):
    data.players,data.deck,data.river = Player.newPlayers()
    data.playerBet = False
    data.turnEnd = False
    data.reveal = False
    data.turns = 0
    data.ante = 250
    data.pot = 2000
    data.drawFlop = True
    data.drawTurn = False
    data.drawRiver = False
    data.mode = "splashscreen"
    data.submode = "flop"
    data.betround = 1
    data.playerTurn = True
    data.currentBet = 0
    data.currentRoundBet = 0
    data.timer = 0
    data.AIIsPlaying = False
    data.potAtLastRound = 0
    data.currentBetToCall = 0
    data.cardImages = []
    data.helpText="""The goals of this game of Texas Hold'Em are to bet,
based on the cards you have received and the five public cards (called the "river"),
aiming to win as much money as possible in a from your opponents,
who are intelligent, decision-capable AI.


For reference, here is a list of the hands, in best order:
1. Straight Flush: five cards of the same suit, in consecutive order of value
2. Four-of-a-Kind: four cards of the same value
3. Full House: a three-of-a-kind and a pair, of differing values
4. Flush: five cards of the same suit
5. Straight: five cards in ascending consecutive order of value
6. Three-of-a-Kind: three cards of the same value
7. Two Pair: two pairs of differing values
8. Pair: two cards of equal value
9. High Card: the single highest card available

Good luck, and may the odds be ever in your favor!"""

#this and similar functions adapted from demo
def loadPlayingCardImages(data):
    cards = 55
    for card in range(cards):
        rank = (card%13)+1
        suit = "cdhsx"[card//13]
        filename = "playing-card-gifs/%s%d.gif" % (suit, rank)
        data.cardImages.append(PhotoImage(file=filename))
    filename = "playing-card-gifs/x1.gif"
    data.cardImages.append(PhotoImage(file=filename))

def playerMousePressed(event,data):
    playerClick(event,data)

def mousePressed(event, data):
    if data.mode == "gameplay": playerMousePressed(event,data)
    if data.mode == "splashscreen": splashMousePressed(event,data)
    if data.mode == "helpscreen": helpMousePressed(event,data)

def keyPressed(event, data):
    if event.keysym == "h" and data.mode == "gameplay":
        data.mode = "helpscreen"
    elif event.keysym == "h" and data.mode == "helpscreen":
        data.mode = "gameplay"
    pass

def timerFired(data):
    if data.mode == "gameplay": gameTimerFired(data)

def gameTimerFired(data):
    data.timer += 1
    if data.timer == 2 and data.AIIsPlaying:
        if data.players[0].status == "player":
            data.AIIsPlaying = False
            runAITurns(data)
        elif data.players[0].status == "fold":
            if data.submode == "flop":
                data.players[0].currentroundofbetting = 1
                runAITurns(data)
                if allCheck(data):
                    changeModes(data)
                else:
                    data.players[0].currentroundofbetting += 1
                    runAITurns(data)
                    changeModes(data)
            if data.submode == "turn":
                data.players[0].currentroundofbetting = 1
                runAITurns(data)
                if allCheck(data):
                    changeModes(data)
                else:
                    data.players[0].currentroundofbetting += 1
                    runAITurns(data)
                    changeModes(data)
                data.players[0].currentroundofbetting = 1
            if data.submode == "river":
                if allCheck(data):
                    changeModes(data)
                else:
                    data.players[0].currentroundofbetting += 1
                    runAITurns(data)
                    changeModes(data)
                    data.reveal = True
                    data.timer = 0
                    for player in data.players:
                        player.revealCards = True
                data.players[0].currentroundofbetting = 1
    if data.reveal:
        for player in data.players:
            player.revealCards = True
    if data.reveal and data.timer == 2:
        for player in data.players:
            player.revealCards = False
        data.reveal = False
            

def redrawAll(canvas, data):
    if data.mode == "gameplay": drawGameScreen(canvas,data)
    if data.mode == "splashscreen": drawSplashScreen(canvas,data)
    if data.mode == "helpscreen": drawHelpScreen(canvas,data)

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.height, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerdelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    root.title("Texas Hold'Em")
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    loadPlayingCardImages(data)
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

def playTexasHoldem():
    run(1800, 1000)

playTexasHoldem()
