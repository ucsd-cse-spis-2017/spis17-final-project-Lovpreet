##import collections
##import itertools
##import random
##
##suits = ("Hearts", "Spades", "Clubs", "Diamonds")
##ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
##
##class card():
##    def __init__(self,rank,suit):
##        self.rank = rank
##        self.suit = suit
##        self.card = self.rank, self.suit
##        return self.rank + "of" + self.suit
##
##
##    
##class poker_hand():
##    def __init__ (self, card_list):
##        self.card_list = card_list
##
##class hand_type():
##    def __init__ (self, 
##
##


import collections
import itertools
import random

SUIT_LIST = ("Hearts", "Spades", "Diamonds", "Clubs")
NUMERAL_LIST = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

#Identifies cards

##class card:
##    def __init__(self, numeral, suit):
##        self.numeral = numeral
##        self.suit = suit
##        self.card = self.numeral, self.suit
##    def __repr__(self):
##        return self.numeral + "-" + self.suit
##
###Identifies hands
##
##class poker_hand():
##    def __init__(self, card_list):
##        self.card_list = card_list
##    def __repr__(self):
##        short_desc = "Nothing."
##        numeral_dict = collections.defaultdict(int)
##        suit_dict = collections.defaultdict(int)
##        for my_card in self.card_list:
##            numeral_dict[my_card.numeral] += 1
##            suit_dict[my_card.suit] += 1
##        # Pair
##        if len(numeral_dict) == 4:
##            short_desc = "One pair."
##        # Two pair or 3-of-a-kind
##        elif len(numeral_dict) == 3:
##            if 3 in numeral_dict.values():
##                short_desc ="Three-of-a-kind."
##            else:
##                short_desc ="Two pair."
##        # Full house or 4-of-a-kind
##        elif len(numeral_dict) == 2:
##            if 2 in numeral_dict.values():
##                short_desc ="Full house."
##            else:
##                short_desc ="Four-of-a-kind."
##        else:
##            # Flushes and straights
##            straight, flush = False, False
##            if len(suit_dict) == 1:
##                flush = True
##            min_numeral = min([NUMERAL_LIST.index(x) for x in numeral_dict.keys()])
##            max_numeral = max([NUMERAL_LIST.index(x) for x in numeral_dict.keys()])
##            if int(max_numeral) - int(min_numeral) == 4:
##                straight = True
##            # Ace can be low
##            low_straight = set(("Ace", "2", "3", "4", "5"))
##            if not set(numeral_dict.keys()).difference(low_straight):
##                straight = True
##            if straight and not flush:
##                short_desc ="Straight."
##            elif flush and not straight:
##                short_desc ="Flush."
##            elif flush and  straight:
##                short_desc ="Straight flush."
##        enumeration = "/".join([str(x) for x in self.card_list])
##        return "{enumeration} ({short_desc})".format(**locals())
##
###Adds cards to deck and creates random hands
##
##class deck(set):
##    def __init__(self):
##        for numeral, suit in itertools.product(NUMERAL_LIST, SUIT_LIST):
##            self.add(card(numeral, suit))
##    def get_card(self):
##        a_card = random.sample(self, 1)[0]
##        self.remove(a_card)
##        return a_card
##    def get_hand(self, number_of_cards=5):
##        if number_of_cards == 5:
##            return poker_hand([self.get_card() for x in range(number_of_cards)])
##
##
##for i in range(1):
##    first_hand = (deck().get_hand())
##    print(first_hand)

##score == 0

class card:
    def __init__(self, numeral, suit):
        self.numeral = numeral
        self.suit = suit
        self.card = self.numeral, self.suit
    def __repr__(self):
        return self.numeral + "-" + self.suit

#Identifies hands

class poker_hand():
    def __init__(self, card_list):
        self.card_list = card_list
    def __repr__(self):
        short_desc = "Nothing."
        numeral_dict = collections.defaultdict(int)
        suit_dict = collections.defaultdict(int)
        for my_card in self.card_list:
            numeral_dict[my_card.numeral] += 1
            suit_dict[my_card.suit] += 1
        # Pair
        if len(numeral_dict) == 4:
            short_desc = "One pair."
        # Two pair or 3-of-a-kind
        elif len(numeral_dict) == 3:
            if 3 in numeral_dict.values():
                short_desc ="Three-of-a-kind."
            else:
                short_desc ="Two pair."
        # Full house or 4-of-a-kind
        elif len(numeral_dict) == 2:
            if 2 in numeral_dict.values():
                short_desc ="Full house."
            else:
                short_desc ="Four-of-a-kind."
        else:
            # Flushes and straights
            straight, flush = False, False
            if len(suit_dict) == 1:
                flush = True
            min_numeral = min([NUMERAL_LIST.index(x) for x in numeral_dict.keys()])
            max_numeral = max([NUMERAL_LIST.index(x) for x in numeral_dict.keys()])
            if int(max_numeral) - int(min_numeral) == 4:
                straight = True
            # Ace can be low
            low_straight = set(("Ace", "2", "3", "4", "5"))
            if not set(numeral_dict.keys()).difference(low_straight):
                straight = True
            if straight and not flush:
                short_desc ="Straight."
            elif flush and not straight:
                short_desc ="Flush."
            elif flush and  straight:
                short_desc ="Straight flush."
        enumeration = "/".join([str(x) for x in self.card_list])
        return "{enumeration} ({short_desc})".format(**locals())


class deck(set):
    def __init__(self):
        num = 0
        for numeral in NUMERAL_LIST:
            for suit in SUIT_LIST:
                num += 1
                self.add(card(numeral, suit))
                if(num == 52):
                    break
                
    def get_card(self):
        a_card = random.sample(self, 1)[0]
        self.remove(a_card)
        return a_card
    def add_card(self, card):
        self.add(card)
    def get_hand(self):
        return poker_hand([self.get_card() for x in range(5)])
    def get_opponent_hand(self):
        '''return all combinations of 5 cards'''
        possibilities = []

        
        for i in range (2000):
            temp = []
            for i in range (5):
                c = self.get_card()
                temp.append(c)
            
            possibilities.append(temp)
            for i in temp:
                self.add_card(i)

        return possibilities

newDeck = deck()
myHand = newDeck.get_hand()
opponent_hand = newDeck.get_opponent_hand()
print(opponent_hand)
        

















    
 
