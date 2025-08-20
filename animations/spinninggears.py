import pygame
import sys
import math

pygame.init()

width, height = 600, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spinning Gears")

gear_color = (100, 100, 100)
tooth_color = (150, 150, 150)

def draw_gear(surface, x, y, radius, num_teeth, angle):
    inner_radius = radius * 0.7
    tooth_width = radius * 0.3 / num_teeth
    tooth_depth = radius * 0.2

    for i in range(num_teeth):
        angle_tooth_center = angle + (2 * math.pi / num_teeth) * i
        angle_tooth_start1 = angle_tooth_center - tooth_width / 2
        angle_tooth_end1 = angle_tooth_center + tooth_width / 2
        angle_tooth_start2 = angle_tooth_center + math.pi / num_teeth - tooth_width / 2
        angle_tooth_end2 = angle_tooth_center + math.pi / num_teeth + tooth_width / 2
        
        outer_point1 = (x + radius * math.cos(angle_tooth_start1), y + radius * math.sin(angle_tooth_start1))
        outer_point2 = (x + radius * math.cos(angle_tooth_end1), y + radius * math.sin(angle_tooth_end1))
        
        inner_point1 = (x + inner_radius * math.cos(angle_tooth_start1), y + inner_radius * math.sin(angle_tooth_start1))
        inner_point2 = (x + (inner_radius - tooth_depth) * math.cos(angle_tooth_center), y + (inner_radius - tooth_depth) * math.sin(angle_tooth_center))
        inner_point3 = (x + inner_radius * math.cos(angle_tooth_end1), y + inner_radius * math.sin(angle_tooth_end1))

        pygame.draw.polygon(surface, tooth_color, [outer_point1, outer_point2, inner_point3, inner_point2, inner_point1])

    pygame.draw.circle(surface, gear_color, (x, y), int(inner_radius))
    pygame.draw.circle(surface, tooth_color, (x, y), int(inner_radius * 0.3))

gears = [
    [width // 3, height // 2, 50, 20, 0.02],
    [2 * width // 3, height // 2 + 20, 70, 30, -0.015],
    [width // 4 + 20, height // 4, 30, 12, 0.03]
]
gear_angles = [0.0] * len(gears)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("lightblue")

    for i, gear_data in enumerate(gears):
        x, y, radius, num_teeth, speed = gear_data
        gear_angles[i] += speed
        draw_gear(screen, int(x), int(y), int(radius), num_teeth, gear_angles[i])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
