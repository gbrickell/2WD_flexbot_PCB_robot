#!/usr/bin/python

# L298N_speed_test01.py python code for the L298N motor controller test rig
# command to run: python3 /home/pi/L298N_flexbot01/L298N_speed_test01.py

# simple set of test routines for the motor speed functions using the L298N motor controller

#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# Raspberry Pi L298N more developed PWM motor functions but based upon the article at 
#  http://www.instructables.com/id/Control-DC-and-stepper-motors-with-L298N-Dual-Moto/
#  which describes the L298N motor controller use with an Arduino Uno
# 
#  N.B. depending upon how the motors are connected the motor direction
#    signals to the in1, in2, in3 and in4 pins may need to be adjusted
#
#  enA is usually the right hand motor and enB the left hand motor
#
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

def motor_pwm(leftright, dutycycle):   # a more generic function for individual motor control
    dutycycle = int(dutycycle) # force as an integer just in case
    # individual motor control with a +'ve or -'ve dutycycle to set the motor forwards or backwards
    if leftright == "left":  # left motor is motor A
        if dutycycle == 0:   # stop the moter
            # motor braking
            # set enA with 100% PWM dutycycle
            pwm_enA.start(100)
            # set in1 off and in2 off i.e. LOW- LOW for no motion
            GPIO.output(in1, 0)
            GPIO.output(in2, 0)
        elif dutycycle > 0:  # move forwards
            # set enA with the PWM dutycycle
            pwm_enA.start(dutycycle)
            # set in1 on and in2 off i.e. HIGH - LOW for forward motion
            GPIO.output(in1, 1)
            GPIO.output(in2, 0)
        elif dutycycle < 0:  # move backwards
            # set enA with the PWM dutycycle
            pwm_enA.start(abs(dutycycle))
            # set in1 on and in2 off i.e. LOW - HIGH for backward motion
            GPIO.output(in1, 0)
            GPIO.output(in2, 1)

    elif leftright == "right":  # right motor is motor B
        if dutycycle == 0:   # stop the moter
            # motor braking
            # set enB with 100% PWM dutycycle
            pwm_enB.start(100)
            # set in1 off and in2 off i.e. LOW- LOW for no motion
            GPIO.output(in3, 0)
            GPIO.output(in4, 0)
        elif dutycycle > 0:  # move forwards
            # set enB with the PWM dutycycle
            pwm_enB.start(dutycycle)
            # set in3 on and in4 off - i.e. HIGH - LOW for forward motion
            GPIO.output(in3, 1)
            GPIO.output(in4, 0)
        elif dutycycle < 0:  # move backwards
            # set enB with the PWM dutycycle
            pwm_enB.start(abs(dutycycle))
            # set in3 off and in4 on i.e. LOW - HIGH for backward motion
            GPIO.output(in3, 0)
            GPIO.output(in4, 1)

        else: #wrong motor type set
            print ("motor_pwm function: wrong motor type set")
            print (" ")

def forward_pwm(dutycycleA, dutycycleB):   # a simple both motors forward function
    # separate duty cycles are set so that each motor can be fine tuned if they vary in performance
    #print ("forward " + str(dutycycleA) + " - " +str(dutycycleB))
    # set enA with the PWM dutycycle
    pwm_enA.start(dutycycleA)
    # set in1 on and in2 off i.e. HIGH - LOW for forward motion
    GPIO.output(in1, 1)
    GPIO.output(in2, 0)
    # set enB with the PWM dutycycle
    pwm_enB.start(dutycycleB)
    # set in3 on and in4 off 
    GPIO.output(in3, 1)
    GPIO.output(in4, 0)
 
def backward_pwm(dutycycleA, dutycycleB):  # a simple both motors backward function
    #print ("backward " + str(dutycycleA) + " - " +str(dutycycleB))
    # set enA with the PWM dutycycle
    pwm_enA.start(dutycycleA)
    # set in1 off and in2 on i.e. LOW - HIGH for backward motion
    GPIO.output(in1, 0)
    GPIO.output(in2, 1)
    # set enB with the PWM dutycycle
    pwm_enB.start(dutycycleB)
    # set in3 off and in4 on i.e. LOW - HIGH for backward motion
    GPIO.output(in3, 0)
    GPIO.output(in4, 1)

def Right_pwm(dutycycle):   # go Right continuously - left motor fwd & right motor off
    #print ("turn Right continuously" + " - " +str(dutycycle))
    # set enA with the passed PWM dutycycle
    pwm_enA.start(dutycycle)
    # set in1 on and in2 off i.e. HIGH - LOW for forward motion
    GPIO.output(in1, 1)
    GPIO.output(in2, 0)
    # set enB with 0% PWM dutycycle
    pwm_enB.start(0)
    # set in3 off and in4 off i.e. LOW - LOW for no motion
    GPIO.output(in3, 0)
    GPIO.output(in4, 0)

