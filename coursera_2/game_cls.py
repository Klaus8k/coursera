#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)

# Вектор от начала координат
class Vec2d():
    def __init__(self, pos: set):
        self.x = pos[0]
        self.y = pos[1]

    def __sub__(self, x, y):
        """"возвращает разность двух векторов"""
        return self.x[0] - self.y[0], self.x[1] - self.y[1]

    def __add__(self, x, y):
        """возвращает сумму двух векторов"""
        return self.x[0] + y[0], self.x[1] + y[1]

    def len(self, x):
        """возвращает длину вектора"""
        return math.sqrt(self.x[0] * self.x[0] + self.x[1] * self.x[1])
    # Что то хуйня какая то
    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        return self[0] * k, self[1] * k

    def int_pair(self, x, y):
        """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
        координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
        return self.__sub__(y, x)


class Polyline():
    def __init__(self, points_obj):
        self.points_obj = points_obj
        self.points_obj = []
        self.speeds = []

    def add_point(self, vec: object, speed):
        self.points_obj.append(vec)
        self.speeds.append(speed)

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        points = list(map(lambda x: x, self.points_obj))
        for p in range(len(self.points_obj)):
            points[p] = (points[p][0] + self.speeds[p][0], points[p][1] + self.speeds[p][1])
            if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
                self.speeds[p] = (- self.speeds[p][0], self.speeds[p][1])
            if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
                self.speeds[p] = (self.speeds[p][0], -self.speeds[p][1])


    def draw_points(points, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(points[p_n][0]), int(points[p_n][1])),
                                 (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0]), int(p[1])), width)






