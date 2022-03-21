from abc import ABC, abstractmethod


class ObservableEngine(Engine):
    def __init__(self):
        self.subscribers = set()

    def subscribe(self, name):
        self.subscribers.add(name)

    def unsubscribe(self, name):
        self.subscribers.remove(name)

    def notify(self, achiv: dict):
        for i in self.subscribers:
            i.update(achiv)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achiv):
        self.achievements.add(achiv['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, achiv):
        if achiv not in self.achievements:
            self.achievements.append(achiv)
