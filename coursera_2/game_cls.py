#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)
FPS = 2

# =======================================================================================
# Функции, отвечающие за расчет сглаживания ломаной
# =======================================================================================
def get_point(points, alpha, deg=None):
    if deg is None:
        deg = len(points) - 1
    if deg == 0:
        return points[0]
    print(points)
    return ((points[deg] * alpha) + (get_point(points, alpha, deg - 1) * (1 - alpha)))


def get_points(base_points, count):  # count = steps
    alpha = 1 / count
    res = []
    for i in range(count):
        res.append(get_point(base_points, i * alpha))
    return res


def get_knot(points, count):
    if len(points) < 3:
        return []
    res = []
    for i in range(-2, len(points) - 2):
        ptn = []

        ptn.append((points[i] + points[i + 1]) * 0.5)
        ptn.append(points[i + 1])
        ptn.append((points[i + 1] + points[i + 2]) * 0.5)
        res.extend(get_points(ptn, count))
    return res

def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))

class Vec2d:
    def __init__(self, pos):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]

    def __sub__(self, other):
        """"возвращает разность двух векторов"""

        return self.x - other.x, self.y - other.y

    def __add__(self, other):
        """возвращает сумму двух векторов"""
        pos = self.x + other.x, self.y + other.y
        sum_vec = Vec2d(pos)
        return sum_vec


    def __len__(self):
        """возвращает длину вектора"""
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        pos = (self.x * k, self.y * k)
        return Vec2d(pos)

    def int_pair(self):
        """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
        координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
        return (int(self.x), int(self.y))


class Polyline:

    def __init__(self):
        self.points = []
        self.speeds = []

    def add_point(self, new_point, speeds=(0,0)):
        self.points.append(Vec2d(new_point))
        self.speeds.append(Vec2d(speeds))

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p][0] = self.points[p][0] + self.points[p][1]
            if self.points[p][0].x > SCREEN_DIM[0] or self.points[p][0].x < 0:
                self.points[p][1] = (- self.points[p][1], self.points[p][1])
            if self.points[p][0].y > SCREEN_DIM[1] or self.points[p][0].y < 0:
                self.points[p][1] = (self.points[p][1], - self.points[p][1])

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            points_line = list(map(lambda x: x[0], self.points))
            for p_n in range(-1, len(points_line) - 1):

                pygame.draw.line(gameDisplay, color,
                                 points_line[p_n][0].int_pair(),
                                 points_line[p_n+1][0].int_pair(), width)

        elif style == "points":
            for p in self.points:
                x,y = p[0].int_pair()
                pygame.draw.circle(gameDisplay, color, (x, y), width)

class Knot(Polyline):

    def draw_points(self, steps=1, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            points_draw = list(map(lambda x: x, self.points))
            points = get_knot(points_draw, count=steps)


            for p_n in range(-1, len(points) - 1):
                print(points[p_n].int_pair())
                pygame.draw.line(gameDisplay, color,
                                 points[p_n].int_pair(),
                                 points[p_n + 1].int_pair(), width)

        elif style == "points":
            for p in self.points:
                x,y = p.int_pair()
                pygame.draw.circle(gameDisplay, color, (x, y), width)


if __name__ == '__main__':
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    clock = pygame.time.Clock()
    pygame.display.set_caption('My')

    steps = 2
    working = True

    show_help = False
    pause = True
    hue = 0
    color = pygame.Color(0)
    points = Knot()

    while working:
        speeds = []
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                speeds = (random.random() * 2,random.random() * 2)
                points.add_point(event.pos, speeds)



        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)

        points.draw_points()
        points.draw_points(steps, style='line', width=3, color=color)
        if not pause:
            points.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)