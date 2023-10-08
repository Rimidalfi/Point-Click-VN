import pygame as pg
import sys
from pygame.locals import *
import time
import random

running = True
clock = pg.time.Clock()
window = (0, 0)
pg.init()
screen = pg.display.set_mode(window,  RESIZABLE,)
image = pg.image.load("assets/sprites/backgroud.png")
image_w = image.get_width()
image_h = image.get_height()
scale_surface = pg.Surface((image_w, image_h))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    scale_surface_width = scale_surface.get_width()
    scale_surface_height = scale_surface.get_height()
    screen_info = pg.display.Info()
    scale_ratio = scale_surface_width/scale_surface_height

    """get shortest side of window"""
    screen_size = pg.display.get_surface().get_size()
    screen_smallest_value = min(screen_size)
    shortest_side = screen_size.index(screen_smallest_value)

    match shortest_side:
        case 0:
            if screen_info.current_w != scale_surface_width:
                scale_surface = pg.transform.scale(
                    scale_surface, (screen_info.current_w, screen_info.current_w/scale_ratio))
                scale_surface_height = scale_surface.get_height()
                screen_info = pg.display.Info()
                screen.fill(0)
                image = pg.image.load("assets/sprites/backgroud.png")
                image = pg.transform.scale(
                    image, (screen_info.current_w, screen_info.current_w/scale_ratio))
                screen.blit(image, (0, (screen_info.current_h/2) -
                            (scale_surface_height/2)))
                screen.blit(image, (0, (screen_info.current_h/2) -
                            (scale_surface_height/2)))
        case 1:
            if screen_info.current_h != scale_surface_height:
                scale_surface = pg.transform.scale(
                    scale_surface, (screen_info.current_h*scale_ratio, screen_info.current_h))
                scale_surface_width = scale_surface.get_width()
                screen_info = pg.display.Info()
                screen.fill(0)
                image = pg.image.load("assets/sprites/backgroud.png")
                image = pg.transform.scale(
                    image, (screen_info.current_h*scale_ratio, screen_info.current_h))
                screen.blit(image, ((screen_info.current_w/2) -
                            (scale_surface_width/2), 0))
                screen.blit(image, ((screen_info.current_w/2) -
                            (scale_surface_width/2), 0))
    pg.display.flip()
    clock.tick(60)

pg.quit()
sys.exit()
