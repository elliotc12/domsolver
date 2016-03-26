#!/usr/bin/python2.7

import Cards
import State
import Play
import Plot

import numpy as np

data = []

player = {}
player[Cards.Cards.SILVER]   = 0.4
player[Cards.Cards.GOLD]     = 0.6
player[Cards.Cards.PROVINCE] = 0.7

xmax = 0.8
ymax = 0.8

init_state = State.State(1, 1, 0,
                        [Cards.Cards.COPPER, Cards.Cards.COPPER, Cards.Cards.COPPER,
                         Cards.Cards.ESTATE, Cards.Cards.ESTATE],
                         [],
                         [Cards.Cards.COPPER, Cards.Cards.COPPER, Cards.Cards.COPPER,
                          Cards.Cards.COPPER, Cards.Cards.ESTATE])

for x in np.arange(0.1,xmax, 0.2):
    for y in np.arange(0.1,ymax, 0.2):
        player[Cards.Cards.MARKET] = x
        player[Cards.Cards.VILLAGE] = y
        print [x,y]
        for _ in range(20):
            init_state = Play.play_turn(init_state, player)
        data.append([player[Cards.Cards.MARKET],
                     player[Cards.Cards.VILLAGE], Play.victory_points(init_state)])

Plot.plot(data, xmax, ymax)
