#!/usr/bin/python2.7

def hand_playable(state):
    return True

def play_turn(start_state, deck, player):
    if not hand_playable(start_state):
        return start_state
    else:
        print "playing turn"
