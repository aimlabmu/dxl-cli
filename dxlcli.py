#!/home/pi/miniconda3/bin/python

import sys
import time
from ax12 import Ax12

class BasicController:
    '''
    Class to control basic functions of  motor on Rpi.
    '''
    def __init__(self, scanLimit=20, defaultSpeed=90):
        self.connection = Ax12()
        self.connected_motor_ids = []
        self.scan_limit = scanLimit
        self.default_speed = defaultSpeed

    ###########################
    # Get Connected Motor Ids #
    ###########################

    def getConnectIds(self):
        self.connected_motor_ids = self.connection.learnServos()
        print("Available ids are", self.connected_motor_ids)

    ####################
    # Position Control #
    ####################

    def setPositionOf(self, motor_id, pos=512, speed=90):
        self.connection.moveSpeed(motor_id, pos, speed=speed)

    def setPositionAll(self, pos=512, speed=90):
        for motorId in self.connected_motor_ids:
            self.connection.moveSpeed(motorId, pos, speed)

    def getPositionOf(self, motor_id):
        return self.connection.readPosition(motor_id)

    def getPositionAll(self):
        temp = {}
        for motorId in self.connected_motor_ids:
            temp[motorId] = self.connection.readPosition(motorId)

        return temp

    ####################
    # Torque Control #
    ####################

    def setTorqueOf(self, motor_id, status):
        self.connection.setTorqueStatus(motor_id, status)

    def setTorqueAll(self, status):
        for motorId in self.connected_motor_ids:
            self.connection.setTorqueStatus(motorId, status)

    def setTorqueLimitOf(self, motor_id, torque):
        self.connection.setTorqueLimit(motor_id, torque)

    def setTorqueLimitAll(self, torque):
        for motorId in self.connected_motor_ids:
            self.connection.setTorqueLimit(motorId, torque)

    ####################
    # Resetting Error #
    ####################

    def resetOverloadErrorOf(self, motor_id):
        self.setTorqueLimitOf(motor_id, 1023)
        self.setTorqueOf(motor_id, 0)