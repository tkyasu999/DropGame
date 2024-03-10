import random
import Init
import Circle

class NextCircle(Circle.Circle):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.update()
    def update(self):
        r = random.randint(1, 5)
        if(r == 1):
            self.color = Init.color_01
            self.radius = Init.radius_01
        elif(r == 2):
            self.color = Init.color_02
            self.radius = Init.radius_02
        elif(r == 3):
            self.color = Init.color_03
            self.radius = Init.radius_03
        elif(r == 4):
            self.color = Init.color_04
            self.radius = Init.radius_04
        elif(r == 5):
            self.color = Init.color_05
            self.radius = Init.radius_05