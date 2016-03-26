class State:
    def __init__(self, buys, actions, money, hand, bought, decklist):
        self.actions = actions
        self.buys = buys
        self.money = money
        self.hand = hand
        self.bought = bought
        self.deck = self.Deck(decklist)

    class Deck:
        def __init__(self, cardlist):
            self.deck.extend(cardlist)
        def discard(card):
            discard.append(card)
        deck = []
        discard = []

    actions = 0
    buys = 0
    money = 0
    hand = 0
    bought = 0
    deck = 0

    def draw(self):
        self.hand.append(self.deck.deck.pop())

    def play(self, card):
        print "play a card"
