import pygame
import sys
import random
import math

pygame.init()

width, height = 600, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Particle System")

particles = []

def create_particle(x, y):
    angle = random.uniform(0, 2 * math.pi)
    speed = random.uniform(2, 5)
    vx = speed * math.cos(angle)
    vy = speed * math.sin(angle)
    color = pygame.Color(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255), 255)
    radius = random.randint(5, 10)
    lifetime = 300
    particles.append([[x, y], [vx, vy], color, radius, lifetime])

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for _ in range(50):
                create_particle(event.pos[0], event.pos[1])

    screen.fill("black")

    for i, particle in reversed(list(enumerate(particles))):
        pos, vel, color, radius, lifetime = particle
        pos[0] += vel[0]
        pos[1] += vel[1]
        color.a = int(255 * (lifetime / 30))  # Fade out alpha
        pygame.draw.circle(screen, color, (int(pos[0]), int(pos[1])), radius)
        particles[i][4] -= 1
        if lifetime <= 0:
            particles.pop(i)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
