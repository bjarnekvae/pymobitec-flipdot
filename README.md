# pymobitec-flipdot
Python code for controlling a Mobitec RS485 flip dot display

## Hardware
The code in this repository is tested with a 28x16 Mobitec FlipDot display controlled by a Raspberry Pi Zero via a UART-RS485
converter. All the necessary components (Raspberry Pi, UART-RS485 converter, DC-DC converter) has successfully been
integrated inside the Mobitec Flipdot display housing. Commands are executed via ssh from a external computer to 
the Raspberry Pi

---Image here---

An image of the Mobitec display currently running ``crypto_ticker.py`` with Cardano ADA - USD trading pairs.

### Connection
The flipdot display are powered by 24 VDC and controlled via a RS485 serial interface, a UART(or USB)-to-RS485 converter
can be bought cheaply on eBay. The wires from the flipdot display are as following:

 - Red wire: +24 volt
 - White wire: RS485 D+
 - Green wire: RS485 D-
 - Black wire: Ground

Here the white and green wires are connected to a UART-to-RS485 converter, which again is connected to GPIO14 and GPIO15 
pin (serial pins, Rx, Tx) on a Raspberry Pi Zero (powered by a DC-DC stepdown converter from the 24V power supply).
The LED-lighting in the flipdot display is controlled by the Raspberry Pi (GPIO18) via an optocoupler.


## Installation:

``pip install requirements``

``python setup.py install``

## Examples
``clock.py`` - Display the time of day (24h format) using custom fonts meant to utilize the entire display.

``clock_secHand.py`` - Same as ``clock.py`` with added seconds hand.

``crypto_ticker.py`` - Displays the price of cryptocurrency, blinks LEDs when price moves more than 0.5% the last minute.

``snake.py`` - An implementation of Snake, the speed is limited due to the slow baud rate of the serial communication
(4800 bit/s).

## References
http://www.busselektro.no/tips-og-funksjonsbeskrivelser/mobitec-rs485/

https://github.com/datagutten/mobitec-php/

https://github.com/duffrohde/mobitec-rs485/

## Donate
Cardano ADA - addr1vy5f47qv28xlvvp7j35xyf8ep2wurprllueegc5nuruav8g0m7f0u