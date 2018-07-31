#!/usr/bin/env python

# The MIT License (MIT)
# Copyright (c) 2014 Alex Aquino dos Santos

# Technische Universität München (TUM)
# Autonomous Navigation for Flying Robots
# Homework 2.1

from plot import plot

class UserCode:
    def __init__(self):
        # initialize data you want to store in this object between calls to the measurement_callback() method
        self.last_yaw_velocity = 0
        self.max_roll_angle    = 0
        self.max_pitch_angle   = 0
        self.max_yaw_velocity  = 0

    def measurement_callback(self, t, dt, navdata):
        '''
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param navdata: measurements of the quadrotor
        '''

        # add your plot commands here
        self.max_roll_angle = max(self.max_roll_angle, abs(navdata.rotX))
        self.max_pitch_angle = max(self.max_pitch_angle, abs(navdata.rotY))
        self.max_yaw_velocity = max(self.max_yaw_velocity, abs((navdata.rotZ - self.last_yaw_velocity) / dt))
        self.last_yaw_velocity = navdata.rotZ

        plot("max_roll_angle", self.max_roll_angle)
        plot("max_pitch_angle", self.max_pitch_angle)
        plot("max_yaw_velocity", self.max_yaw_velocity)
