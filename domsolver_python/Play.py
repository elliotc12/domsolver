import Cards
import State

import copy
import itertools

def my_deep_copy(state):
    new_deck = copy.deepcopy(state.deck)
    new_discard_pile = copy.deepcopy(state.discard_pile)
    new_temp = copy.deepcopy(state.temp)
    new_state = copy.deepcopy(state)
    new_state.deck = new_deck
    new_state.discard_pile = new_discard_pile
    new_state.temp = new_temp
    return new_state

def victory_points(state):
    pts = 0
    for c in state.hand:
        if Cards.carddata[c].type == Cards.Types.VICTORY:
            pts += Cards.carddata[c].points
    for c in state.deck:
        if Cards.carddata[c].type == Cards.Types.VICTORY:
            pts += Cards.carddata[c].points
    for c in state.discard_pile:
        if Cards.carddata[c].type == Cards.Types.VICTORY:
            pts += Cards.carddata[c].points
    return pts

def hand_playable(state):
    for c in state.hand:
        if Cards.carddata[c].type == Cards.Types.ACTION:
            return True
    return False

def play_actions(state):
    #print "playing action, actions: " + str(state.actions)  + " hand: " + str(state.hand) + " deck: " + str(state.deck) + " discard: " + str(state.discard_pile) + " temp: " + str(state.temp)
    if not hand_playable(state) or state.actions < 1:
        return [state]
    else:
        possible_states = []
        for c in state.hand:
            if Cards.carddata[c].type == Cards.Types.ACTION:
                new_state = my_deep_copy(state)
                new_state.discard(c)
                new_state.actions -= 1
                new_state.play(c)
                retval = play_actions(new_state)
                possible_states.extend(retval)
        return possible_states

def play_buys(states, player):
    best_score = 0
    best_state = None
    bought = []
    possible_buys = player.keys()
    for state in states:
        buying_power = state.money
        for c in state.hand:
            if Cards.carddata[c].type == Cards.Types.CURRENCY:
                buying_power += Cards.carddata[c].value
        purchase_options = []
        for i in range(1, state.buys+1):
            purchase_options.extend(
                list(itertools.combinations(possible_buys, i)))
        for option in purchase_options:
            cost = 0
            score = 0
            for o in option:
                cost += Cards.carddata[o].cost
                score += player[o]
            if buying_power >= cost and score > best_score:
                best_score = score
                best_state = state
                bought = option
    if bought != []:
        best_state.bought = bought
        return best_state
    else:
        return states[0]

def play_turn(state, player):
    possible_states = play_actions(state)
    state = play_buys(possible_states, player)
    state.discard_pile.extend(state.hand)
    state.discard_pile.extend(state.temp)
    state.discard_pile.extend(state.bought)
    state.hand = []
    state.bought = []
    state.temp = []
    state.actions = 1
    state.buys = 1
    state.money = 0
    for i in range (5):
        state.draw()
    return state
