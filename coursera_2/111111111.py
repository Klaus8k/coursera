class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        self.adaptee.set_dim(len(grid[0]), len(grid))

        for i in range(len(self.adaptee.dim)):
            for j in range(len(self.adaptee.dim)):
                field = self.adaptee.dim[i][j]
                if field == 1:
                    self.adaptee.set_lights(i,j)
                elif field == -1:
                    self.adaptee.set_obstacles(i,j)
        l_map = self.adaptee.generate_lights()
        return l_map