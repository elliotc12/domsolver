import Cards
import State

from copy import copy, deepcopy

class State:
    actions = 0
    buys = 0
    money = 0
    hand = 0
    bought = 0
    deck = []
    discard_pile = []
    temp = []

    def __init__(self, buys, actions, money, hand, bought, decklist):
        self.actions = actions
        self.buys = buys
        self.money = money
        self.hand = hand
        self.bought = bought
        self.deck = []
        self.discard_pile = []
        self.deck.extend(decklist)

    def draw(self):
        if len(self.deck) <= 0:
            if len(self.discard_pile) <= 0:
                return
            else:
                self.deck.extend(self.discard_pile) # TODO: shuffle
                self.discard_pile = []
        self.hand.append(self.deck.pop())

    def discard(self, card):
        if not card in self.hand:
            print "Attempting to discard card not in hand"
            exit()
        self.temp.append(card)
        self.hand.remove(card)

    def play(self, card):
        Cards.carddata[card].play(self)
