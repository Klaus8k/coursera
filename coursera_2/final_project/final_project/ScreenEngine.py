import pygame
import collections

colors = {
    "black": (0, 0, 0, 255),
    "white": (255, 255, 255, 255),
    "red": (255, 0, 0, 255),
    "green": (0, 255, 0, 255),
    "blue": (0, 0, 255, 255),
    "wooden": (153, 92, 0, 255),
}


class ScreenHandle(pygame.Surface):

    def __init__(self, *args, **kwargs):
        if len(args) > 1:
            self.successor = args[-1]
            self.next_coord = args[-2]
            args = args[:-2]
        else:
            self.successor = None
            self.next_coord = (0, 0)
        super().__init__(*args, **kwargs)
        self.fill(colors["wooden"])

    def draw(self, canvas):
        if self.successor is not None:
            canvas.blit(self.successor, self.next_coord)
            self.successor.draw(canvas)

    # FIXME connect_engine
    def connect_engine(self, engine):
        pass
        # if self.successor is not None:
        #     self.successor.connect_engine(engine)


class GameSurface(ScreenHandle):

    # FIXME save engine and send it to next in chain
    def connect_engine(self, engine):
        self.game_engine = engine
        if self.successor is not None:
            self.successor.connect_engine(engine)

    def draw_hero(self):
        hero = self.game_engine.hero
        self.draw_object(hero.sprite, hero.position)

    def draw_map(self):
        min_x, min_y = self.calculate()

        if self.game_engine.map:
            for i in range(len(self.game_engine.map[0]) - min_x):
                for j in range(len(self.game_engine.map) - min_y):
                    self.blit(self.game_engine.map[min_y + j][min_x + i][
                                  0],
                              (i * self.game_engine.sprite_size, j * self.game_engine.sprite_size))
        else:
            self.fill(colors["white"])

    def draw_object(self, sprite, coord):
        size = self.game_engine.sprite_size

        min_x, min_y = self.calculate()
        self.blit(sprite, ((coord[0] - min_x) * size,
                           (coord[1] - min_y) * size))

    def draw(self, canvas):
        size = self.game_engine.sprite_size
        min_x, min_y = self.calculate()
        self.draw_map()
        for obj in self.game_engine.objects:
            self.blit(obj.sprite[0], ((obj.position[0] - min_x) * size,
                                      (obj.position[1] - min_y) * size))
        self.draw_hero()

        # draw next surface in chain
        if self.successor is not None:
            canvas.blit(self.successor, self.next_coord)
            self.successor.draw(canvas)

    # FIXME || calculate (min_x,min_y) - left top corner(5 free sprites)
    def calculate(self):
        screen_size = list(self.get_size())
        screen_size[0] /= self.game_engine.sprite_size
        screen_size[1] /= self.game_engine.sprite_size
        hero_pos = self.game_engine.hero.position
        min_x = int(max(0, hero_pos[0] - screen_size[0] + 5))
        min_y = int(max(0, hero_pos[1] - screen_size[1] + 5))
        return (min_x, min_y)


