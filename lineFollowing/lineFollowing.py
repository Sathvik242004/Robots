#final code
from machine import Pin,PWM
import time
import utime


#light pin
led=Pin("LED",Pin.OUT)
for _ in range(3):
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
led.value(0)

#motor pins
Mot_A_Forward = Pin(18, Pin.OUT)
Mot_A_Back = Pin(19, Pin.OUT)
Mot_B_Forward = Pin(20, Pin.OUT)
Mot_B_Back = Pin(21, Pin.OUT)


#ir input
leftIp=Pin(16,Pin.IN)
rightIp=Pin(17,Pin.IN)

#frequency
#m1s.freq(1000)
#m2s.freq(1000)

#duty cycle
#m1s.duty_u16(65025)
#m2s.duty_u16(65025)


#moments

def forward():
    Mot_A_Forward.high()
    Mot_B_Forward.high()
    Mot_A_Back.low()
    Mot_B_Back.low()
    print("forward")
    
def backward():
    Mot_A_Forward.low()
    Mot_B_Forward.low()
    Mot_A_Back.high()
    Mot_B_Back.high()
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


#working
while True:
    rightval=rightIp.value()
    leftval=leftIp.value()
    
    print(rightIp.value(),leftIp.value())
    
    if rightval==0 and leftval==0:
        forward()
    elif rightval==0 and leftval==1:
        right()
    elif rightval==1 and leftval==0:
        left()
    elif rightval==1 and leftval==1:
        stop()



