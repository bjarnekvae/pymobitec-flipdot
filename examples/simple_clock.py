import serial
import time
import datetime
import pymobitec_flipdot as flipdot

with serial.Serial('/dev/ttyS0', 4800, timeout=1) as ser:

    while True:
        time_now = datetime.datetime.now()
        time_str = time_now.strftime("%H:%M")
        msg = flipdot.text(time_str)
        ser.write(msg)
        time.sleep(1)


