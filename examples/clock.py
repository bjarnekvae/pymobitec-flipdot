import serial
import time
import datetime
import pymobitec_flipdot as flipdot

with serial.Serial('/dev/ttyS0', 4800, timeout=1) as ser:

    while True:
        tod = datetime.datetime.now()
        time_str = tod.strftime("%H:%M")

        msg = flipdot.set_text(time_str, 1, 0, flipdot.Fonts.numbers_14px)
        ser.write(msg)

        time.sleep(10)
