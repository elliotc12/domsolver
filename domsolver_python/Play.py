#!/usr/bin/python2.7

import Cards
import State

import copy

def hand_playable(state):
    return True

def play_turn(state, player):
    print play_actions(state)

def play_actions(state):
    possible_states = []
    if not hand_playable(state) or state.actions < 1:
        return [state]
    else:
        print state.hand
        for c in state.hand:
            print c
            if Cards.carddata[c].type == Cards.Types.ACTION:
                new_state = copy.deepcopy(state)
                new_state.discard(c)
                new_state.actions -= 1
                new_state.play(c)
                possible_states.extend(play_actions(new_state))
        return possible_states
