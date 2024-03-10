import pygame
import Init

class Circle(object):
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
    def draw(self):
        pygame.draw.circle(
            Init.display,
            self.color,
            Init.convert_cordinates((self.x, self.y)),
            self.radius
        )