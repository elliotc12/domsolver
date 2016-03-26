#!/usr/bin/python2.7

import Cards
import State
import Play

init_state = State.State(1, 1, 0,
                         [Cards.Cards.COPPER,
                          Cards.Cards.COPPER,
                          Cards.Cards.COPPER,
                          Cards.Cards.VILLAGE,
                          Cards.Cards.MARKET],
                         [],
                         [Cards.Cards.COPPER,
                          Cards.Cards.SILVER,
                          Cards.Cards.GOLD])

player = {}
player[Cards.Cards.ESTATE] = 0.1
player[Cards.Cards.DUCHY] = 0.3
player[Cards.Cards.PROVINCE] = 0.6

Play.play_turn(init_state, player)
