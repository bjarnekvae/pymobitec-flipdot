import serial
import time
import pymobitec_flipdot as flipdot
import threading
import queue
import curses
import signal
import sys
from numpy import random

def signal_handler():
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def keyboar_input(q):
    # get the curses screen window
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

    while 1:
        char = screen.getch()
        try:
            if char == curses.KEY_RIGHT:
                screen.addstr(0, 0, 'right')
                q.put_nowait("right")
            elif char == curses.KEY_LEFT:
                screen.addstr(0, 0, 'left ')
                q.put_nowait("left")
            elif char == curses.KEY_UP:
                screen.addstr(0, 0, 'up   ')
                q.put_nowait("up")
            elif char == curses.KEY_DOWN:
                screen.addstr(0, 0, 'down ')
                q.put_nowait("down")
        except queue.Full:
            pass

def update_display(q):
    with serial.Serial('/dev/ttyS0', 4800, timeout=1) as ser:

        while True:
            command = q.get()
            ser.write(command)


display_queue = queue.Queue(1)

display_thr = threading.Thread(target=update_display, args=(display_queue,))
display_thr.daemon = True
display_thr.start()

snake = [[3, 8], [4, 8], [5, 8]]
snake_direction = "right"
food = [[random.randint(0, 27), random.randint(0, 15)]]
score = 0

keybaord_queue = queue.Queue(1)
screen = curses.initscr()
keyboard_thr = threading.Thread(target=keyboar_input, args=(keybaord_queue,))
keyboard_thr.daemon = True
keyboard_thr.start()


while True:
    pixels = snake.copy()
    pixels.extend(food)
    to_display = flipdot.set_pixels(tuple(zip(*pixels)))
    display_queue.put(to_display)
    time.sleep(0.2)

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
            msg = flipdot.text(str(score), 8, 11, flipdot.Fonts.text_9px_bold)
            display_queue.put(msg)
            time.sleep(5)
            signal_handler()

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
    else:
        snake.pop(0)





