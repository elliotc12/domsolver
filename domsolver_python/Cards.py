class Cards:
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
    def play(self, state):
        state.hand.append(state.draw())
        state.actions += 2
        return state

class Market:
    type = Types.ACTION
    cost = 5
    def play(self, state):
        state.hand.append(state.draw())
        state.actions += 1
        state.buys += 1
        state.money += 1
        return state

class Smithy:
    type = Types.ACTION
    cost = 4
    def play(self, state):
        state.hand.append(state.draw())
        state.hand.append(state.draw())
        state.hand.append(state.draw())
        return state

carddata = []
carddata.insert(Cards.COPPER,     Copper())
carddata.insert(Cards.SILVER,     Silver())
carddata.insert(Cards.GOLD,       Gold())
carddata.insert(Cards.ESTATE,     Estate())
carddata.insert(Cards.DUCHY,      Duchy())
carddata.insert(Cards.PROVINCE,   Province())
carddata.insert(Cards.VILLAGE,    Village())
carddata.insert(Cards.MARKET,     Market())
carddata.insert(Cards.SMITHY,     Smithy())
