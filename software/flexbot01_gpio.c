// flexbot01_gpio.c custom C GPIO function code for L298N or HG7881 controlled 2WD robots with v7 flexbot PCB  
// developed by Enmore October 2019

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>   // added so that usleep(microseconds) can be used
#include <time.h>     // added to use standard time/date functions
#include <wiringPi.h> // include the wiringPi GPIO library
#include <softPwm.h>  // also include the WiringPi PWM library
#include "flexbot01_gpio.h"

// ****************************************************************
// this simple 'connection' function included for test purposes
// type void as nothing is returned
// ****************************************************************
//
void connect()
{
    printf("Connected to the flexbot01 C library...\n");

}

// ****************************************************************
// this random number function included for test purposes
// type int as it returns a random integer in the range 0-50
// ****************************************************************
//
int randNum()
{
    int nRand = rand() % 50; 
    return nRand;
}

// ****************************************************************
// simple GPIO function to use the Broadcom pin numbering
// ****************************************************************
void set_broadcom()
{
    // GPIO setup stuff:
    wiringPiSetupGpio();      // Initialize wiringPi -- using Broadcom pin numbers

}

// ****************************************************************
// simple GPIO function to set a pin to either INPUT or OUTPUT
// type = 0 means INPUT type = 1 means OUTPUT
// ****************************************************************
void setIO_GPIO(int pin_number, int type)
{
    if (type == 0)
        {
            pinMode(pin_number, INPUT);    // Set pin as input
        }
    else if (type == 1)
        {
            pinMode(pin_number, OUTPUT);    // Set pin as output
        }

}

// ***********************************************************************
// GPIO function to set the pull-up or pull-down resistor mode
// the pin must have previously been set to an input pin
// type = 0 means PUD_DOWN  type = 1 means PUD_UP  type = 9 means PUD_OFF
// ***********************************************************************
void set_pud(int in_pin, int type)
{
    if (type == 0)
        {
            pullUpDnControl (in_pin, PUD_DOWN) ;    // Set to PUD_DOWN
        }
    else if (type == 1)
        {
            pullUpDnControl (in_pin, PUD_UP) ;      // Set to PUD_UP
        }
    else if (type == 9)
        {
            pullUpDnControl (in_pin, PUD_OFF) ;     // Set to PUD_OFF
        }
}


// ****************************************************************
// simple GPIO function to set an OUTPUT pin to either HIGH or LOW
// state = 0 means LOW  state = 1 means HIGH
// ****************************************************************
void set_pin(int out_pin, int state)
{
    digitalWrite(out_pin, state) ;   // set the pin to the state value

}

// *******************************************************************
// simple GPIO function to set a pin to be software PWM
// just uses the standard int softPwmCreate function from  <softPwm.h>
// with a start value of 0 and a range of 100
// returns a value of 0 if successful
// *******************************************************************
int setPWM_GPIO(int pwm_pin)
{
    int pwm_result = softPwmCreate (pwm_pin, 0, 100)  ;   // set the pin to be PWM
    return pwm_result;

}

// **********************************************************************************
// simple GPIO function to update a previously created PWM pin with a new 0-100 value
// just uses the standard void softPwmWrite function from  <softPwm.h>
// **********************************************************************************
void set_pwm(int pwm_pin, int pwmvalue)
{
    softPwmWrite (pwm_pin, pwmvalue)  ;   // update the PWM value

}

// ****************************************************************
// simple GPIO function to read an INPUT pin as either HIGH or LOW
// state = 0 means LOW  state = 1 means HIGH
// ****************************************************************
int read_pin(int in_pin)
{
    return(digitalRead(in_pin)) ;   // return the read pin state value

}


// *******************************************************************
// send a sound pulse from the ultrasonic sensor using the Trigger pin
// the duration parameter is the pulse length in usecs
// ****************************************************************
void send_ultra(int trig, int duration, int debug)
{
    // Send duration-us pulse to trigger
    digitalWrite(trig, 1) ;   // set Trigger pin HIGH
    usleep(duration);
    digitalWrite(trig, 0) ;   // set Trigger pin LOW
	if (debug==1)
       {
           printf ("%2d usec pulse sent\n", duration);
       }
}


// **********************************************************************
// set ultrasonic sensor Trigger pin to a LOW state for a set duration
// used before sending a sound pulse to ensure the sound pulse is 'clean
// the duration parameter is the duration in usecs
// **********************************************************************
void setlow_ultra(int trig, int duration, int debug)
{
    // Send duration-us pulse to trigger
    digitalWrite(trig, 0) ;   // set Trigger pin LOW
    usleep(duration);
	if (debug==1)
        {
            printf ("%2d usec off period set\n", duration);
        }
}
 
