import serial
import time
import pymobitec_flipdot as flipdot
import threading
import queue
import curses
import signal
import sys
import RPi.GPIO as GPIO
from numpy import random


def signal_handler(sig, frame):
    exit_game()
signal.signal(signal.SIGINT, signal_handler)

def exit_game():
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    sys.exit(0)

def keyboar_input(q):
    # get the curses screen window
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

    while 1:
        char = screen.getch()
        try:
            if char == curses.KEY_RIGHT:
                q.put_nowait("right")
            elif char == curses.KEY_LEFT:
                q.put_nowait("left")
            elif char == curses.KEY_UP:
                q.put_nowait("up")
            elif char == curses.KEY_DOWN:
                q.put_nowait("down")
        except queue.Full:
            pass

def update_display(q):
    with serial.Serial('/dev/ttyS0', 4800, timeout=1) as ser:
        while True:
            command = q.get()
            ser.write(command)

def set_LED(q):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.LOW)

    while(1):
        q.get()
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.05)


display_queue = queue.Queue(1)
display_thr = threading.Thread(target=update_display, args=(display_queue,))
display_thr.daemon = True
display_thr.start()

led_queue = queue.Queue(50)
led_thr = threading.Thread(target=set_LED, args=(led_queue,))
led_thr.daemon = True
led_thr.start()

keybaord_queue = queue.Queue(2)
screen = curses.initscr()
keyboard_thr = threading.Thread(target=keyboar_input, args=(keybaord_queue,))
keyboard_thr.daemon = True
keyboard_thr.start()

init_snake = [[3, 8], [4, 8], [5, 8]]
snake = init_snake.copy()
snake_direction = "right"
food = [[random.randint(0, 27), random.randint(0, 15)]]
score = 0

while True:
    pixels = snake.copy()
    pixels.extend(food)
    to_display = flipdot.set_pixels(tuple(zip(*pixels)))
    display_queue.put(to_display)
    time.sleep(0.25)

    #  Set snake direction
    if keybaord_queue.qsize() > 0:
        input = keybaord_queue.get()
        if input == "right" and snake_direction == "left":
            pass
        elif input == "left" and snake_direction == "right":
            pass
        elif input == "up" and snake_direction == "down":
            pass
        elif input == "down" and snake_direction == "up":
            pass
        else:
            snake_direction = input

    # Move snake
    if snake_direction == "right":
        snake.extend([[snake[-1][0] + 1, snake[-1][1]]])
    elif snake_direction == "left":
        snake.extend([[snake[-1][0] - 1, snake[-1][1]]])
    elif snake_direction == "up":
        snake.extend([[snake[-1][0], snake[-1][1] - 1]])
    elif snake_direction == "down":
        snake.extend([[snake[-1][0], snake[-1][1] + 1]])

    #  Check if game over
    for i in range(len(snake)-2):
        if snake[-1][:] == snake[i+1][:]:

            # Set score
            score_text = flipdot.Text("SCORE:", 2, 0, flipdot.Fonts.text_5px)
            if score < 10:
                score_number = flipdot.Text(str(score), 10, 15, flipdot.Fonts.text_9px_bold)
            else:
                score_number = flipdot.Text(str(score), 7, 15, flipdot.Fonts.text_9px_bold)
            msg = flipdot.set_texts([score_text, score_number])
            display_queue.put(msg)

            # blink LEDs
            time.sleep(0.3)
            for _ in range(0, 40):
                led_queue.put(1)
            time.sleep(4)

            while not keybaord_queue.empty():
                keybaord_queue.get_nowait()

            # Re-init game
            snake = init_snake.copy()
            score = -1
            food = [[5, 8]]
            snake_direction = "right"

            # Wait for key to start game
            keybaord_queue.get()

            # clear queue so new game does not start automatically
            while not keybaord_queue.empty():
                keybaord_queue.get_nowait()

            break

    #  If snake goes to the end, start on the other side
    if snake[-1][0] == 28:
        snake[-1][0] = 0
    elif snake[-1][0] == -1:
        snake[-1][0] = 27
    elif snake[-1][1] == 16:
        snake[-1][1] = 0
    elif snake[-1][1] == -1:
        snake[-1][1] = 15

    #  If snake eats food, grow by one
    if snake[-1][:] == food[0][:]:
        food = [[random.randint(0, 27), random.randint(0, 15)]]
        score = score + 1
        led_queue.put(1)
    else:
        snake.pop(0)





