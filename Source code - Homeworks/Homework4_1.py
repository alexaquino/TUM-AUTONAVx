#!/usr/bin/env python

# The MIT License (MIT)
# Copyright (c) 2014 Alex Aquino dos Santos

# Technische Universität München (TUM)
# Autonomous Navigation for Flying Robots
# Homework 4.1

class UserCode:
    def __init__(self):
        # tune gains
        self.Kp = 150
        self.Kd = 31.5
        self.Last_x = 0

    def compute_control_command(self, t, dt, x_measured, x_desired):
        '''
        param t: time since simulation start
        param dt: time since last call to compute_control_command
        param x_measured: measured position (scalar)
        param x_desired: desired position (scalar)
        return - control command u
        '''
        # implement PD controller
        up = self.Kp * (x_desired - x_measured)
        ud = self.Kd * (0 - (x_measured - self.Last_x) / dt)
        self.Last_x = x_measured
        u = up + ud
        return u
