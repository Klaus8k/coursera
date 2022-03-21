from abc import ABC, abstractmethod
import adapter

class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(10)] for _ in range(5)]
        self.map[3][4] = 1  # Источники света
        self.map[3][2] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)


class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()

s = System()
dim = (len(s.map[0]), len(s.map))
x = Light(dim)
r = s.get_lightening(adapter.MappingAdapter(x))
