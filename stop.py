#!/usr/bin/env python
import car_dir
import motor
import RPi.GPIO as GPIO
busnum = 1          # Edit busnum to 0, if you uses Raspberry Pi 1 or 0

car_dir.setup(busnum=busnum)
motor.setup(busnum=busnum)     # Initialize the Raspberry Pi GPIO connected to the DC motor. 
car_dir.home()
print ('Stopping racer')
motor.stop()
motor.setSpeed(24)