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