class ProgressBar(ScreenHandle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fill(colors["wooden"])

    # FIXME save engine and send it to next in chain
    def connect_engine(self, engine):
        self.engine = engine
        if self.successor is not None:
            self.successor.connect_engine(engine)

    def draw(self, canvas):
        self.fill(colors["wooden"])
        pygame.draw.rect(self, colors["black"], (50, 30, 200, 30), 2)
        pygame.draw.rect(self, colors["black"], (50, 70, 200, 30), 2)

        pygame.draw.rect(self, colors["red"], (50, 30, 200 * self.engine.hero.hp / self.engine.hero.max_hp, 30))
        pygame.draw.rect(self, colors["green"], (50, 70, 200 * self.engine.hero.exp /
                                                 (100 * (2 ** (self.engine.hero.level - 1))), 30))

        font = pygame.font.SysFont("arial", 14)
        font_b = pygame.font.SysFont("arial", 14)
        font_b.bold = True

        self.blit(font.render(f'{self.engine.level} floor', True, colors["black"]),
                  (10, 0))

        self.blit(font.render(f'Hero at {self.engine.hero.position}', True, colors["black"]),
                  (100, 0))

        # ?????????????? ???????????????????? ???? ??????????
        self.blit(font.render(f'{self.engine.hero.stats}', True, colors["black"]),
                  (230, 0))

        self.blit(font.render(f'HP', True, colors["black"]),
                  (10, 30))
        self.blit(font.render(f'EXP', True, colors["black"]),
                  (10, 70))

        self.blit(
            font_b.render(f'{self.engine.hero.hp}/{self.engine.hero.max_hp}', True, colors["black"]),
            (60, 30))
        self.blit(
            font_b.render(f'{self.engine.hero.exp}/{(100 * (2 ** (self.engine.hero.level - 1)))}',
                          True, colors["black"]),
            (60, 70))

        self.blit(font.render(f'LEVEL', True, colors["black"]),
                  (300, 30))
        self.blit(font.render(f'GOLD', True, colors["black"]),
                  (300, 70))

        self.blit(font_b.render(f'{self.engine.hero.level}', True, colors["black"]),
                  (360, 30))
        self.blit(font_b.render(f'{self.engine.hero.gold}', True, colors["black"]),
                  (360, 70))

        self.blit(font.render(f'STR', True, colors["black"]),
                  (420, 30))
        self.blit(font.render(f'LUCK', True, colors["black"]),
                  (420, 70))

        self.blit(font_b.render(f'{self.engine.hero.stats["strength"]}', True, colors["black"]),
                  (480, 30))
        self.blit(font_b.render(f'{self.engine.hero.stats["luck"]}', True, colors["black"]),
                  (480, 70))

        self.blit(font.render(f'SCORE', True, colors["black"]),
                  (550, 30))
        self.blit(font_b.render(f'{self.engine.score:.4f}', True, colors["black"]),
                  (550, 70))

        # draw next surface in chain
        if self.successor is not None:
            canvas.blit(self.successor, self.next_coord)
            self.successor.draw(canvas)


class InfoWindow(ScreenHandle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.len = 30
        clear = []
        self.data = collections.deque(clear, maxlen=self.len)

    def update(self, value):
        self.data.append(f"> {str(value)}")

    def draw(self, canvas):
        self.fill(colors["wooden"])
        # size = self.get_size()

        font = pygame.font.SysFont("arial", 15)
        for i, text in enumerate(self.data):
            self.blit(font.render(text, True, colors["black"]),
                      (5, 20 + 18 * i))

        # FIXME
        # draw next surface in chain
        if self.successor is not None:
            canvas.blit(self.successor, self.next_coord)
            self.successor.draw(canvas)

    # FIXME set this class as Observer to engine and send it to next in
    # chain
    def connect_engine(self, engine):
        self.engine = engine
        self.engine.subscribe(self)
        if self.successor is not None:
            self.successor.connect_engine(engine)


class HelpWindow(ScreenHandle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.len = 30
        clear = []
        self.data = collections.deque(clear, maxlen=self.len)
        self.data.append([" ???", "Move Right"])
        self.data.append([" ???", "Move Left"])
        self.data.append([" ??? ", "Move Top"])
        self.data.append([" ??? ", "Move Bottom"])
        self.data.append([" H ", "Show Help"])
        self.data.append(["Num+", "Zoom +"])
        self.data.append(["Num-", "Zoom -"])
        self.data.append([" R ", "Restart Game"])

    # FIXME You can add some help information

    # def connect_engine(self, engine):
    # FIXME save engine and send it to next in chain
    def connect_engine(self, engine):
        self.engine = engine
        if self.successor is not None:
            self.successor.connect_engine(engine)

    def draw(self, canvas):
        alpha = 0
        if self.engine.show_help:
            alpha = 128
        self.fill((0, 0, 0, alpha))
        size = self.get_size()
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        if self.engine.show_help:
            pygame.draw.lines(self, (255, 0, 0, 255), True, [
                (0, 0), (700, 0), (700, 500), (0, 500)], 5)
            for i, text in enumerate(self.data):
                self.blit(font1.render(text[0], True, ((128, 128, 255))),
                          (50, 50 + 30 * i))
                self.blit(font2.render(text[1], True, ((128, 128, 255))),
                          (150, 50 + 30 * i))
        # FIXME
        # draw next surface in chain
        if self.successor is not None:
            canvas.blit(self.successor, self.next_coord)
            self.successor.draw(canvas)
