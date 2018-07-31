#!/usr/bin/env python

# The MIT License (MIT)
# Copyright (c) 2014 Alex Aquino dos Santos

# Technische Universität München (TUM)
# Autonomous Navigation for Flying Robots
# Homework 1.1

import quadrotor.command as cmd
from math import sqrt

def plan_mission(mission):

    commands  = [
        cmd.up(1.0),            # cmd.up: move x meters up
        cmd.left(2.0),          # cmd.left: move x meters to the left
        cmd.forward(6.0),       # cmd.forward: move x meters forward
        cmd.right(2.0),         # cmd.right: move x meters to the right
        cmd.backward(6.0),      # cmd.backward: move x meters backward
        cmd.right(2.0),
        cmd.forward(6.0),
        cmd.left(2.0),
        cmd.backward(6.0)
    ]

    mission.add_commands(commands)
