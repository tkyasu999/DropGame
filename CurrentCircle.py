import pygame
import Circle
import Init
import Ball

class CurrentCircle(Circle.Circle):
    def __init__(self, x, y, color, radius, start, stop):
        super().__init__(x, y, color, radius)
        self.dist = 2
        self.start = start
        self.stop = stop
    def handle_keys(self):
        key = pygame.key.get_pressed()
        if(key[pygame.K_LEFT] and (self.x - self.dist) >= self.start):
            self.x -= self.dist
        if(key[pygame.K_RIGHT] and (self.x + self.dist) <= self.stop):
            self.x += self.dist
    def get_ball(self):
        if(self.radius == Init.radius_01):
            ball = Ball.Ball01(self.x, self.y)
        elif(self.radius == Init.radius_02):
            ball = Ball.Ball02(self.x, self.y)
        elif(self.radius == Init.radius_03):
            ball = Ball.Ball03(self.x, self.y)
        elif(self.radius == Init.radius_04):
            ball = Ball.Ball04(self.x, self.y)
        elif(self.radius == Init.radius_05):
            ball = Ball.Ball05(self.x, self.y)
        return ball