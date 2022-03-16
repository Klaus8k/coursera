from abc import ABC, abstractmethod

class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()

class AbstractEffect(ABC, Hero):

    def __init__(self, base):
        self.base = base
        self.stats = self.base.get_stats()


    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass

class Berserk(AbstractEffect):


    def get_positive_effects(self):
        # x = self.base.get_positive_effects()
        return 'Bers'

    def get_stats(self):
        self.stats['HP'] += 100000000
        return self.base.get_stats()


if __name__ == '__main__':
    h = Hero()
    b1 = Berserk(h)
    b2 = Berserk(b1)
    b3 = Berserk(b2)
    print(b1.stats)
    print(b2.stats)
    print(b3.stats)

    b3.base = b3.base.base

    print(b3.get_stats())
