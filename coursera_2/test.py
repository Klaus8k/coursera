from abc import ABC, abstractmethod


class AbstractEffect(ABC, Hero):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        return self.base.get_negative_effects

    @abstractmethod
    def get_stats(self):
        return self.base.get_stats()


class AbstractPositive(AbstractEffect):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    @abstractmethod
    def get_stats(self):
        return self.base.get_stats()


class AbstractNegative(AbstractEffect):
    def __init__(self, base):
        self.base = base

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        return self.base.get_negative_effects()

    @abstractmethod
    def get_stats(self):
        return self.base.get_stats()


class Berserk(AbstractPositive):
    def __init__(self, base):
        self.base = base

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] += 7
        stats['Endurance'] += 7
        stats['Agility'] += 7
        stats['Luck'] += 7
        for i in ('Charisma', 'Perception', 'Intelligence'):
            stats[i] -= 3
        stats['HP'] += 50
        return stats

    def get_positive_effects(self):
        positive_effects = self.base.get_positive_effects()
        positive_effects.append('Berserk')
        return positive_effects


class Blessing(AbstractPositive):
    def __init__(self, base):
        self.base = base

    def get_stats(self):
        stats = self.base.get_stats()
        for key in stats.keys():
            if len(key) > 2:
                stats[key] += 2
        return stats

    def get_positive_effects(self):
        positive_effects = self.base.get_positive_effects()
        positive_effects.append('Blessing')
        return positive_effects


class Weakness(AbstractNegative):
    def __init__(self, base):
        self.base = base

    def get_stats(self):
        stats = self.base.get_stats()
        for i in ('Strength', 'Endurance', 'Agility'):
            stats[i] -= 4
        return stats

    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        negative_effects.append('Weakness')
        return negative_effects


class EvilEye(AbstractNegative):
    def __init__(self, base):
        self.base = base

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Luck'] -= 10
        return stats

    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        negative_effects.append('EvilEye')
        return negative_effects


class Curse(AbstractNegative):
    def __init__(self, base):
        self.base = base

    def get_stats(self):
        stats = self.base.get_stats()
        for key in stats.keys():
            if len(key) > 2:
                stats[key] -= 2
        return stats

    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        negative_effects.append('Curse')
        return negative_effects
