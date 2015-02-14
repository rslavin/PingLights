import serial
import serial.tools.list_ports
import sys
import time
import ping
from array import *

good = 100
bad = 250

host = "8.8.8.8"
timeout = 1
size = 32
foundArduino = False

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
    if line == None:
        line = 0
        hadATimeout = True
    line = line * 1000
    pings[currentPing] = line
    if pings[0] != 0.0 and pings[1] != 0.0 and pings[2] != 0.0:
        hadATimeout = False
    currentPing = currentPing + 1
    if currentPing > 2:
        currentPing = 0
        avg = (pings[0] + pings[1] + pings[2]) / 3
        #print "average: " + str(avg)

        if avg == 0.0:
            ser.write('4') # blink red
        elif hadATimeout:
            ser.write('5') # blink yellow
        elif avg < good:
            ser.write('1') # solid green
        elif avg > bad:
            ser.write('3') # solid red
        else:
            ser.write('2') # solid yellow
