import serial
import time
import datetime
import pymobitec_flipdot as flipdot

with serial.Serial('/dev/ttyS0', 4800, timeout=1) as ser:

    while True:
        tod = datetime.datetime.now()

        hour = tod.hour
        minute = tod.minute

        msb_h = str(hour // 10)
        lsb_h = str(hour % 10)
        colon = ":"
        msb_m = str(minute // 10)
        lsb_m = str(minute % 10)

        time_str = msb_h + lsb_h + colon + msb_m + lsb_m

        msg = flipdot.set_text(time_str, 1, 0, flipdot.Fonts.numbers_14px)
        ser.write(msg)

        time.sleep(10)
