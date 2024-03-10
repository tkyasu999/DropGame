import pygame
import pymunk
import math

pygame.init()

disp_size = (800, 800)
display = pygame.display.set_mode(disp_size)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = 0, -1000
FPS = 100

BLACK = (0, 0, 0)
WHEAT = (245, 222, 179)

color_01 = (255,   0,   0)
color_02 = (255, 100, 100)
color_03 = (100,   0, 150)
color_04 = (255, 150,   0)
color_05 = (255, 100,   0)
color_06 = (255,   0,   0)
color_07 = (255, 255, 150)
color_08 = (255, 200, 200)
color_09 = (255, 200,   0)
color_10 = (100, 200,  50)
color_11 = (  0, 150,   0)

radius_01 = 10
radius_02 = 15
radius_03 = 20
radius_04 = 25
radius_05 = 30
radius_06 = 35
radius_07 = 40
radius_08 = 45
radius_09 = 50
radius_10 = 55
radius_11 = 60

def convert_cordinates(point):
    return point[0], disp_size[1]-point[1]

def rotate_cordinates(point, d):
    rad = math.radians(d)
    rotated_x = point[0] * math.cos(rad) - point[1] * math.sin(rad)
    rotated_y = point[0] * math.sin(rad) + point[1] * math.cos(rad)
    return rotated_x, rotated_y