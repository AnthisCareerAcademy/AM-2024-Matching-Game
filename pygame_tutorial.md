# Using PyGame in PyCharm

## Installing PyGame

To install PyGame, open the local terminal in a new PyCharm project.

![Press Alt+F12 to open the terminal](https://github.com/user-attachments/assets/31c718aa-3ff4-4735-9a0c-e8f59607e73c)

Inside the terminal, type `pip install pygame`.

Wait a while for everything to load, then add the following to the top of your code.

```python
import pygame
from pygame.locals import *
pygame.init()
```

This initializes the PyGame window.
