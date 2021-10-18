class Board:
    EMPTY_SLOT = "_"

    def __init__(self, width, height):
        if (width < 0 or width < 0):
            raise ValueError
        self.width = width
        self.height = height
        self.grid = self.init_grid()

    def reset(self):
        self.grid = self.init_grid()

    # Initialize grid to be 2D list of underscores.
    # I had to initialize this 2D list using the trick
    # described here (https://stackoverflow.com/a/44382900/7020654),
    # to avoid extremely bizarre behavior.
    def init_grid(self):
        return [[Board.EMPTY_SLOT] * self.width \
                for i in range(self.height)]

    def print(self):
        for row in self.grid:
            print(row)