//
// *****************************************************************************************
// simple routine to just check the ON/OFF slide switch state and return the swmode variable
// type int as it returns the swmode as a simple integer
// debug set to 1 gives additional outputs - but the routine is otherwise 'silent'
// **************************************************************************************
//
int check_onoff(int swmode_last, int debug, int onoff)
{
    // check for just the ON/OFF slide switch setting
    // swmode_last is a simple passed parameter of the current/last swmode setting
    // swmode = 0 means 'OFF' and swmode = 1 means 'ON'

	int swmode=10;  // initially set to a non-normal value

	int state_onoff = digitalRead(onoff);
    // if the on/off switch is low (=0), it's OFF
    if (state_onoff == 0)
    {
        if (swmode_last!=0 && debug==1)
        {
            printf("The on/off switch is now OFF \n");
            printf("slide switches set to IDLE mode \n");
        }
		swmode=0;    //  switch mode is OFF
    }
	
	else if (state_onoff == 1)
	{
        if (swmode_last!=1 && debug==1)
        {
            printf("The on/off switch is now ON \n");
            printf("slide switches set to an active mode for whatever opmode is set \n");
        }
		swmode=1;    //  switch mode is ON
    }

    return swmode; 

}
 
//
// **************************************************************************************
// routine to check slide switch state and change the opmode setting accordingly
// type int as it returns the opmode as a simple integer
//       opmode options:  simple integers as set out below
// switch state options:  state_onoff   state_AB   state_CD   state_EF are either 0 or 1
// debug set to 1 gives additional outputs - but the routine is otherwise 'silent'
// **************************************************************************************
//
int check_slideswitch(int opmode_last, int debug, int s_AB, int s_CD, int s_EF)
{
    // check for each slide switch setting
    // opmode_last is a simple passed parameter of the current/last opmode setting
    // opmode = 0 means 'idle' with the ON/OFF switch in the OFF position - but not checked here
    // opmode = 1 means ON + ACE
    // opmode = 2 means ON + BCE
    // opmode = 3 means ON + ADE
    // opmode = 4 means ON + ADF
    // opmode = 5 means ON + ACF
    // opmode = 6 means ON + BCF
    // opmode = 7 means ON + BDE
    // opmode = 8 means ON + BDF
    // opmode = 9 means an undefined operational mode

    int opmode=10;  // initially set to a non-normal value

    // read the current switch states
	int state_AB = digitalRead(s_AB);
    int state_CD = digitalRead(s_CD);
    int state_EF = digitalRead(s_EF);
	
    // Now check all the various switch state permutations
	
    // *** ON/OFF slide switch *** not checked here - now in a separate routine (see above)
    //     -------------------
       

    // *** ACE combination - opmode 1 ***
    //     --------------------------
    if (state_AB == 0 && state_CD == 0 && state_EF == 1)
	{
	    if (debug==1 && opmode_last != 1)
        {
            printf("slide switches set to 'ACE'- opmode 1 \n");
        }
        opmode=1;
	}

    // *** BCE combination - opmode 2 ***
    //     --------------------------
	else if (state_AB == 1 && state_CD == 0 && state_EF == 1)
	{
	    if (debug==1 && opmode_last != 2)
        {
            printf("slide switches set to 'BCE'- opmode 2 \n");
        }
        opmode=2;
	}

    // *** ADE combination - opmode 3 ***
    //     --------------------------
	else if (state_AB == 0 && state_CD == 1 && state_EF == 1)
	{
	    if (debug==1 && opmode_last != 3)
        {
            printf("slide switches set to 'ADE'- opmode 3 \n");
        }
        opmode=3;
	}

    // *** ADF combination - opmode 4 ***
    //     --------------------------
	else if (state_AB == 0 && state_CD == 1 && state_EF == 0)
	{
	    if (debug==1 && opmode_last != 4)
        {
            printf("slide switches set to 'ADF'- opmode 4 \n");
        }
        opmode=4;
	}

    // *** ACF combination - opmode 5 ***
    //     --------------------------
	else if (state_AB == 0 && state_CD == 0 && state_EF == 0)
	{
	    if (debug==1 && opmode_last != 5)
        {
            printf("slide switches set to 'ACF'- opmode 5 \n");
        }
        opmode=5;
	}

    // *** BCF combination - opmode 6 ***
    //     --------------------------
	else if (state_AB == 1 && state_CD == 0 && state_EF == 0)
	{
	    if (debug==1 && opmode_last != 6)
        {
            printf("slide switches set to 'BCF'- opmode 6 \n");
        }
        opmode=6;
	}

    // *** BDE combination - opmode 7 ***
    //     --------------------------
	else if (state_AB == 1 && state_CD == 1 && state_EF == 1)
	{
	    if (debug==1 && opmode_last != 7)
        {
            printf("slide switches set to 'BDE'- opmode 7 \n");
        }
        opmode=7;
	}

    // *** BDF combination - opmode 8 ***
    //     --------------------------
	else if (state_AB == 1 && state_CD == 1 && state_EF == 0)
	{
	    if (debug==1 && opmode_last != 8)
        {
            printf("slide switches set to 'BDF'- opmode 8 \n");
        }
        opmode=8;
	}

    // *** opmode 99 ***
    //     --------------------------
	else  // should never be here!!
	{
	    if (debug==1 && opmode_last != 99)
        {
            printf("slide switches set to an impossible combination! \n");
        }
        opmode=99;
	}

    return opmode;

}
