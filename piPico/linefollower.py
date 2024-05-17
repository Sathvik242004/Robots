from machine import Pin, PWM
import time
import utime
import _thread


# Light pin
led = Pin("LED", Pin.OUT)
for _ in range(3):
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
led.value(0)

# Motor pins
Mot_A_Forward = Pin(18, Pin.OUT)
Mot_A_Back = Pin(19, Pin.OUT)
Mot_B_Forward = Pin(20, Pin.OUT)
Mot_B_Back = Pin(21, Pin.OUT)

# IR input
leftIp = Pin(16, Pin.IN)
rightIp = Pin(17, Pin.IN)

#record the path

def record(k):
    global lc,c
    if k==lc:
        c+=1
        print("executed",lc,k,c)
    else:
        f=open("log.txt",'a+')
        saveLine=lc+","+str(c)+"\n"
        f.write(saveLine)
        print(saveLine)
        f.close()
        lc,c=k,0
        print("recorded",lc,k,c)
        


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



def main():
    #record
    print("recording")
    rightval = rightIp.value()
    leftval = leftIp.value()
    print(rightIp.value(), leftIp.value())

    if rightval == 0 and leftval == 0:
        forward()
        record('f')
    elif rightval == 0 and leftval == 1:
        right()
        record('r')
    elif rightval == 1 and leftval == 0:
        left()
        record('l')
    elif rightval == 1 and leftval == 1:
        stop()
        record('s')
stop()
print("i am out of the loop")

sLock= _thread.allocate_lock()
def secondThread():
    sLock.acquire()
    count=0;
    while True:
        sleep(0.5)
        count+=0.5
        #clock with precition 0.5
        print("program started",count,"ago")
        sLock.release()
_thread.start_new_thread(secondThread,())


if __name__=="__main__":
    sLock.acquire()
    lc='hello'
    c=0
    print("from 1st")
    while True:
        main()
    stop()
    sLock.release()
    


        
