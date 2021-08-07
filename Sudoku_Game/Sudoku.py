# Importing Modules
from pygame import *
import sys

# Setting up window, icon, and caption,
init()
screen_width = 800
screen_height = 600
screen = display.set_mode((screen_width, screen_height))
display.set_caption('Sudoku')
icon = image.load('sudoku_logo.png')
display.set_icon(icon)

# Making screen white
screen.fill((255, 255, 255))

# Setting the font
num_font = font.Font('freesansbold.ttf', 60)


# Setting up Empty space class
class ESpace:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
        self.active = False

        self.text = num_font.render(player, True, (0, 0, 255))
        self.click_value = 65

    # allowing you to write in the empty space
    def naming(self, events):
        for e in events:
            if e.type == MOUSEBUTTONDOWN:
                if self.x + self.click_value - 20 >= mx >= self.x - 14 and self.y + 45 >= my >= self.y - 10:
                    self.active = True
                else:
                    self.active = False
            if e.type == KEYDOWN:
                if self.active:
                    if e.key == K_BACKSPACE:
                        self.player = self.player[:-1]
                        screen.fill((255, 255, 255))
                    else:
                        self.player += e.unicode
                        self.click_value += 7
                self.text = num_font.render(self.player, True, (0, 0, 0))
        return self.player

    # Dislaying the empty space
    def draw(self, screen):
        screen.blit(self.text, (int(self.x + 5), int(self.y + 5)))


# list fills up with the amount of ESpace objects
squares = []


# Draws the thick black lines of the grid
def draw_big_grid(line_start_x, line_start_y, line_end_x, line_end_y, vertical):
    for x in range(4):
        if vertical:
            draw.line(screen, (0, 0, 0), (line_start_x, line_start_y), (line_end_x, line_end_y), 5)
            line_end_x += 200
            line_start_x += 200
        else:
            draw.line(screen, (0, 0, 0), (line_start_x, line_start_y), (line_end_x, line_end_y), 5)
            line_start_y += 190
            line_end_y += 190


# Draws the thin grey lines of the grid
def draw_small_grid(line_start_x, line_start_y, line_end_x, line_end_y, vertical):
    for x in range(10):
        if vertical:
            draw.line(screen, (0, 0, 0), (line_start_x, line_start_y), (line_end_x, line_end_y))
            line_end_x += 67
            line_start_x += 67
        else:
            draw.line(screen, (0, 0, 0), (line_start_x, line_start_y), (line_end_x, line_end_y))
            line_start_y += 63
            line_end_y += 63


# The numbers of the sudoku puzzle
num_matrix = [2, 0, 0, 0, 0, 3, 0, 9, 0,
              0, 0, 5, 2, 6, 0, 4, 7, 0,
              0, 0, 0, 0, 0, 7, 0, 0, 3,
              3, 1, 2, 5, 4, 6, 0, 0, 0,
              4, 0, 6, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 6, 0, 0,
              0, 2, 1, 0, 0, 0, 9, 6, 0,
              8, 0, 4, 9, 0, 0, 0, 0, 0,
              9, 7, 0, 0, 2, 0, 8, 1, 4]


# adds numbers to the screen and empty spaces in the squares list
def grid_numbers():
    num_x = 120
    num_y = 15
    for i in range(len(num_matrix)):
        if (i % 9) == 0 and i != 0:
            num_x = 120
            num_y += 63
        if num_matrix[i] != 0:
            num_text = num_font.render(str(num_matrix[i]), True, (0, 0, 255))
            screen.blit(num_text, (int(num_x), int(num_y)))
            num_x += 66.5
        if num_matrix[i] == 0:
            squares.append(ESpace(num_x, num_y - 5, ''))
            num_x += 66.5


# main game loop
while True:
    # defining events and mouse positions
    events = event.get()
    mx, my = mouse.get_pos()

    # allows the person to quit the game
    for e in events:
        if e.type == QUIT:
            quit()
            sys.exit()

    # Makes screen white so it updates after you delete a number
    screen.fill((255, 255, 255))

    # runs drawing thick lines functions
    draw_big_grid(100, 10, 100, 580, True)
    draw_big_grid(100, 10, 701, 10, False)

    # runs drawing thin lines functions 
    draw_small_grid(100, 10, 100, 580, True)
    draw_small_grid(100, 10, 701, 10, False)
    
    # runs grid number function
    grid_numbers()
    
    # puts the empty space in the screen and allows you to type in it
    for sq in squares:
        sq.naming(events)
        sq.draw(screen)

    # updating the screen
    display.update()
    time.delay(1)
