#!/usr/bin/python2.7

import Cards
import State
import Play

init_state = State.State(1, 1, 0,
                         [Cards.Names.COPPER,
                          Cards.Names.COPPER,
                          Cards.Names.COPPER],
                         [],
                         [Cards.Names.COPPER,
                          Cards.Names.SILVER,
                          Cards.Names.GOLD])