def Left_pwm(dutycycle):   # go Left continuously - right motor fwd & left motor off
    #print ("turn Left " + " - " +str(dutycycle))
    # set enA with 0% PWM dutycycle
    pwm_enA.start(0)
    # set in1 off and in2 off i.e. LOW - LOW for no motion
    GPIO.output(in1, 0)
    GPIO.output(in2, 0)
    # set enB with the passed PWM dutycycle
    pwm_enB.start(dutycycle)
    # set in3 on and in4 off - HIGH - LOW for forward motion 
    GPIO.output(in3, 1)
    GPIO.output(in4, 0)

def RightSpin_pwm(dutycycleA, dutycycleB):   # spin Right continuously - left motor fwd & right motor back
    #print ("Right-spin " + " - " +str(dutycycleA) + " - " +str(dutycycleB))
    # set enA with the passed PWM dutycycle
    pwm_enA.start(dutycycleA)
    # set in1 on and in2 off i.e. HIGH - LOW for forward motion
    GPIO.output(in1, 1)
    GPIO.output(in2, 0)
    # set enB with the passed PWM dutycycle
    pwm_enB.start(dutycycleB)
    # set in3 off and in4 on i.e. LOW - HIGH for backward motion
    GPIO.output(in3, 0)
    GPIO.output(in4, 1)

def LeftSpin_pwm(dutycycleA, dutycycleB):   # spin Left continuously - left motor back & right motor fwd
    #print ("spin Left " + " - " +str(dutycycleA) + " - " +str(dutycycleB))
    # set enA with the passed PWM dutycycle
    pwm_enA.start(dutycycleA)
    # set in1 off and in2 on i.e. LOW - HIGH for backward motion
    GPIO.output(in1, 0)
    GPIO.output(in2, 1)
    # set enB with the passed PWM dutycycle
    pwm_enB.start(dutycycleB)
    # set in3 on and in4 off i.e. HIGH - LOW for forward motion
    GPIO.output(in3, 1)
    GPIO.output(in4, 0)
 
def stop_pwm(mode):   # two options to stop both motors NB the mode must be passed as a string
    if mode == "brake":
        #print ("brake stop")
        # motor braking
        # set enA with 100% PWM dutycycle
        pwm_enA.start(100)
        # set in1 off and in2 off i.e. LOW- LOW for no motion
        GPIO.output(in1, 0)
        GPIO.output(in2, 0)
        # set enB with 100% PWM dutycycle
        pwm_enB.start(100)
        # set in3 off and in4 off i.e. LOW- LOW for no motion
        GPIO.output(in3, 0)
        GPIO.output(in4, 0)

    elif mode == "coast":
        #print ("coast stop")
        # coasting
        # set enA with 0% PWM dutycycle
        pwm_enA.start(0)
        # set in1 off and in2 off i.e. LOW- LOW for no motion
        GPIO.output(in1, 0)
        GPIO.output(in2, 0)
        # set enB with 0% PWM dutycycle
        pwm_enB.start(0)
        # set in3 off and in4 off i.e. LOW- LOW for no motion
        GPIO.output(in3, 0)
        GPIO.output(in4, 0)
 
def turnRight_pwm(turn_time, dutycycle):   # run left motor fwd & right motor off for a set time
    #print ("turn Right " + str(turn_time) + " - " +str(dutycycle))
    # set enA with the passed PWM dutycycle
    pwm_enA.start(dutycycle)
    # set in1 on and in2 off i.e. HIGH - LOW for forward motion
    GPIO.output(in1, 1)
    GPIO.output(in2, 0)
    # set enB with 0% PWM dutycycle
    pwm_enB.start(0)
    # set in3 off and in4 off i.e. LOW - LOW for no motion
    GPIO.output(in3, 0)
    GPIO.output(in4, 0)
    time.sleep(turn_time) # only run the motors for the set amount of turn_time seconds
    stop_pwm("brake")     # stop the motors after the turn
 
def turnLeft_pwm(turn_time, dutycycle):   # run right motor fwd & left motor off for a set time
    #print ("turn Left " + str(turn_time) + " - " +str(dutycycle))
    # set enA with 0% PWM dutycycle
    pwm_enA.start(0)
    # set in1 off and in2 off i.e. LOW - LOW for no motion
    GPIO.output(in1, 0)
    GPIO.output(in2, 0)
    # set enB with the passed PWM dutycycle
    pwm_enB.start(dutycycle)
    # set in3 on and in4 off i.e. HIGH - LOW for forward motion
    GPIO.output(in3, 1)
    GPIO.output(in4, 0)
    time.sleep(turn_time) # only run the motors for the set amount of turn_time seconds
    stop_pwm("brake")     # stop the motors after the turn
 
