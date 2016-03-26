#!/usr/bin/python2.7

import Cards
import State
import Play
import Plot

import numpy as np

data = []

for i in range (1,10):
    player = {}
    player[Cards.Cards.SILVER]   = i/10.0
    player[Cards.Cards.GOLD]     = 1.0 - i/10.0
    player[Cards.Cards.MARKET]   = 0.5
    player[Cards.Cards.PROVINCE] = 0.7

    init_state = State.State(1, 1, 0,
                         [Cards.Cards.COPPER, Cards.Cards.COPPER, Cards.Cards.COPPER,
                          Cards.Cards.ESTATE, Cards.Cards.ESTATE],
                         [],
                         [Cards.Cards.COPPER, Cards.Cards.COPPER, Cards.Cards.COPPER,
                          Cards.Cards.COPPER, Cards.Cards.ESTATE])

    for _ in range(20):
        init_state = Play.play_turn(init_state, player)

    data.append([i/10.0, 1.0-i/10.0, Play.victory_points(init_state)])

Plot.plot(data, "Silver Preference", "Gold Preference")
