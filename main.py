import pygame
import numpy as np
import pickle


class GameOfLife():
    def __init__(self):
        self.n = 30
        self.width = 10
        self.height = 10
        self.margin = 1
        self.speed=10

    def _next_grid(self, grid):
        current_grid=grid
        next_grid= np.zeros((current_grid.shape[0], current_grid.shape[1]))
        for row, column in np.ndindex(current_grid.shape):
            currently_alive = np.sum(current_grid[row - 1:row + 2, column - 1:column + 2]) - current_grid[row, column]

            if current_grid[row, column] == 1 and currently_alive < 2 or currently_alive > 3:
               next_grid[row, column] = 0

            elif current_grid[row, column] == 0 and  currently_alive == 3:
               next_grid[row, column] = 1

            elif current_grid[row, column] == 1 and  2<= currently_alive <= 3:
               next_grid[row, column] = 1

        return next_grid


    def output(self,values):
        pygame.init()
        display = pygame.display.set_mode((self.n * (self.width + self.margin), self.n * (self.height + self.margin)))
        pygame.display.set_caption("Game of life output")

        grid = values

        for i in grid:
            print(i)


        done = False
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            display.fill((25, 25, 25))

            for row in range(self.n):
                for column in range(self.n):
                    pygame.draw.rect(display, (255,255,255) if grid[row][column] == 1 else (0,0,0),
                                     [self.margin + (self.margin + self.width) * column,
                                      self.margin + (self.margin + self.height) * row, self.width, self.height])

            grid = self._next_grid(grid)


            pygame.display.update()
            pygame.time.Clock().tick(self.speed)

        pygame.quit()


    def input(self):
        pygame.init()

        display = pygame.display.set_mode((self.n * (self.width + self.margin),self.n * (self.height + self.margin)))
        pygame.display.set_caption("Game of life Input")

        grid = [[0 for x in range(self.n)] for y in range(self.n)]

        done = False
        while not done:

            position = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    grid = np.array(grid)
                    self.output(grid)
                    done = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    column = position[0] // (self.width + self.margin)
                    row = position[1] // (self.height + self.margin)
                    #print(row, column)
                    grid[row][column] = 1

            display.fill((0,0,0))

            for row in range(self.n):
                for column in range(self.n):
                    pygame.draw.rect(display, (200,10,0) if grid[row][column] == 1 else (255,255,255),
                                     [self.margin + (self.margin + self.width) * column,
                                      self.margin + (self.margin + self.height) * row, self.width, self.height])
            pygame.display.flip()
            pygame.time.Clock().tick(60)


        pygame.quit()



#-Input any cell config
custom = GameOfLife()
custom.n = 40
custom.speed = 10
custom.input()

