class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    # @staticmethod
    # def pr_l(mass):
    #     x=[]
    #     for i in range(len(mass)):
    #         x= []
    #         for j in range(len(mass[0])):
    #             x.append(mass[i][j])
    #         print(x)

    def lighten(self, grid):
        # MappingAdapter.pr_l(grid)
        self.adaptee.set_dim((len(grid[0]), len(grid)))
        lights = []
        obstacles = []
        for i in range(len(self.adaptee.grid[0])):
            for j in range(len(self.adaptee.grid)):
                field = grid[j][i]
                if field == 1:
                    lights.append((i,j))
                elif field == -1:
                    obstacles.append((i,j))
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        l_map = self.adaptee.generate_lights()
        return l_map