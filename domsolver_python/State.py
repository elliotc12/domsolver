import Cards
import State

class State:
    actions = 0
    buys = 0
    money = 0
    hand = 0
    bought = 0
    deck = 0

    def __init__(self, buys, actions, money, hand, bought, decklist):
        self.actions = actions
        self.buys = buys
        self.money = money
        self.hand = hand
        self.bought = bought
        self.deck = self.Deck(decklist)

    class Deck:
        deck = []
        discard_pile = []
        def __init__(self, cardlist):
            self.deck.extend(cardlist)
        def discard(self, card):
            self.discard_pile.append(card)

    def draw(self):
        if len(self.deck.deck) <= 0:
            print "shuffling discard into deck"
            self.deck.deck.extend(self.deck.discard_pile)
            self.deck.discard_pile = []
        new = self.deck.deck.pop()
        print "adding to hand " + str(new)
        self.hand.append(new)

    def play(self, card):
        Cards.carddata[card].play(self)

    def discard(self, card):
        if not card in self.hand:
            print "Attempting to discard card not in hand"
            exit()
        self.deck.discard(card)
        self.hand.remove(card)
