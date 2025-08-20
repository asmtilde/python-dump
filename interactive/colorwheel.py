import pygame
import sys
import math

pygame.init()

width, height = 600, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Interactive Color Wheel")

center_x, center_y = width // 2, height // 2
radius = 100
current_color = pygame.Color("white")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            angle = math.atan2(mouse_y - center_y, mouse_x - center_x)
            hue = (math.degrees(angle) + 180) % 360
            current_color.hsla = (int(hue), 100, 50, 100)

    screen.fill("black")
    pygame.draw.circle(screen, current_color, (center_x, center_y), radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
