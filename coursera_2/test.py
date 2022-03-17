from abc import ABC, abstractmethod

class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1  # Источники света
        self.map[5][2] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)

class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        self.adaptee.set_dim(len(grid[0]), len(grid))

        for i in range(len(grid)):
            for j in range(len(grid)):
                field = grid[i][j]
                if field == 1:
                    self.adaptee.set_lights(field)
                elif field == -1:
                    self.adaptee.set_obstacles(field)
        return self.adaptee.generate_lights()


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

sys = System()
sys.lightmap(MappingAdapter(Light))