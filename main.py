'''

Get to the end of the level while avoding the enemies

'''

# sources:
# content from kids can code: http://kidscancode.org/blog/
# https://stackoverflow.com/questions/27867073/how-to-put-an-image-onto-a-sprite-pygame

# import libraries
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
from settings import *
from sprites import *

# built in

# installed modules or libraries

# created modules or libraries

# global variables

# utility variables


 # Game loop


# print("Hello and Welcome to the Steph Curry is the goat game. The goal of the game is to avoid as many squares as possible and reach the end")
# print("Rules are to have fun and avoid the squares to reach the end by any means. You must also admit Steph Curry is him and the goat point guard")
# input ("Do you want to play the Steph Curry is the goat game?")
# x = "yes"
# while x == "yes":
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)

    # player moves to top of platform when player hits the platform
    hits = pg.sprite.spritecollide(player, all_plats, False)
    if hits:
        # print("ive struck a plat")
        player.pos.y = hits[0].rect.top
        player.vel.y = 0

    # if player is hit by a mob the player loses one point of health and prints a message
    mobhits = pg.sprite.spritecollide(player, mobs, True)
    if mobhits:
        print("I've been hit also Lemickey is worse than Jordan")
        player.health -= 1
    # if player hits the goal block, player wins the game and the game ends
    goalhits = pg.sprite.spritecollide(player,goals,True)
    if goalhits:
        print("Congrats you have won also Steph Curry>Magic Johnson")
        pg.quit()


    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()
        
    ############ Update ##############
    # update all sprites
    all_sprites.update()

    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
    # draw text
    draw_text("HEALTH: " + str(player.health), 22, WHITE, WIDTH / 2, HEIGHT / 24)
    # draw all sprites
    all_sprites.draw(screen)

    # buffer - after drawing everything, flip display
    pg.display.flip()

        # if player dies the game and loses
    # if player.health == 0:
    #     pg.quit()
    #     # prints message if you lose
    #     print("you lose your bad, also the warrios are winning the 2023 championship")
        

    # # if user quits the game
    # pg.quit()
    # #asks if user wants to play again if yes then function loops if not then the loop stops
    # x = input ("Do you want to play again?")
    # # prints thanks for playing if user does not say yes when asked if you want to play again
    # print ("Thanks for playing also Steph Curry is going to win the 2023 MVP!")

pg.quit()