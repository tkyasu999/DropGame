import pygame
import pymunk
import Init

class Field():
    def __init__(self, tlx, tly, brx, bry):
        self.tlx = tlx
        self.tly = tly
        self.brx = brx
        self.bry = bry
        self.edge = int(brx - tlx)
        self.step = 7
        self.width = 3
        # Start and Stop
        self.rl_start, self.rl_stop = (brx, tly), (brx, bry)
        self.bl_start, self.bl_stop = (tlx, bry), (brx, bry)
        self.ll_start, self.ll_stop = (tlx, tly), (tlx, bry)
        # Create Line
        self.create_line(self.rl_start, self.rl_stop)  # Right
        self.create_line(self.bl_start, self.bl_stop)  # Bottom
        self.create_line(self.ll_start, self.ll_stop)  # Left
    def draw(self):
        # Top Line
        for i in range(0, self.edge, self.step):
            if(i % (self.step * 2) == 0):
                pygame.draw.line(
                    Init.display,
                    Init.BLACK,
                    Init.convert_cordinates((self.tlx+i, self.tly)),
                    Init.convert_cordinates((self.tlx+i+self.step, self.tly)),
                    self.width
                )
        # Right Line
        pygame.draw.line(
            Init.display,
            Init.BLACK,
            Init.convert_cordinates(self.rl_start),
            Init.convert_cordinates(self.rl_stop),
            self.width
        )
        # Bottom Line
        pygame.draw.line(
            Init.display,
            Init.BLACK,
            Init.convert_cordinates(self.bl_start),
            Init.convert_cordinates(self.bl_stop),
            self.width
        )
        # Left Line
        pygame.draw.line(
            Init.display,
            Init.BLACK,
            Init.convert_cordinates(self.ll_start),
            Init.convert_cordinates(self.ll_stop),
            self.width
        )
    def create_line(self, start, stop):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(body, start, stop, self.width)
        shape.elasticity = 0.75
        shape.friction = 0.9
        Init.space.add(shape, body)