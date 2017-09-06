import collections
import itertools
import random

SUIT_LIST = ("Hearts", "Spades", "Diamonds", "Clubs")
NUMERAL_LIST = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
SCORE_DICT = {"2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7, "10":8, "Jack": 9, "Queen":10, "King":11, "Ace":12}
HAND_DICT = {"Nothing.": 0, "One pair.": 1, "Two pair.": 2, "Three-of-a-kind.": 3, "Straight.": 4, "Flush.": 5, "Full house.":6, "Four-of-a-kind.": 7, "Straight flush.":8, "Royal flush":9}
#if SCORE_DICT["2"] < SCORE_DICT["King"]

def generate_all_cards(myHand):
    all_cards = []
    for suit in SUIT_LIST:
        for numeral in NUMERAL_LIST:
            if myHand[0].numeral == numeral and myHand[0].suit == suit or\
            myHand[1].numeral == numeral and myHand[1].suit == suit or\
            myHand[2].numeral == numeral and myHand[2].suit == suit or\
            myHand[3].numeral == numeral and myHand[3].suit == suit or\
            myHand[4].numeral == numeral and myHand[4].suit == suit:
                continue
            else:
                all_cards.append(card(numeral,suit))
    return all_cards
#Identifies cards
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
        self.short_desc = None
        
    def calculate(self):
        self.short_desc = "Nothing."
        numeral_dict = collections.defaultdict(int)
        suit_dict = collections.defaultdict(int)
        for my_card in self.card_list:
            numeral_dict[my_card.numeral] += 1
            suit_dict[my_card.suit] += 1
        # Pair
        if len(numeral_dict) == 4:
            self.short_desc = "One pair."
        # Two pair or 3-of-a-kind
        elif len(numeral_dict) == 3:
            if 3 in numeral_dict.values():
                self.short_desc ="Three-of-a-kind."
            else:
                self.short_desc ="Two pair."
        # Full house or 4-of-a-kind
        elif len(numeral_dict) == 2:
            if 2 in numeral_dict.values():
                self.short_desc ="Full house."
            else:
                self.short_desc ="Four-of-a-kind."
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
                self.short_desc ="Straight."
            elif flush and not straight:
                self.short_desc ="Flush."
            elif flush and  straight:
                self.short_desc ="Straight flush."

    def __repr__(self):
        enumeration = "/".join([str(x) for x in self.card_list])
        return "{enumeration} ({self.short_desc})".format(**locals())

#Creates deck
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

        
        for i in range (10):
            temp = []
            for i in range (5):
                c = (self.get_card())
                temp.append(c)
            possibilities.append(poker_hand(temp))
            for i in temp:
                self.add_card(i)

        return possibilities
#Finds biggest value in a hand*
def get_biggest_card_value(hand):
    """ Find the biggest card in a hand"""
    card_list = hand.card_list
    myBiggestNumber = 0
    for i in range (5):
        if SCORE_DICT[card_list[i].numeral] > myBiggestNumber:
            myBiggestNumber = SCORE_DICT[card_list[i].numeral]
    return myBiggestNumber
#Finds best hand between opponents
def get_better_hand(myHand, opponent_hand):
    score = 0
    """Find the better hand out of yours and the opponents"""
    if HAND_DICT[myHand.short_desc] > HAND_DICT[opponent_hand.short_desc]:
        score = score + 1
    elif HAND_DICT[myHand.short_desc] == 0 & HAND_DICT[opponent_hand.short_desc] == 0:
        if get_biggest_card_value(myHand) > get_biggest_card_value(opponent_hand):
            score = score + 1
        elif get_biggest_card_value(myHand) == get_biggest_card_value(opponent_hand):
            score = score + (1/2)
    elif HAND_DICT[myHand.short_desc] == HAND_DICT[opponent_hand.short_desc]:
        score = score + (1/2)
    return score

score = 0
newDeck = deck()
myHand = newDeck.get_hand()
opponent_hand = newDeck.get_opponent_hand()
myHand.calculate()
all_cards = generate_all_cards(myHand.card_list)

possible_combinations = []
for i in range(len(all_cards)):
    for j in range(i+1, len(all_cards)):
        for k in range(j+1, len(all_cards)):
            for m in range(k+1, len(all_cards)):
                for n in range(m+1, len(all_cards)):
                    possible_combinations.append( poker_hand( [all_cards[i], all_cards[j], all_cards[k], all_cards[m], all_cards[n] ] ) )
for i in range(len(possible_combinations)):
    possible_combinations[i].calculate()
    score = score + get_better_hand(myHand, possible_combinations[i])
print (myHand)
##print (score)


hand_strength = score/len(possible_combinations)
##print (hand_strength)


#Pot odds are always going to be 33%
pot_odds = .333
RR = hand_strength/pot_odds
print (RR)

#Returns action
if 0.0 < RR < 1.0:
    if random.randint (1, 100) <=95:
        print("Fold")
    elif random.randint (1, 100) >95:
        print("Raise")
    
if 1.0 < RR < 2.0:
    if random.randint (1, 100) <=80:
        print("Fold")
    elif random.randint (1, 100) >80>85:
        print("Call")
    elif random.randint (1, 100) >=85:
        print("Raise")
if 2.0 < RR < 3.0:
    if random.randint (1, 100) >=60:
        print("Call")
    elif random.randint (1, 100) <60:
        print("Raise")
elif RR > 3.0: 
    if random.randint (1, 100) >=30:
        print("Call")
    elif random.randint (1, 100) <30:
        print("Raise")












    
 
