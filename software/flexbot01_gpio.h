void connect();
int randNum();
void set_broadcom();
void setIO_GPIO(int pin_number, int type);
void set_pud(int in_pin, int type);
void set_pin(int out_pin, int state);
int setPWM_GPIO(int pwm_pin);
void set_pwm(int pwm_pin, int pwmvalue);
int read_pin(int in_pin);
void send_ultra(int trig, int duration, int debug);
void setlow_ultra(int trig, int duration, int debug);
int check_onoff(int onoff_last, int debug, int onoff);
int check_slideswitch(int opmode_last, int debug, int s_AD, int s_BE, int s_CF);






