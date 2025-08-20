import pygame
import sys
import random

pygame.init()

width, height = 600, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drifting Squares")

num_squares = 20
squares = []
for _ in range(num_squares):
    size = random.randint(20, 50)
    x = random.randint(0, width - size)
    y = random.randint(0, height - size)
    speed_x = random.uniform(-2, 2)
    speed_y = random.uniform(-2, 2)
    color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    squares.append([pygame.Rect(x, y, size, size), speed_x, speed_y, color])

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for i, (rect, speed_x, speed_y, color) in enumerate(squares):
        rect.x += speed_x
        rect.y += speed_y
        
        if rect.left < 0 or rect.right > width:
            speed_x *= -1
            squares[i][3] = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if rect.top < 0 or rect.bottom > height:
            speed_y *= -1
            squares[i][3] = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        squares[i][1] = speed_x
        squares[i][2] = speed_y
        pygame.draw.rect(screen, color, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
