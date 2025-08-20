import pygame
import sys
import math

pygame.init()

width, height = 600, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hypnotic Circle")

center_x, center_y = width // 2, height // 2
radius = 50
color = pygame.Color("lightblue")
phase = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
    radius = 50 + 30 * math.sin(pygame.time.get_ticks() / 200)
    hue = (pygame.time.get_ticks() // 10) % 360
    color.hsla = (hue, 100, 50, 100)

    pygame.draw.circle(screen, color, (center_x, center_y), int(radius))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
