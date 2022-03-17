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