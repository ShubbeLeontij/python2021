import pygame
from pygame.draw import *
import math


def ell(screen, color, x0, y0, size, angle):
    """
    Draws tilted ellipse
    screen - pygame.Surface object
    color - color; RGB tuple, for ex. (0, 0, 0) is black
    x0, y0 - ellipse coordinates
    size - ellipse size
    angle - angle of tilt
    """
    for k in range(0, 100):
        circle(screen, color, (x0 + size * 20 * math.sin(angle / 180 * math.pi) * k / 100,
                               y0 + size * 20 * math.cos(angle / 180 * math.pi) * k / 100),
               2 * size * (1 + 1 * (k / 100) ** 0.8), width=0)
        circle(screen, color, (x0 + size * 20 * math.sin(angle / 180 * math.pi) * (1 + k / 100),
                               y0 + size * 20 * math.cos(angle / 180 * math.pi) * (1 + k / 100)),
               2 * size * (2 - (k / 100) ** 1.25), width=0)


def stick(screen, color, x, y, n, size, angle):
    """
    Draws stick
    screen - pygame.Surface object
    color - stick color; RGB tuple, for ex. (0, 0, 0) is black
    x, y - stick coordinates
    n - number of ellipses in one stick
    size - stick size
    angle - angle of tilt
    """
    a = []
    b = 1
    if x[0] < y[0]:
        b = -1
    if angle < 0:
        b = b * (-1)
    for k in range(1, 101):
        a.append((x[0] + k / 100 * (y[0] - x[0]), x[1] + ((k / 100) ** (2 ** b)) * (y[1] - x[1])))
    lines(screen, color, False, a, width=2)
    for k in range(0, n):
        ell(screen, color, x[0] + (y[0] - x[0]) * (0.5 * abs((b - 1)) / 2 + k / n / 2),
            x[1] + (y[1] - x[1]) * (0.5 * abs((b - 1)) / 2 + k / n / 2), size, angle)


def bamboo(screen, color, x=200, y=225, size=15):
    """
    Draws bamboo
    screen - pygame.Surface object
    color - bamboo color; RGB tuple, for ex. (0, 0, 0) is black
    x, y - bamboo coordinates
    size - bamboo size
    """
    rect(screen, color, (x, y + size * 6, size, size * 14 / 3))
    rect(screen, color, (x, y, size, size * 16 / 3))
    polygon(screen, color, [(x + size * 2 / 3, y - size * 2 / 3), (x, y - size),
                            (x + size / 3, y - size * 13 / 3), (x + size, y - size * 14 / 3)])
    polygon(screen, color, [(x + size, y - size * 14 / 3), (x + size * 2 / 3, y - size * 73 / 15),
                            (x + size * 17 / 15, y - size * 29 / 3), (x + size * 22 / 15, y - size * 142 / 15)])
    stick(screen, color, [x - size * 13 / 3, y - size * 5 / 3], [x - size * 1 / 3, y + size / 3], 3, 1, -30)
    stick(screen, color, [x + size * 24 / 3, y - size * 25 / 3], [x + size * 4 / 3, y - size * 3], 5, 1, 30)
    stick(screen, color, [x - size * 13 / 3, y - size * 25 / 3], [x - size * 1 / 3, y - size * 5], 5, 1, -30)
    stick(screen, color, [x + size * 14 / 3, y - size * 5 / 3], [x + size * 4 / 3, y + size / 3], 3, 1, 30)


def panda(screen, color_1, color_2, x=600, y=300, size=25):
    """
    Draws cute panda
    screen - pygame.Surface object
    color_1, color_2 - colors of different parts of panda; RGB tuple, for ex. (0, 0, 0) is black
    x, y - panda coordinates
    size - panda size
    """
    ellipse(screen, color_2, (x + size * 2, y - size * 2, size * 10, size * 34 / 5))
    ellipse(screen, color_1, (x + size / 25 * 240, y + size / 25 * 30, size * 2, size * 24 / 5))
    circle(screen, color_1, (x + size / 25 * 250, y + size / 25 * 130), size)
    polygon(screen, color_1, [(x + size / 25 * 245, y + size * 2), (x + size / 25 * 260, y + size / 25 * 140),
                              (x + size / 25 * 225, y + size / 25 * 130)])
    polygon(screen, color_1, [(x + size / 25 * 220, y - size * 2), (x + size / 25 * 220, y + size / 25 * 100),
                              (x + size / 25 * 180, y + size / 25 * 130), (x + size / 25 * 150, y + size / 25 * 157),
                              (x + size / 25 * 135, y + size / 25 * 100), (x + size / 25 * 160, y + size / 25 * 70)])
    circle(screen, color_1, (x + size / 25 * 140, y + size / 25 * 130), size * 6 / 5)
    ellipse(screen, color_1, (x + size / 25 * 40, y - size / 25 * 30, size * 16 / 5, size * 36 / 5))
    ellipse(screen, color_2, (x + size / 25 * 30, y - size / 25 * 80, size * 32 / 5, size * 36 / 5))
    polygon(screen, color_2, [(x + size / 25 * 190, y + size / 25 * 10), (x + size / 25 * 190, y + size * 2),
                              (x + size / 25 * 170, y + size / 25 * 80), (x + size / 25 * 110, y + size / 25 * 100)])
    polygon(screen, color_1, [(x + size / 25 * 70, y - size / 25 * 60), (x + size / 25 * 30, y - size),
                              (x + size / 25 * 20, y - size * 2), (x + size * 2, y - size / 25 * 70)])
    ellipse(screen, color_1, (x + size / 25 * 150, y - size / 25 * 70, size * 8 / 5, size * 14 / 5))
    ellipse(screen, color_1, (x + size * 2, y + size / 25 * 65, size * 8 / 5, size))
    circle(screen, color_1, (x + size / 25 * 60, y + size / 25 * 30), size * 4 / 5)
    circle(screen, color_1, (x + size / 25 * 110, y + size / 25 * 30), size * 4 / 5)


pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 500))
GREEN = (0, 100, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 160, 110)

# draw background
rect(screen, PINK, (0, 0, 1000, 500))

# draw 4 bamboo
bamboo(screen, GREEN, 200, 225, 15)
bamboo(screen, GREEN, 400, 225, 15)
bamboo(screen, GREEN, 800, 225, 15)
bamboo(screen, GREEN, 600, 225, 20)

# draw one big and one small panda
panda(screen, BLACK, WHITE, 600, 300, 25)
panda(screen, BLACK, WHITE, 490, 420, 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
