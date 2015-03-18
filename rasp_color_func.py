__author__ = 'MauroNew'
#!/usr/bin/env python

import time
import os

STEP = 1
DELAY = 0.01

def pwm(pin, angle):
    cmd = "echo " + str(pin) + "=" + str(angle) + " > /dev/pi-blaster"
    os.system(cmd)
    time.sleep(DELAY)

while True:
    pwm(2,1)
    #blue to green
    for j in range(128, 256, STEP):
        pwm(0,j/255.0)
        pwm(1,1 - ((j-128)/255.0))
    #green to red
    for j in range(128, 256, STEP):
        pwm(1,j/255.0)
        pwm(2,1 - ((j-128)/255.0))
    #red to blue
    for j in range(0, 128, STEP):
        pwm(0,1 - (j/255.0))
        pwm(2,(j+128)/255.0)