def spinRight_pwm(spin_time, dutycycleA, dutycycleB):   # run left motor fwd & right motor back for a set time
    #print ("spin Right " + str(spin_time) + " - " +str(dutycycleA) + " - " +str(dutycycleB))
    # set enA with the passed PWM dutycycle
    pwm_enA.start(dutycycleA)
    # set in1 on and in2 off i.e. HIGH - LOW for forward motion
    GPIO.output(in1, 1)
    GPIO.output(in2, 0)
    # set enB with the passed PWM dutycycle
    pwm_enB.start(dutycycleB)
    # set in3 off and in4 on i.e. LOW - HIGH for backward motion
    GPIO.output(in3, 0)
    GPIO.output(in4, 1)
    time.sleep(spin_time) # only run the motors for the set amount of spin_time seconds
    stop_pwm("brake")     # stop the motors after the spin
   
def spinLeft_pwm(spin_time, dutycycleA, dutycycleB):   # run left motor back & right motor fwd for a set time
    #print ("spin Left " + str(spin_time) + " - " +str(dutycycleA) + " - " +str(dutycycleB))
    # set enA with the passed PWM dutycycle
    pwm_enA.start(dutycycleA)
    # set in1 off and in2 on i.e. LOW - HIGH for backward motion
    GPIO.output(in1, 0)
    GPIO.output(in2, 1)
    # set enB with the passed PWM dutycycle
    pwm_enB.start(dutycycleB)
    # set in3 on and in4 off i.e. HIGH - LOW for forward motion
    GPIO.output(in3, 1)
    GPIO.output(in4, 0)
    time.sleep(spin_time) # only run the motors for the set amount of spin_time seconds
    stop_pwm("brake")     # stop the motors after the spin


 

#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# main code
#
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import RPi.GPIO as GPIO # Import the GPIO Library
import time             # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)  # this is normally the default but it is set here explicitly
GPIO.setwarnings(False) # avoids the display of GPIO usage warnings

# L298N setup code using the RPi GPIO libary
# Define Outputs from RPi to L298N - variable names are as per the L298N pin labels
enA = 14   # this will be a software set PWM pin
in1 = 15   
in2 = 18  
enB = 25   # this will be a software set PWM pin
in3 = 23  
in4 = 24
# Set the L298N GPIO Pin modes - all set as OUTPUTs using the RPi GPIO libary
GPIO.setup(enA, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

# PWM parameters
# How many times to turn the GPIO pin on and off each second 
Frequency = 20

# How long the GPIO pin stays on each cycle, as a percent  
# Setting the duty cycle to 0 means the motors will not turn
DutyCycleA = 50
DutyCycleB = 50

pwm_enA = GPIO.PWM(enA, Frequency)  # set the enA pin as a software set PWM pin
pwm_enB = GPIO.PWM(enB, Frequency)  # set the enB pin as a software set PWM pin
# Start the software PWM pins with a duty cycle of 0 (i.e. motors not moving)
pwm_enA.start(0)
pwm_enB.start(0)

#print ("*** PWM initialised - but no motor rotation")

##########################
###     motor tests    ###
##########################

print ("*** drive motor A & B forward for 3 seconds")
forward_pwm(DutyCycleA, DutyCycleB)
time.sleep(3)

print ("*** stop both motors")
stop_pwm("coast")
time.sleep(3)

print ("*** drive motor A & B backward for 3 seconds")
backward_pwm(DutyCycleA, DutyCycleB)  
time.sleep(3)

print ("*** turn right by driving motor B forward continuously for 3 seconds")
Right_pwm(DutyCycleB)  
time.sleep(3)

print ("*** turn left by driving motor A forward continuously for 3 seconds")
Left_pwm(DutyCycleA)  
time.sleep(3)

print ("*** spin right by driving motor A forward & motor B backward continuously for 3 seconds")
RightSpin_pwm(DutyCycleA, DutyCycleB)  
time.sleep(3)

print ("*** spin left by driving motor A backward & motor B forward continuously for 3 seconds")
LeftSpin_pwm(DutyCycleA, DutyCycleB)  
time.sleep(3)

print ("*** turn right by driving motor B forward for a set time")
turnRight_pwm(2, DutyCycleB)  

print ("*** turn left by driving motor A forward for a set time")
turnLeft_pwm(2, DutyCycleA)


print ("*** testing finished ***")

stop_pwm("brake")


