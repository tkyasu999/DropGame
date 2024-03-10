import pygame
import pymunk
import Init

class Ball(object):
    def __init__(self, x, y, color, radius, mass, collision_type):
        self.color = color
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.body.position = x, y
        self.body.mass = mass
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.collision_type = collision_type
        self.shape.density = 1
        self.shape.elasticity = 0.5
        self.shape.friction = 0.5
        Init.space.add(self.body, self.shape)
    def draw(self):
        pygame.draw.circle(
            Init.display,
            self.color,
            Init.convert_cordinates(self.body.position),
            self.shape.radius
        )

class Ball01(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, Init.color_01, Init.radius_01, 10, 1)
        pass

class Ball02(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, Init.color_02, Init.radius_02, 15, 2)
        pass

class Ball03(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, Init.color_03, Init.radius_03, 20, 3)
        pass

class Ball04(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, Init.color_04, Init.radius_04, 25, 4)
        pass

class Ball05(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, Init.color_05, Init.radius_05, 30, 5)
        pass

class Ball06(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, Init.color_06, Init.radius_06, 35, 6)
        pass

class Ball07(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, Init.color_07, Init.radius_07, 40, 7)
        pass

class Ball08(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, Init.color_08, Init.radius_08, 45, 8)
        pass

class Ball09(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, Init.color_09, Init.radius_09, 50, 9)
        pass

class Ball10(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, Init.color_10, Init.radius_10, 55, 10)
        pass

class Ball11(Ball):
    def __init__(self, x, y):
        super().__init__(x, y, Init.color_11, Init.radius_11, 60, 11)
        pass