class Entity:
    def __init__(self, char, origin_x, origin_y,
                 width, height):
        if (origin_x < 0 or origin_y < 0 or width < 0 or height < 0):
            raise ValueError
        self.char = char
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width
        self.height = height

    def __str__(self):
        pass

    def get_representation_char(self):
        return self.char

    def get_origin_x(self):
        return self.origin_x

    def get_origin_y(self):
        return self.origin_y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def move_left(self):
        self.origin_x -= 1
        
    def can_move_left(self):
        if (self.origin_x > 0):
            return True
        return False
    
    def move_right(self):
        self.origin_x += 1

    def can_move_right(self, board_width):
        if (self.origin_x + self.width < board_width):
            return True
        return False

    def move_up(self):
        self.origin_y -= 1

    def can_move_up(self):
        if (self.origin_y > 0):
            return True
        return False
    
    def move_down(self):
        self.origin_y += 1

    def can_move_down(self, board_height):
        if (self.origin_y + self.height - 1 < board_height):
            return True
        return False
    
    def draw_on_board(self, board):
        for r in range(self.origin_y, self.origin_y + self.height):
            for c in range(self.origin_x, self.origin_x + self.width):
                board.grid[r][c] = self.char
        return board.grid
    
    def collides_with(self, other):
        if(self.origin_x + self.width < other.origin_x or self.origin_x > other.origin_x + other.width):
            return False
        if(self.origin_y + self.height < other.origin_y or self.origin_y > other.origin_y + other.height):
            return False

        return True
