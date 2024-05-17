#code following
from machine import Pin, PWM
from time import sleep
import utime

# Light pin
led = Pin("LED", Pin.OUT)
for _ in range(3):
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)
led.value(0)

# Motor pins
Mot_A_Forward = Pin(18, Pin.OUT)
Mot_A_Back = Pin(19, Pin.OUT)
Mot_B_Forward = Pin(20, Pin.OUT)
Mot_B_Back = Pin(21, Pin.OUT)

# IR input

#record the path

# Define movement functions
def forward():
    Mot_A_Forward.low()
    Mot_B_Forward.low()
    Mot_A_Back.high()
    Mot_B_Back.high()
    print("forward")


def backward():
    Mot_A_Forward.high()
    Mot_B_Forward.high()
    Mot_A_Back.low()
    Mot_B_Back.low()
    print("backward")


def left():
    Mot_A_Forward.high()
    Mot_B_Forward.low()
    Mot_A_Back.low()
    Mot_B_Back.high()
    print("left")


def right():
    Mot_A_Forward.low()
    Mot_B_Forward.high()
    Mot_A_Back.high()
    Mot_B_Back.low()
    print("right")


def stop():
    Mot_A_Forward.low()
    Mot_B_Forward.low()
    Mot_A_Back.low()
    Mot_B_Back.low()
    print("stop")
    
    
    
def execute():
    f=open('log.txt','r+')
    lines=f.readlines()
    for line in lines:
        value,freq=line.split(',')
        freq=int(freq)
        print(value,freq)
        if freq>0 and value=='s':
            stop()
            sleep(freq//1000)
        elif  freq>0 and value=='l':
            left()
            sleep(freq//1000)
        elif  freq>0 and value=='r':
                right()
                sleep(freq//1000)
        elif  freq>0 and value=='f':
                forward()
                sleep(freq//1000)
            
        
            
        
        
        
        
if __name__=="__main__":
    execute()
    stop()
    print("Completed")
