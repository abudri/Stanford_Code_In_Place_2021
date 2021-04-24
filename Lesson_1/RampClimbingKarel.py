from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""

def main():
    put_beeper()
    while front_is_clear():
        move()
        move()
        turn_left()
        move()
        put_beeper()
        turn_right()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    run_karel_program('RampKarel3.w')
