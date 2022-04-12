import time
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
    @abstractmethod
    def interact(self, engine, hero):
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


class Objects(Interactive):
    def __init__(self, icon, action, position):
        self.sprite = icon
        self.position = position
        self.action = action

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
            self.stats["strength"] += 10
            self.stats["endurance"] += 10
            self.calc_max_HP()
            self.hp = self.max_hp
            return 'LEVEL UP'


class Enemy(Creature):
    def __init__(self, icon, stats, experience, position):
        self.sprite = icon
        self.stats = stats
        self.hp = self.stats["strength"]
        self.position = position
        self.experience = experience

    def interact(self, engine, hero):
        engine.notify('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        while True:
            hero_hit = hero.stats["strength"] * random.randint(1,hero.stats["luck"])
            enemy_hit = self.stats["strength"] * (random.randint(1,self.stats["luck"])/2)
            if random.randint(0, 20) < 15:
                hero.hp -= enemy_hit
                message = 'Враг нанес {} урона'.format(enemy_hit)
            else:
                message = 'Враг промахнулся'
            engine.notify(message)

            if hero.hp <= 0:
                engine.notify("Герой погиб. R - для рестарта")
                engine.show_help = True
                break
            elif self.hp <= 0:
                message = "Враг повержен! За победу: " + str(self.experience) + " xp"
                engine.notify(message)
                break
            else:
                self.hp -= hero_hit
                engine.notify('Вы нанесли {} урона'.format(hero_hit))

        hero.exp += self.experience
        engine.notify('>>>>>>>>>>>>>>>>>>>>>>>>>>>')

        if hero.exp >= 100 * (2 ** (hero.level - 1)):
            engine.notify("level up!")
            hero.level += 1
            hero.stats["strength"] += 2
            hero.stats["endurance"] += 4
            hero.calc_max_HP()
            hero.hp = hero.max_hp

class Effect(Hero):

    def __init__(self, base):
        self.base = base
        self.stats = self.base.stats.copy()

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
        if self.base.max_hp < value:
            self.base.hp = self.base.max_hp
        else: self.base.hp = value

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

    @abstractmethod
    def apply_effect(self):
        pass


class Blessing(Effect):
    def __init__(self, base):
        self.base = base
        self.stats = self.base.stats.copy()
        self.apply_effect()

    def apply_effect(self):
        self.stats['luck'] *= 2
        return self.stats


class Berserk(Effect):
    def __init__(self, base):
        self.base = base
        self.stats = self.base.stats.copy()
        self.apply_effect()

    def apply_effect(self):
        self.stats['strength'] *= 2
        self.stats['endurance'] += 20
        return self.stats


class Weakness(Effect):
    def __init__(self, base):
        self.base = base
        self.stats = self.base.stats.copy()
        self.apply_effect()

    def apply_effect(self):
        self.stats['strength'] -= 5
        return self.stats