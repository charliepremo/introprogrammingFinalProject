import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
from settings import *

vec = pg.math.Vector2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def colorbyte():
        return random.randint(0,255)


# creates text on the screen
def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)


# sprites...

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(5, 5)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.health = 5
        self.jumppower = 12
        self.jumps = 2
        # the keys and controls of the game
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

# creates the platforms class
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# creates mob class
class Mob(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
    def update(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH or self.rect.x < 0:
            self.speed *= -1



# creates end goal
class Goal(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()

# create groups
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
mobs = pg.sprite.Group()
goals = pg.sprite.Group()

# instantiate classes
player = Player()

# places platfroms, plat 4-10 are randomly generated before every time you start
plat = Platform(0,0,5,800)
# plat2 = Platform(1400,0,5,800)
ground = Platform(0, HEIGHT-40, 2000, 40)
plat4 = Platform(randint(0,1400),randint(0,700),100,35)
plat5 = Platform(randint(0,1400),randint(0,700),100,35)
plat6 = Platform(randint(0,1400),randint(0,700),100,35)
plat7 = Platform(randint(0,1400),randint(0,700),100,35)
plat8 = Platform(randint(0,1400),randint(0,700),100,35)
plat9 = Platform(randint(0,1400),randint(0,700),100,35)
plat10 = Platform(randint(0,1400),randint(0,700),100,35)

# puts end goal in
goal = Goal(1300,350,100,100)

# puts 65 mobs in at random parts of the game
for i in range((30)):
    m = Mob(randint(0,WIDTH), randint(0, HEIGHT), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
    all_sprites.add(m)
    mobs.add(m)
    print(m)


# add player to all sprites group
all_sprites.add(player)
all_plats.add(plat, ground, plat4, plat5, plat6, plat7, plat8, plat9, plat10)
goals.add(goal)

# add platform to all sprites group
all_sprites.add(plat)
# all_sprites.add(plat2)
all_sprites.add(ground)
all_sprites.add(plat4)
all_sprites.add(plat5)
all_sprites.add(plat6)
all_sprites.add(plat7)
all_sprites.add(plat8)
all_sprites.add(plat9)
all_sprites.add(plat10)
all_sprites.add(goal)

# add things to their respective groups
