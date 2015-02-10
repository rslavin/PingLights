import serial
import time
import ping
from array import *

good = 100
bad = 250

host = "8.8.8.8"
timeout = 1
size = 32

ser = serial.Serial('/dev/ttyS9', 115200)

pings = array('d', [0,0,0])
currentPing = 0
avg = 0

while True:
    time.sleep(2)
    line = ping.do_one(host, timeout, size)
    if line == None:
        line = 0
    line = line * 1000
    pings[currentPing] = line
    currentPing = currentPing + 1
    if currentPing > 2:
        currentPing = 0
        avg = (pings[0] + pings[1] + pings[2]) / 3
        #print "average: " + str(avg)

        if avg == 0.0:
            ser.write('4')
        elif avg < good:
            ser.write('1')
        elif avg > bad:
            ser.write('3')
        else:
            ser.write('2')
