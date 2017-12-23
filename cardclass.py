import random
from tkinter import *
import copy

class Card(object):
    values = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    suits = ["Clubs","Diamonds","Hearts","Spades"]
    #initializes a card with a value and a suit
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    #generates a random card
    @staticmethod
    def generateCard():
        v = random.choice(Card.values)
        s = random.choice(Card.suits)
        return Card(v,s)

    #generates full deck
    @staticmethod
    def generateDeck():
        deck = []
        for value in Card.values:
            for suit in Card.suits:
                deck.append(Card(value,suit))
        random.shuffle(deck)
        return deck
    
    #draws a card
    def drawCard(self,canvas,cx,cy,data):
        w = 75
        h = 105
        image = self.getPlayingCardImage(data)
        canvas.create_image(cx,cy,image=image)
                    
    def getPlayingCardImage(self, data):
        suitName = self.suit[0].lower() # only car about first letter
        suitNames = "cdhsx"
        suit = suitNames.index(suitName)
        rank = self.findValue()+1
        if self.value == "Ace":
            rank = 1
        return data.cardImages[13*suit + rank]
        
    #repr function for printing out deck in order to debug
    def __repr__(self):
        return self.value + " of " + self.suit
        
    #redefining ==,<=,>=,<,> operators and creating similar methods
    #so that cards may be compared
    #static method to find an element in a list and return it
    def findSuit(self):
        suitIndex = 0
        for i in range(len(Card.suits)):
            if self.suit == Card.suits[i]:
                suitIndex = i
        return suitIndex
    def findValue(self):
        valueIndex = 0
        for i in range(len(Card.values)):
            if self.value == Card.values[i]:
                valueIndex = i
        return valueIndex
    def suitsEqual(self,other):
        if isinstance(other,Card): return self.suit == other.suit
    def valueEqual(self,other):
        if isinstance(other,Card): return self.value == other.value
    def completeEqual(self,other):
        if isinstance(other,Card):
            return valueEqual(self,other) and suitsEqual(self,other)
    #use index in Card.values to compare
    def __gt__(self,other):
        if isinstance(other,Card):
            if self.value == other.value:
                return self.findSuit() > other.findSuit()
            else: return self.findValue() > other.findValue()
    def __lt__(self,other):
        if isinstance(other,Card):
            if self.value == other.value:
                return self.findSuit() < other.findSuit()
            else: return self.findValue() < other.findValue()
    def __ge__(self,other):
        if isinstance(other,Card):
            if self.value == other.value:
                return self.findSuit() >= other.findSuit()
            else: return self.findValue() >= other.findValue()
    def __le__(self,other):
        if isinstance(other,Card):
            if self.value == other.value:
                return self.findSuit() <= other.findSuit()
            else: return self.findValue() <= other.findValue()
    def __sub__(self,other):
        if isinstance(other,Card):
            return self.findValue() - other.findValue()
    def __eq__(self,other):
        return self.suitsEqual(other) and self.valueEqual(other)
