#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)
FPS = 5

# =======================================================================================
# Функции, отвечающие за расчет сглаживания ломаной
# =======================================================================================
def get_point(points, alpha, deg=None):
    if deg is None:
        deg = len(points) - 1
    if deg == 0:
        return points[0]
    return (points[deg] * alpha) + (get_point(points, alpha, deg - 1) * (1 - alpha))


def get_points(base_points, count):  # count = steps
    alpha = 1 / count
    res = []
    for i in range(count):
        res.append(get_point(base_points, i * alpha))
    return res


def get_knot(points, count):
    k = 0.5
    if len(points) < 3:
        return []
    res = []
    for i in range(-2, len(points) - 2):
        ptn = []
        ptn.append((points[i] + points[i + 1]) * k)
        ptn.append(points[i + 1])
        ptn.append((points[i + 1] + points[i + 2]) * k)
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
        self.pos = (self.x - other.x, self.y - other.y)
        return self

    def __add__(self, other):
        """возвращает сумму двух векторов"""
        self.pos = (self.x + other.x, self.y + other.y)
        return self

    def __len__(self):
        """возвращает длину вектора"""
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        self.pos = (self.x * k, self.y * k)
        return self

    def int_pair(self):
        """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
        координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
        return (int(self.x), int(self.y))


class Polyline:

    def __init__(self):
        self.points = []

    def add_point(self, new_point: object, speeds=(0, 0)):
        self.points.append((new_point, speeds))

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

    def reshape(self, step):
        p_n = list(map(lambda x: x[0], self.points))
        print(p_n)
        points_line = get_knot(p_n, count=step)
        Knot.draw_line(points_line)

    @staticmethod
    def draw_line(points_line, width=3, color=(255, 255, 255)):
        for p_n in range(-1, len(points_line) - 1):
            print(points_line[p_n].int_pair())
            pygame.draw.line(gameDisplay, color,
                             points_line[p_n].int_pair(),
                             points_line[p_n + 1].int_pair(), width)








if __name__ == '__main__':
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    clock = pygame.time.Clock()
    pygame.display.set_caption('My')

    steps = 5
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
                speeds.append((random.random() * 2,
                               random.random() * 50))
                points.add_point(Vec2d(event.pos), speeds)



        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)

        points.draw_points()
        # Перерисовка со сглаживанием
        # draw_points(get_knot(points, steps), "line", 3, color)
        points.reshape(steps)
        if not pause:
            points.reshape(steps)
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)