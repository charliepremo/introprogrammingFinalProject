import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint

vec = pg.math.Vector2

#game settings 
WIDTH = 1400
HEIGHT = 800
FPS = 30

# player settings
PLAYER_GRAV = 0.8
PLAYER_FRIC = 0.1

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
