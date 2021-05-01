# Stanford Code In Place 2021

## Karel Reference


<img src="https://user-images.githubusercontent.com/17362519/116785443-96020400-aa67-11eb-87b2-372f1815634c.png" width="750;" />

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

## Glossary

**Decomposition / Step-wise refinement**
How to take a big problem and break it down into smaller pieces, that process of breaking it down is called Decomposition / Step-wise Refinement. It's like how you decompose and break down things that are organic. The same word.  We're going to learn how to take big problems and break them down to smaller pieces so that you can solve great tasks without writing really convoluted code.  It's a real art form and it's incredibly important, and it's one of the most important things about becoming a great engineer. It has other names some people call it stepwise refinement but it's the same art form that people are talking about 

