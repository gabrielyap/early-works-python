from board import Board
from entity import Entity

class Game:
    def __init__(self, input_file_name):
        self.board = None
        self.hero = None
        self.enemies = []
        f = open(input_file_name)
        line1 = f.readline()
        self.board = Board(int(line1.split()[0]), int(line1.split()[1]))
        line2 = f.readline()
        self.hero = Entity(Game.parse_entity_line(line2)[0], Game.parse_entity_line(line2)[1], Game.parse_entity_line(line2)[2], Game.parse_entity_line(line2)[3], Game.parse_entity_line(line2)[4])
        line = f.readline()
        while line != "":
            newEnt = Entity(Game.parse_entity_line(line)[0], Game.parse_entity_line(line)[1], Game.parse_entity_line(line)[2], Game.parse_entity_line(line)[3], Game.parse_entity_line(line)[4])
            self.enemies.append(newEnt)
            line = f.readline()
        f.close()
        
    # Optional helper function.
    # You don't have to use it, if you don't want to.
    def parse_entity_line(line):
        char,origin_x,origin_y,width,height = line.split()
        return char,int(origin_x),int(origin_y),\
            int(width),int(height)
    
    def write_entities(self, output_file_name):
        pass

    def run(self):
        while len(self.enemies) > 0:
            self.display_game()
            choice = input("Enter: ")
            if choice == "l":  # left
                if self.hero.can_move_left():
                    self.hero.move_left()
                    self.check_collisions()
            elif choice == "r":  # right
                if self.hero.can_move_right(self.board.width):
                    self.hero.move_right()
                    self.check_collisions()
            elif choice == "u":  # up
                if self.hero.can_move_up():
                    self.hero.move_up()
                    self.check_collisions()
            elif choice == "d":  # down
                if self.hero.can_move_down(self.board.height):
                    self.hero.move_down()
                    self.check_collisions()
            elif choice[0] == "s":  # save
                option,file_name = choice.split()
                self.write_entities(file_name)
            elif choice == "q":  # quit
                print("You are not a winner!")
                return False
        # User won.
        self.display_game()
        print("You are a winner!")
        return True

    def check_collisions(self):
        i = 0
        while i < len(self.enemies):
            enemy = self.enemies[i]
            if enemy.collides_with(self.hero):
                del self.enemies[i]
            else:
                i += 1

    def display_game(self):
        self.board.reset()
        self.draw_game()
        self.board.print()

    def draw_game(self):
        self.hero.draw_on_board(self.board)
        for enemy in self.enemies:
            enemy.draw_on_board(self.board)


