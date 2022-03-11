#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


# Вектор от начала координат
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
        return self.x + other.x, self.y + other.y

    def __len__(self):
        """возвращает длину вектора"""
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        return self.x * k, self.y * k

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
            if self.points[p][0][0] > SCREEN_DIM[0] or self.points[p][0][0] < 0:
                self.points[p][1] = (- self.points[p][1], self.points[p][1])
            if self.points[p][0][1] > SCREEN_DIM[1] or self.points[p][0][1] < 0:
                self.points[p][1] = (self.points[p][1], - self.points[p][1])

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 self.points[p_n][0].int_pair(),
                                 self.points[p_n+1][0].int_pair(), width)

        elif style == "points":
            for p in self.points:
                x,y = p[0].int_pair()
                print(x, y)
                pygame.draw.circle(gameDisplay, color, (x, y), width)


if __name__ == '__main__':
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    clock = pygame.time.Clock()
    pygame.display.set_caption('My')

    working = True
    x = Polyline()

    while working:
        clock.tick(3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x.add_point(Vec2d(event.pos))


        gameDisplay.fill((0, 0, 0))
        x.draw_points()
        if len(x.points) > 1:
            x.draw_points(style='line')
        print(x.points)
        pygame.display.flip()


