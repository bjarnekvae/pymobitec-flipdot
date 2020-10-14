import serial
import time
import pymobitec_flipdot as flipdot
import cryptocompare

currency = 'ADA'

with serial.Serial('/dev/ttyS0', 4800, timeout=1) as ser:

    while True:
        price = cryptocompare.get_price(currency, curr='USD')
        price = price[currency]['USD'] + 0.00001 # Prevent round number

        if price > 1.0:
            price_str = str(price)[:5]
        else:
            price_str = str(price)[1:6]

        msg = flipdot.set_text(price_str, 1, 0, flipdot.Fonts.numbers_14px)
        ser.write(msg)

        time.sleep(60)
