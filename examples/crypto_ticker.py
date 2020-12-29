import serial
import time
import pymobitec_flipdot as flipdot
import cryptocompare
import RPi.GPIO as GPIO

crypto_currency = 'ADA'
fiat_currency = 'USD'
LED_flash_threshold = 0.005  # % price change per period

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)

prev_price = 1.0

with serial.Serial('/dev/ttyS0', 4800, timeout=1) as ser:

    while True:
        price = cryptocompare.get_price(crypto_currency, curr=fiat_currency)

        if price is not None:
            price = price[crypto_currency]['USD'] + 0.00001  # extra digits to fill out display
        else:
            time.sleep(60)
            continue

        if price > 1.0:
            price_str = str(price)[:5]
        else:
            price_str = str(price)[1:6]

        msg = flipdot.set_text(price_str, 1, 0, flipdot.Fonts.numbers_14px)
        ser.write(msg)

        if (price-prev_price)/prev_price > LED_flash_threshold:
            for i in range(3):
                GPIO.output(18, GPIO.LOW)
                time.sleep(0.04)
                GPIO.output(18, GPIO.HIGH)
                time.sleep(0.06)

        prev_price = price

        time.sleep(60)
