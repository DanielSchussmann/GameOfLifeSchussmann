import pygame
import numpy as np



class GameOfLife():
    def __init__(self):
        self.n = 30         # Number of Rows and Columns so nxn
        self.width = 10     # Width of a cell
        self.height = 10    # height of a cell
        self.margin = 1     # margin between the cells
        self.speed=10       # Update speed

    def _next_grid(self, grid):     # Function is privat because it is only accessed within the class
        current_grid=grid           # Set the current grid to the incoming input

        for row, column in np.ndindex(current_grid.shape):  # Loops through all the values
            currently_alive = np.sum(current_grid[row - 1:row + 2, column - 1:column + 2]) - current_grid[row, column]  # Retreive the values of the neighboring cells

            if current_grid[row, column] == 1 and currently_alive < 2 or currently_alive > 3:   # Check if cell should "die"
               current_grid[row, column] = 0                # Set value to 0

            elif (current_grid[row, column] == 0 and  currently_alive == 3):                    # Check if the cell should be revived
                current_grid[row, column] = 1               # Set value to 1

        next_grid = current_grid
        return next_grid            # Returns the updated grid back to the output


    def output(self,values):    # Call directly if no Input is wanted
        pygame.init()           # Initializes the pygame environment
        display = pygame.display.set_mode((self.n * (self.width + self.margin), self.n * (self.height + self.margin)))  # Set the displaysize in accordance to the cell count
        pygame.display.set_caption("Game of life output")   # Set the window Title

        grid = values           # This sets the starting grid
        done = False
        while not done:         # Loops until variable done is set to be True

            for event in pygame.event.get():        # Runs if the window is closed
                if event.type == pygame.QUIT:
                    done = True                     # Exit the loop

            display.fill((25, 25, 25))      # This creates the grid effect as the rectangels are merely spaced appart. Without this there would be no grid

            for row in range(self.n):       # This loop colors in all the cells according to their value in either white if == 1 or black if == 0
                for column in range(self.n):
                    pygame.draw.rect(display, (255,255,255) if grid[row][column] == 1 else (0,0,0),
                                     [self.margin + (self.margin + self.width) * column,
                                      self.margin + (self.margin + self.height) * row, self.width, self.height])

            grid = self._next_grid(grid)            # Get the next step


            pygame.display.update()                 # Updates the window
            pygame.time.Clock().tick(self.speed)    # Speed in which the application updates

        pygame.quit()           # Is required so that there is no error message


    def input(self):    # Call if a custom input should be defined
        pygame.init()   # Initializes the pygame environment

        display = pygame.display.set_mode((self.n * (self.width + self.margin),self.n * (self.height + self.margin)))   # Set the displaysize in accordance to the cell count
        pygame.display.set_caption("Game of life Input")            # Set the window Title

        grid = [[0 for x in range(self.n)] for y in range(self.n)]  # Fills a grid of size nxn with zeros

        done = False
        while not done:                     # loops until variable done is set to be True

            position = pygame.mouse.get_pos()   # the mouse position within the application

            for event in pygame.event.get():    # Runs if the window is closed
                if event.type == pygame.QUIT:
                    grid = np.array(grid)       # Turn the grid into an array so it can be manipulated by numpy
                    self.output(grid)           # Call the output method with the highlighted grid
                    done = True                 # Terminate the while loop

                elif event.type == pygame.MOUSEBUTTONDOWN:              # Runs if the mouse is clicked
                    column = position[0] // (self.width + self.margin)  # Gets the  colume and row inde of the nearest cell to the mouse cursor
                    row = position[1] // (self.height + self.margin)    # Gets the  colume and row inde of the nearest cell to the mouse cursor
                    #print(row, column)
                    grid[row][column] = 1                                # Sets the value of the grid to 1 if clicked

            display.fill((0,0,0))           # This creates the grid effect as the rectangels are merely spaced appart. Without this there would be no grid

            for row in range(self.n):       # This loop colors in all the cells according to their value in either red if == 1 or white if == 0
                for column in range(self.n):
                    pygame.draw.rect(display, (200,10,0) if grid[row][column] == 1 else (255,255,255),
                                     [self.margin + (self.margin + self.width) * column,
                                      self.margin + (self.margin + self.height) * row, self.width, self.height])
            pygame.display.flip()           # Updates the window so highlighted cells appear
            pygame.time.Clock().tick(60)    # speed in which the application updates


        pygame.quit()   # Is required so that there is no error message

"""

#-Input any cell config
custom = GameOfLife()
custom.n = 60
custom.input()"""


