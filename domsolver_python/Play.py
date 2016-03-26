import Cards
import State

import copy
import itertools

def my_deep_copy(state):
    new_deck = copy.deepcopy(state.deck)
    new_discard_pile = copy.deepcopy(state.discard_pile)
    new_state = copy.deepcopy(state)
    new_state.deck = new_deck
    new_state.discard_pile = new_discard_pile
    return new_state

def hand_playable(state):
    for c in state.hand:
        if Cards.carddata[c].type == Cards.Types.ACTION:
            return True
    return False

def play_turn(state, player):
    possible_states = play_actions(state)
    best_score = 0
    bought = []
    possible_buys = player.keys()
    for state in possible_states:
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
                bought = option
    print bought

def play_actions(state):
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
