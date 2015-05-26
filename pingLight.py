import serial
import serial.tools.list_ports
import sys
import time
import ping
import subprocess
from array import *

SOLID_GREEN = '1'
SOLID_YELLOW = '2'
SOLID_RED = '3'
BLINK_RED = '4'
BLINK_YELLOW = '5'
BLINK_GREEN = '6'
BLINK_REDBLACK = '7'

good = 100 # maximum good ping 
bad = 250 # minimum bad ping 

host = "8.8.8.8"
timeout = 1
size = 32
foundArduino = False

def avgWithTimeout(pings):
    count = 0
    total = 0
    for ping in pings:
        if ping != 0.0:
            count += 1
            total += ping
    if count != 0:
        return total/count
    else:
        return 0.0


# Assumes only one Arduino is connected
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "Arduino" in p[1]:
        ser = serial.Serial(p[0], 115200)
        foundArduino = True

if not foundArduino:
    sys.exit("No Arduino found")

pings = array('d', [0,0,0])
currentPing = 0
avg = 0
hadATimeout = False

while True:
    time.sleep(2)
    line = ping.do_one(host, timeout, size)
    avgTimeout = False
    if line == None:
        line = 0
        hadATimeout = True
    line = line * 1000
    pings[currentPing] = line
    if pings[0] != 0.0 and pings[1] != 0.0 and pings[2] != 0.0:
        hadATimeout = False
    else:
        avg = avgWithTimeout(pings)

    currentPing = currentPing + 1
    if currentPing > 2:
        currentPing = 0
        avg = (pings[0] + pings[1] + pings[2]) / 3
        #print "average: " + str(avg)

        if avg == 0.0:
            ser.write(BLINK_REDBLACK) # blink red
            subprocess.call("zipReconnect.py", shell=True)
        elif hadATimeout and avg < good:
            ser.write(BLINK_GREEN)
        elif hadATimeout and avg > good and avg < bad:
            ser.write(BLINK_YELLOW)
        elif hadATimeout and avg > bad:
            ser.write(BLINK_RED)
        elif avg < good:
            ser.write(SOLID_GREEN) # solid green
        elif avg > good and avg < bad:
            ser.write(SOLID_YELLOW)
        else:
            ser.write(SOLID_RED) # solid red
