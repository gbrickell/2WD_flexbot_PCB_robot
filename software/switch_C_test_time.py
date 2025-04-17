#!/usr/bin/python
# 

# command to run:  python3 /home/pi/L298N_flexbot01/switch_C_test_time.py



###################################################################################
#
#  main code
#
###################################################################################

import time # Import the Time library
import datetime

# allow C libraries to be used
from ctypes import *

# for GPIO functions the custom C library is used which uses the wiringPi functions
flexbot01_gpio = CDLL("/home/pi/L298N_flexbot01/libflexbot01_gpio.so")
#call C function to check connection to gpio C library
flexbot01_gpio.connect() 
# set the Broadcom pin numbering
flexbot01_gpio.set_broadcom()

debug = 1   # outputs more info to the screen: set to 0 once code is in production use

# Set variables slide switches connected to the GPIO pins
onoff = 9
AB = 11
CD = 10
EF = 22
print (" slide switch GPIOs: " + str(onoff) + " - " + str(AB) + " - " + str(CD) + " - " + str(EF) )


# set the slide switch pins as INPUT
flexbot01_gpio.setIO_GPIO(onoff, 0)
flexbot01_gpio.setIO_GPIO(AB, 0)
flexbot01_gpio.setIO_GPIO(CD, 0)
flexbot01_gpio.setIO_GPIO(EF, 0)

# set initial switch states to something undefined so that the program checks can run from the start
state_onoff = 2
state_AB = 2
state_CD = 2
state_EF = 2

# get an initial swmode and opmode setting
global swmode   # swmode variable set as global just in case
global opmode   # opmode variable set as global just in case
opmode = 0      # initial opmode 
opmode_last = 9
printstatus = "yes"  # set initial condition

loop = 0

# initially send a swmode_last and 'opmode_last' of 10 that is 'impossible'
swmode = flexbot01_gpio.check_onoff(10, debug, onoff)
opmode = flexbot01_gpio.check_slideswitch(10, debug, AB, CD, EF)


start_time = datetime.datetime.now()
try:
    #repeat the next indented block forever
    print ("program started")
    while True:
        loop = loop + 1
        opmode = flexbot01_gpio.check_slideswitch(opmode, debug, AB, CD, EF)
        swmode = flexbot01_gpio.check_onoff(swmode, debug, onoff)
        #elapsed = datetime.datetime.now() - start_time
        #print ("elapsed ms: " + str(int(elapsed.total_seconds()*1000)) )
        #print ("loop - opmode: " + str(loop) + " - " +str(opmode) )
        #print (" ")

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    elapsed = datetime.datetime.now() - start_time
    print ("program stopped")
    print ("elapsed ms: " + str(int(elapsed.total_seconds()*1000)) )
    print ("loop - opmode - swmode: " + str(loop) + " - " +str(opmode)  + " - " +str(swmode) )
    print (" ")

