# Stanford Code In Place 2021

## Karel Reference

### Base Commands

```
move()
turn_left()
put_beeper()
pick_beeper()
```

### Types of Conditions

```
front_is_clear()
left_is_clear()
right_is_clear()

beepers_present()
beepers_in_bag()

facing_north()
facing_south()
facing_east()
facing_west()

no_beepers_present()
no_beepers_in_bag()

front_is_blocked()
left_is_blocked()
right_is_blocked()

not_facing_north()
not_facing_south()
not_facing_east()
not_facing_west()

random()
random(0.75)
```

### Program Structure

```
# Comments can be included in any part of a program.
# They start with a # and include the rest of the line.def main():
    code to execute declarations of other functions
```

### Conditions

```
if condition:
    code run if condition passes

if condition:
    code block for "yes"
else:
    code block for "no"
```

### Loops

```
for i inrange(count):
    code to repeat

while condition:
    code to repeat
```

### Functions

```
def name():
    code in the body of the function.
```

### Extra Commands

```
paint_corner(COLOR_NAME)
corner_color_is(COLOR_NAME)
```

### Valid colours

```
BLANK
BLACK
BLUE
CYAN
DARK_GRAY
GRAY
GREEN
LIGHT_GRAY
MAGENTA
ORANGE
PINK
RED
WHITE
YELLOW
```
