from karel.stanfordkarel import *

def main():

    while front_is_clear():
        turn_left()
        build_column()
        go_back_down()
        next_avenue()
    turn_left()
    build_column()

def build_column():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()
    if no_beepers_present():
        put_beeper()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def next_avenue():
    if front_is_clear():
        for i in range(4):
            move()

def go_back_down():
    turn_around()
    while front_is_clear():
        move()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    run_karel_program('SampleQuad2.w')
