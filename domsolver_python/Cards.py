class Names:
    [COPPER, SILVER, GOLD, ESTATE, DUCHY, PROVINCE, VILLAGE, MARKET, SMITHY] = range(9)

class Types:
    ACTION, CURRENCY, VICTORY = range(3)

class Copper:
    type = Types.CURRENCY
    cost = 0
    value = 1

class Silver:
    type = Types.CURRENCY
    cost = 3
    value = 2

class Gold:
    type = Types.CURRENCY
    cost = 6
    value = 3

class Estate:
    type = Types.VICTORY
    cost = 2
    points = 1

class Duchy:
    type = Types.VICTORY
    cost = 5
    points = 3

class Province:
    type = Types.VICTORY
    cost = 8
    points = 6

class Village:
    type = Types.ACTION
    cost = 3
    def play(state):
        state.hand.append(state.deck.draw())
        state.actions += 2
        return state

class Market:
    type = Types.ACTION
    cost = 5
    def play(state):
        state.hand.append(state.deck.draw())
        state.actions += 1
        state.buys += 1
        state.money += 1
        return state

class Smithy:
    type = Types.ACTION
    cost = 4
    def play(state):
        state.hand.append(state.deck.draw())
        state.hand.append(state.deck.draw())
        state.hand.append(state.deck.draw())
        return state

cards = []
cards.insert(Names.COPPER,     Copper())
cards.insert(Names.SILVER,     Silver())
cards.insert(Names.GOLD,       Gold())
cards.insert(Names.ESTATE,     Estate())
cards.insert(Names.DUCHY,      Duchy())
cards.insert(Names.PROVINCE,   Province())
cards.insert(Names.VILLAGE,    Village())
cards.insert(Names.MARKET,     Market())
cards.insert(Names.SMITHY,     Smithy())
