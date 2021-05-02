# Stanford Code In Place 2021

## Karel Reference


<img src="https://user-images.githubusercontent.com/17362519/116785443-96020400-aa67-11eb-87b2-372f1815634c.png" width="700;" />

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

How to take a big problem and break it down into smaller pieces, that process of breaking it down is called Decomposition / Step-wise Refinement. It's like how you decompose and break down things that are organic. The same word.  We're going to learn how to take big problems and break them down to smaller pieces so that you can solve great tasks without writing really convoluted code.  It's a real art form and it's incredibly important, and it's one of the most important things about becoming a great engineer. It has other names some people call it stepwise refinement but it's the same art form that people are talking about. We also choose **milestones** when doing decomposition, and once one milestone is solved and tested, we move on to the next milestone to work on, so we decompose with milestones, such as "wash up" below. [Week 1, Lesson 3]

<img src="https://user-images.githubusercontent.com/17362519/116785789-5f2ced80-aa69-11eb-9f50-195e62b6ba61.png" width="550;" />


## Pro Tips

### Functions

<img src="https://user-images.githubusercontent.com/17362519/116786570-576f4800-aa6d-11eb-9bab-4c0c899969fb.png" width="350;" />


# Python Notes

## Variable Naming
<img src="https://user-images.githubusercontent.com/17362519/116816955-33296f00-ab32-11eb-8f04-3a19d3f750a0.png" width="400;" />

When you create a variable name in python the variable name must _start with either_ a **letter** or an **underscore** character. After that it can only contain **digits** or **letters**, and **underscores**.  You start with a digit like the number 2, it has to start with a letter or underscore but then it can contain letters digits or underscores but it can't contain other punctuation such as dashes or exclamation points or periods, etc. Those are not part of a valid variable name.  Final thing and this is a minor thing but it's important to keep in mind, it can't be one of the** built-in commands** in python so like back in the day you learned about **`for`** loops and **`while`** loops right those are actually python, so the word `**for**` is actually a built-in command in python so you can't have a variable called **`for`** because python will get confused between that and the notion of a **`for`** loop.  There's only about 200 or so of those words in python so it's not very likely that you just randomly happen to hit on one but just so you know.  The other thing you want to keep in mind is that variable names are also case sensitive, so `Hello` with a capital H is not the same variable name as `hello` with a lowercase h.  So variables are case sensitive, the same word but with different casing for the letters will actually be treated as different variables.  Also, the language doesn't enforce this but to do good programming style is to have variable names be **descriptive** of the value they were referring to. So if you have a variable called `x`, `x` is not a very descriptive name it's only a good name if you say it's referring to an `x` coordinate inside like an `x` `y` coordinate, or something if you're referring to some value in a grid like say where Karel was right, but otherwise if you're like having a writing a program that keeps track of a bank balance keeping track of the balance with a variable x isn't meaningful because when someone reads that they're like what is this `x` thin. You might actually want that variable to be something like `balance` or `bank_balance` to make it clear what value is actually being stored in the box for that variable.  Also, we want to write the variable names in **snake case** so just like you saw with the names for **functions**, the names for **variables** should also be snake case, which is separate words that are joined by underscores.

