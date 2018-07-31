#!/usr/bin/env python

# The MIT License (MIT)
# Copyright (c) 2014 Alex Aquino dos Santos

# Technische Universität München (TUM)
# Autonomous Navigation for Flying Robots
# Homework 2.2 - 2D Odometry

import numpy as np
import math
from plot import plot_trajectory

class UserCode:
    def __init__(self):
        self.position = np.array([[0], [0]])
        self.yaw = 0

    def measurement_callback(self, t, dt, navdata):
        '''
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param navdata: measurements of the quadrotor
        '''

        d = navdata.vx * dt
        a = navdata.rotZ
        t = np.array([[d * math.cos(a)], [d * math.sin(a)]])
        self.position = self.position + t

        # update self.position by integrating measurements contained in navdata
        plot_trajectory("odometry", self.position)
