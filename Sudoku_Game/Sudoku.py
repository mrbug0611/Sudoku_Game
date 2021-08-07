from pygame import *

init()
screen_width = 800
screen_height = 600
screen = display.set_mode((screen_width, screen_height))
display.set_caption('Sudoku')
icon = image.load('sudoku_logo.png')
display.set_icon(icon)

screen.fill((255, 255, 255))

num_font = font.Font('freesansbold.ttf', 60)

class ESpace:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
        self.active = False

        self.text = num_font.render(player, True, (0, 0, 255))
        self.click_value = 65

    def naming(self, events):
        for e in events:
            if e.type == MOUSEBUTTONDOWN:
                if self.x + self.click_value-20 >= mx >= self.x - 14 and self.y + 45 >= my >= self.y - 10:
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

    def draw(self, screen):
        screen.blit(self.text, (self.x + 5, self.y + 5))


squares = []


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


num_matrix = [2, 0, 0, 0, 0, 3, 0, 9, 0,
              0, 0, 5, 2, 6, 0, 4, 7, 0,
              0, 0, 0, 0, 0, 7, 0, 0, 3,
              3, 1, 2, 5, 4, 6, 0, 0, 0,
              4, 0, 6, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 6, 0, 0,
              0, 2, 1, 0, 0, 0, 9, 6, 0,
              8, 0, 4, 9, 0, 0, 0, 0, 0,
              9, 7, 0, 0, 2, 0, 8, 1, 4]


def grid_numbers():
    num_x = 120
    num_y = 15
    for i in range(len(num_matrix)):
        if (i % 9) == 0 and i != 0:
            num_x = 120
            num_y += 63
        if num_matrix[i] != 0:
            num_text = num_font.render(str(num_matrix[i]), True, (0, 0, 255))
            screen.blit(num_text, (num_x, num_y))
            num_x += 66.5
        if num_matrix[i] == 0:
            squares.append(ESpace(num_x, num_y, ''))
            num_x += 66.5


while True:
    events = event.get()
    mx, my = mouse.get_pos()

    for e in events:
        if e.type == QUIT:
            quit()

    screen.fill((255, 255, 255))

    draw_big_grid(100, 10, 100, 580, True)
    draw_big_grid(100, 10, 701, 10, False)

    draw_small_grid(100, 10, 100, 580, True)
    draw_small_grid(100, 10, 701, 10, False)

    grid_numbers()

    for sq in squares:
        sq.naming(events)
        sq.draw(screen)

    display.update()
    time.delay(1)
