import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.cleanup()

echo_right = 18
trig_right = 12

echo_left = 25
trig_left = 24

echo_front = 20
trig_front = 21 

GPIO.setmode(GPIO.BCM)

def frnt_dist():
    GPIO.setup(trig_front,GPIO.OUT)
    GPIO.setup(echo_front,GPIO.IN)
    GPIO.output(trig_front,False)
    time.sleep(0.2)
    GPIO.output(trig_front,True)
    time.sleep(0.00001)
    GPIO.output(trig_front,False)
    while GPIO.input(echo_front)==0:
        pulse_start=time.time()
    while GPIO.input(echo_front)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance_frnt=pulse_duration*17150
    distance_frnt=round(distance_frnt,2)
    return distance_frnt


def left_dist():
    GPIO.setup(trig_left,GPIO.OUT)
    GPIO.setup(echo_left,GPIO.IN)
    GPIO.output(trig_left,False)
    time.sleep(0.2)
    GPIO.output(trig_left,True)
    time.sleep(0.00001)
    GPIO.output(trig_left,False)
    while GPIO.input(echo_left)==0:
        pulse_start=time.time()
    while GPIO.input(echo_left)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance_left=pulse_duration*17150
    distance_left=round(distance_left,2)
    return distance_left

def right_dist():
    GPIO.setup(trig_right,GPIO.OUT)
    GPIO.setup(echo_right,GPIO.IN)
    GPIO.output(trig_right,False)
    time.sleep(0.2)
    GPIO.output(trig_right,True)
    time.sleep(0.00001)
    GPIO.output(trig_right,False)
    while GPIO.input(echo_right)==0:
        pulse_start=time.time()
    while GPIO.input(echo_right)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance_right=pulse_duration*17150
    distance_right=round(distance_right,2)
    return distance_right

from gpiozero import AngularServo

servo = AngularServo(5, min_pulse_width=0.0006, max_pulse_width=0.0023)                   
    
def turn_left(time):
    servo.angle = -35
    sleep(time)


    
def turn_right(time):
    servo.angle =30
    sleep(time)


def return_straight(time):
    servo.angle =-5
    sleep(time)
    
in1 = 2
in2 = 3
en = 4
temp1=1

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,100)

p.start(25)

def move_forward(speed):
    p.ChangeDutyCycle(speed)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    
def move_backward(speed):
    p.ChangeDutyCycle(speed)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    
def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    

return_straight(1)
while True:
    print(frnt_dist())
    move_forward(65)
    
    if frnt_dist()<15:
        move_backward(65)
        return_straight(1)
    
    if frnt_dist() <90 and frnt_dist()>15:
        stop()
        if left_dist() > right_dist():
            move_forward(65)
            turn_left(1.5)
            return_straight(0.5)
                    
        elif right_dist() > left_dist():
            move_forward(65)
            turn_right(1.5)
            return_straight(0.5)
        else:
            return_straight(0.1)
    else:
        return_straight(0.4)
