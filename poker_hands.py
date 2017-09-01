import collections
import itertools
import random

suit = ("Hearts", "Spades", "Clubs", "Diamonds")
rank = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "King", "Queen", "Ace")

class card():
    def __init__(slef,rank,suit):
        self.rank = rank
        self.suit = suit
        self.card = self.rank, self.suit
    def __    __(self):
        return self.rank + "of" + self.suit


    
##class poker_hand():
##    def __init__ (self, card_list):
##        self.card_list = card_list
