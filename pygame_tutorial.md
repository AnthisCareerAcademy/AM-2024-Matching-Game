# Using PyGame in PyCharm

## Installing PyGame

To install PyGame, open the local terminal in a new PyCharm project.

![Press Alt+F12 to open the terminal](https://github.com/user-attachments/assets/53d80b17-9776-4b92-9302-a252d31c8338)

Inside the terminal, type `pip install pygame`.

Wait a while for everything to load, then add the following to the top of your code.

```python
import pygame
from pygame.locals import *

pygame.init()

pygame.quit()
```

This initializes PyGame and then closes it at the end.

## Making a Window in Pygame

Begin by defining a `runnning` variable after the `pygame.init()` call. Set it to true so that the game begins running immediately.

Next, define a variable called `screen`. This is a variable that PyGame will look for. Set it equal to `pygame.display.set_mode((800, 800))`. Notice that the argument is a tuple `(800, 800)` and not two arguments. This creates a screen that is 800 by 800.

Create a `while running` loop. Inside of it, add a for loop:

```python
for event in pygame.event.get():
    pass
```

This loop will iterate over PyGame's event calls, but we're only interested in the QUIT event, so we'll add an if statement that checks for it.

```python
if event.type == QUIT:
    running = False
```

Your code should look like this:

```python
import pygame
from pygame.locals import *

pygame.init()
running = True

screen = pygame.display.set_mode((800, 800))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
```

## Setting a Background

Now that we have a window, we can do some fun things to it like change the background color. You'll use the screen object for this.

To set the background color, use `screen.fill()`. It accepts an RGB tuple as its argument. Let's set the background to be light blue:

```python
screen.fill((50, 150, 200))
```

You can put this snippet before the while loop. You may notice, though, that this code doesn't actually change the color. You need another command below the first:

```python
pygame.display.update()
```

This updates the screen and changes the background. By placing these calls inside of the while loop and adding some variables, you can make a color-changing background!

You can also set the title of the window with `pygame.display.set_caption()`. This will change the name of the window to be whatever you choose.

## Creating Size Variables

You don't want your game to break if somebody resizes the screen, so it's always best to use relative coordinates that change based on the size of the screen. To do this, we'll rewrite some code:

```python
size = width, height = (800, 800)
screen = pygame.display.set_mode(size)
```

This code goes where the screen definition originally was. Now, we have a tuple called `size` that represents the size of the window, as well as `width` and `height` variables that represent the width and height.

Your code should look like this now:

```python
import pygame
from pygame.locals import *

pygame.init()
running = True

size = width, height = (800, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Game in PyGame")
screen.fill((200, 215, 230))
pygame.display.update()
.
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
```
