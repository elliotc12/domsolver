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

Play.play_turn(init_state, 0)
