from pylibftdi import Device
import time
import datetime
import pymobitec_flipdot as flipdot

with Device(mode='b') as dev:
    dev.baudrate = 4800

    while True:
        time_now = datetime.datetime.now()
        time_str = time_now.strftime("%H:%M")
        msg = flipdot.text(time_str)
        dev.write(msg)
        time.sleep(10)


