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

    def __init__(self, buys, actions, money, hand, bought, decklist):
        self.actions = actions
        self.buys = buys
        self.money = money
        self.hand = hand
        self.bought = bought
        self.deck.extend(decklist)

    def draw(self):
        if len(self.deck) > 0:
            self.hand.append(self.deck.pop())

    def discard(self, card):
        if not card in self.hand:
            print "Attempting to discard card not in hand"
            exit()
        self.discard_pile.append(card)
        self.hand.remove(card)

    def play(self, card):
        Cards.carddata[card].play(self)
