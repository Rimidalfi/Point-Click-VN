import pygame as p
import sys

clock = p.time.Clock()
p.mixer.init()
p.init()
screen = p.display.set_mode((500, 500))
p.display.set_caption("button")
x = p.Rect(0, 0, 200, 100)
x.center = (250, 250)
initial_size = x.size

click_sound = p.mixer.Sound("./assets/sounds/Click.mp3")


backgroudn_img = p.image.load("./assets/sprites/backgroud_500x500.png")
button_idle = p.image.load("./assets/sprites/Button_idle.png")
button_hover = p.image.load("./assets/sprites/Button_hover.png")
button_idle_rect = button_idle.get_rect()
button_hover_rect = button_hover.get_rect()
button_idle_rect.center = (250, 250)
button_hover_rect.center = (250, 250)
button_initial_size = button_idle_rect.size
while True:
    screen.blit(backgroudn_img, (0, 0))

    mouse_pos = p.mouse.get_pos()
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            p.mixer.quit()
            sys.exit()

        """"CLICK Animation"""
        if event.type == p.MOUSEBUTTONDOWN:
            while x.collidepoint(mouse_pos):
                click_sound.play(0)
                x.inflate_ip(-10, -10)
                button_idle_rect.inflate_ip(-10, -10)

                break
        if event.type == p.MOUSEBUTTONUP and x.size < initial_size:
            x.inflate_ip(10, 10)

        if event.type == p.MOUSEBUTTONUP and button_idle_rect.size < button_initial_size:
            x.inflate_ip(10, 10)
            button_idle_rect.inflate_ip(10, 10)

        """HOVER Animation"""
        if x.collidepoint(mouse_pos):
            rect_color = (50, 168, 82)
            current_button = button_hover
            # Image Idle
        else:
            rect_color = (34, 117, 57)
            current_button = button_idle
            # Image Hover
        # if event.type == p.KEYDOWN:
        #     click_sound.play(0)
    scaled_button = p.transform.scale(current_button, button_idle_rect.size)
    screen.blit(scaled_button, button_idle_rect)
    # p.draw.rect(screen, rect_color, x)
    p.display.flip()
    clock.tick(60)
