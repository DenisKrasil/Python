# Создайте программу для игры в ""Крестики-нолики"".

import pygame
import sys

def win(list, sign):
    zeros = 0
    for row in list:
        zeros += row.count(0)
        if row in list:
            if row.count(sign)==3:
                return sign
    for column in range(3):
        if list[0][column] == sign and list[1][column] == sign and list[2][column] == sign:
            return f'{sign} - победитель'
    if list[0][0] == sign and list[1][1] == sign and list[2][2] == sign:
            return f'{sign} - победитель'
    if list[0][2] == sign and list[1][1] == sign and list[2][0] == sign:
            return f'{sign} - победитель'
    if zeros==0:
        return 'Ничья'
    return False


pygame.init()
size_block = 100
margin=5
width=height=size_block * 3 + margin * 4
size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики-нолики')

black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255) 
list1 = [[0]*3 for i in range(3)]
query = 0 
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            column = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if list1[row][column] == 0:
                if query%2==0:
                    list1[row][column] = 'X'
                else:
                    list1[row][column] = 'O'
                query += 1
    if not game_over:
        for row in range(3):
            for column in range(3):
                if list1[row][column] == 'X':
                    color = blue
                elif list1[row][column] == 'O':
                    color = red
                else:
                    color=white
                x = column*size_block + (column+1)*margin
                y = row * size_block + (row+1)*margin
                pygame.draw.rect(screen, color, (x,y, size_block, size_block))
                if color==blue:
                    pygame.draw.line(screen,white, (x+10,y+10), (x + size_block-10, y + size_block-10), 5)
                    pygame.draw.line(screen,white, (x + size_block-10,y+10), (x+10, y + size_block-10), 5)
                elif color==red:
                    pygame.draw.circle(screen,white, (x + size_block//2, y + size_block//2),size_block//2-10,5)

    if (query-1)%2==0:
        game_over = win(list1,'X')
    else:
        game_over = win(list1,'O')
    
    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('bitstreamverasans', 50)
        text1 = font.render(game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width()/2 - text_rect.width /2
        text_y = screen.get_height()/2 - text_rect.height /2
        screen.blit(text1, [text_x, text_y])
    pygame.display.update()
    