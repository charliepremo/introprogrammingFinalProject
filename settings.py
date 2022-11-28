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


def controls(self):
        keys = pg.key.get_pressed()
        # if keys[pg.K_w]:
        #     self.acc.y = -1
        if keys[pg.K_a]:
            self.acc.x = -.75
        # if keys[pg.K_s]:
        #     self.acc.y = 1
        if keys[pg.K_d]:
            self.acc.x = .75


# how you jump
def jump(self):
    self.rect.x += 1
    hits = pg.sprite.spritecollide(self, all_plats, False)
    self.rect.x += -1
    # player must be on platform to jump, then has 5 double jumps until hits platform again
    if hits:
        self.jumps = 5
    if self.jumps > 0:
        self.vel.y = -self.jumppower
        self.jumps -= 1
        # print(self.jumps)

def update(self):
            self.acc = vec(0,PLAYER_GRAV)
            self.controls()
            # friction
            self.acc.x += self.vel.x * -0.1
            # self.acc.y += self.vel.y * -0.1
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc
            # self.rect.x += self.xvel
            # self.rect.y += self.yvel
            self.rect.midbottom = self.pos

