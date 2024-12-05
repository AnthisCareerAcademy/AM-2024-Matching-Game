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
```

This initializes the PyGame window.
