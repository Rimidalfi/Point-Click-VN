import pygame as pg
import sys
from pygame.locals import *
import time
import random

running = True
clock = pg.time.Clock()
# font_color = (255, 255, 255)
window = (0, 0)
pg.init()
screen = pg.display.set_mode(window, RESIZABLE)
# image = pg.image.load("assets/sprites/backgroud.png")
# screen_info = pg.display.Info()
scale_surface = pg.Surface((4, 3))
counter = 0
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
        # in case width is the shortest side
        case 0:
            if screen_info.current_w != scale_surface_width:
                scale_surface = pg.transform.scale(
                    scale_surface, (screen_info.current_w, screen_info.current_w/scale_ratio))
                scale_surface_height = scale_surface.get_height()
                screen_info = pg.display.Info()
                screen.blit(
                    scale_surface, (0, (screen_info.current_h/2)-(scale_surface_height/2)))
                print("width is smaller\n")

                """Printing values"""
                scale_surface_width = scale_surface.get_width()
                scale_surface_height = scale_surface.get_height()
                print("\nVerhältnis:", scale_ratio, "\n ")
                print("Dispalygröße:", screen_info.current_w,
                      screen_info.current_h, "\n ")
                print("Rechteckgröße:", scale_surface_width, scale_surface_height,
                      "\n ")
                scale_surface.fill(
                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        # in case height is the shortest side
        case 1:
            if screen_info.current_h != scale_surface_height:
                scale_surface = pg.transform.scale(
                    scale_surface, (screen_info.current_h*scale_ratio, screen_info.current_h))
                scale_surface_width = scale_surface.get_width()
                screen_info = pg.display.Info()
                screen.blit(
                    scale_surface, ((screen_info.current_w/2)-(scale_surface_width/2), 0))
                print("height is smaller\n")

                """Printing values"""
                scale_surface_width = scale_surface.get_width()
                scale_surface_height = scale_surface.get_height()
                screen_info = pg.display.Info()
                print("\nVerhältnis:", scale_ratio, "\n ")
                print("Dispalygröße:", screen_info.current_w,
                      screen_info.current_h, "\n ")
                print("Rechteckgröße:", scale_surface_width, scale_surface_height,
                      "\n ")
                scale_surface.fill(
                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    pg.display.flip()
    clock.tick(60)

pg.quit()
sys.exit()

# time.sleep(3)
# screen.blit(scale_surface, (0, 0))

# if scale_surface_height != screen_info.current_h:

#     scale_surface = pg.transform.scale(
#         scale_surface, (screen_info.current_h*scale_ratio, screen_info.current_h))
#     scale_surface_width = scale_surface.get_width()
#     scale_surface_height = scale_surface.get_height()
#     screen_info = pg.display.Info()
# image_width = image.get_width()
# screen.blit(scale_surface, (0, 0))

# if init_screen_width != screen_info.current_w:
#     scaled_image = pg.transform.scale(image, (1, screen_info.current_w))
#     screen.blit(scaled_image, (0, 0))
#     """reference width of scaled image"""
#     image_scaling_ratio = image_width/screen_info.current_w

# print(image_scaling_ratio)
# print(screen_info.current_w)
# print(scaled_image.get_width())
