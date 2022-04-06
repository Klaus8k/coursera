from abc import ABC, abstractmethod
import pygame
import random


def create_sprite(img, sprite_size):
    icon = pygame.image.load(img).convert_alpha()
    icon = pygame.transform.scale(icon, (sprite_size, sprite_size))
    sprite = pygame.Surface((sprite_size, sprite_size), pygame.HWSURFACE)
    sprite.blit(icon, (0, 0))
    return sprite


class Interactive(ABC):
    pass


class AbstractObject(ABC):

    @abstractmethod
    def __init__(self, position, min_x, sprite):
        self.position = position
        self.min_x = min_x
        self.sprite = sprite

    def draw(self, canval):
        canval.blit(self.sprite, self.position)


class Ally(AbstractObject, Interactive):

    def __init__(self, icon, action, position):
        self.sprite = icon
        self.action = action
        self.position = position

    def interact(self, engine, hero):
        self.action(engine, hero)


class Creature(AbstractObject):

    def __init__(self, icon, stats, position):
        self.sprite = icon
        self.stats = stats
        self.position = position
        self.calc_max_HP()
        self.hp = self.max_hp

    def calc_max_HP(self):
        self.max_hp = 5 + self.stats["endurance"] * 2


class Hero(Creature):

    def __init__(self, stats, icon):
        pos = [1, 1]
        self.level = 1
        self.exp = 0
        self.gold = 0
        super().__init__(icon, stats, pos)

    def level_up(self):

        if self.exp >= 100 * (2 ** (self.level - 1)):
            self.level += 1
            self.stats["strength"] += 2
            self.stats["endurance"] += 2
            self.calc_max_HP()
            self.hp = self.max_hp
            return "------level up!---------"

    #  Реализовать смерть героя
    def die(self):
        print(111111111111111)


class Effect(Hero):

    def __init__(self, base):
        self.base = base
        self.stats = self.base.stats.copy()
        # self.apply_effect()

    @property
    def position(self):
        return self.base.position

    @position.setter
    def position(self, value):
        self.base.position = value

    @property
    def level(self):
        return self.base.level

    @level.setter
    def level(self, value):
        self.base.level = value

    @property
    def gold(self):
        return self.base.gold

    @gold.setter
    def gold(self, value):
        self.base.gold = value

    @property
    def hp(self):
        return self.base.hp

    @hp.setter
    def hp(self, value):
        self.base.hp = value

    @property
    def max_hp(self):
        return self.base.max_hp

    @max_hp.setter
    def max_hp(self, value):
        self.base.max_hp = value

    @property
    def exp(self):
        return self.base.exp

    @exp.setter
    def exp(self, value):
        self.base.exp = value

    @property
    def sprite(self):
        return self.base.sprite

    # Абстрактный метод наложенных эффектов
    # @abstractmethod
    # def apply_effect(self):
    #     pass


class Enemy(Creature):
    def __init__(self, icon, stats, experience, position):
        self.sprite = icon
        self.stats = stats
        self.position = position
        self.experience = experience

    def interact(self, engine, hero):
        for i in range(0, self.stats['strength']):
            damage = self.stats['endurance']
            hero.hp -= damage
            engine.notify('Урон {}'.format(damage))

        hero.exp += self.experience
        engine.notify(hero.level_up())

        # if hero.hp < 0:  # Реализовать смерть героя
        #     hero.die()


# FIXME
# Задать класс объектов сундука и лестницы

# https://github.com/Searge/mipt_oop/tree/master/week_5/final_project