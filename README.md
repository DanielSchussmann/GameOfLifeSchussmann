# GameOfLifeSchussmann

#### Required Imports
~~~
import pygame
import numpy as np
~~~

### Gerneral Functionality

The application is run in 'custom mode' by calling the GameOfLife() class and then calling the input() method. 

The application is run in 'Example mode' by calling the GameOfLife() class and then calling the output() method while specifying a Starting Matrix.

Before calling input() all the constructors can be changed:

Change the number of cells with:
~~~
self.n
~~~

Change the evolution speed with:
~~~
self.speed
~~~

Change the cell look(cell-width, cell-height, margin between cells)  with:
~~~
self.width
self.height
self.margin
~~~
