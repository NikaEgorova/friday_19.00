import pygame
import sys
import random
pygame.init()

GREEN = (5, 150, 12)
LIGHT_GREEN = (102,235,0)
F_COLOR = (1,50,32)
HEADER_COLOR = (102,204,0)
SNAKE_COLOR = (45,55,225)
BLACK = (0,0,0)
RED = (250,30,30)
MARGIN = 1
HEADER_MARGIN = 70
COUNT_BLOCK = 25
SIZE_BLOCK = 20
size = [SIZE_BLOCK * COUNT_BLOCK + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK,SIZE_BLOCK * COUNT_BLOCK + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK + HEADER_MARGIN]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake game')
timer = pygame.time.Clock()
print(size)

class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def check_inside(self):
        return 0<=self.x<COUNT_BLOCK and 0<= self.y<COUNT_BLOCK

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y

def get_random_block():
    x = random.randint(0, COUNT_BLOCK - 1)
    y = random.randint(0,COUNT_BLOCK - 1)
    randomblock = SnakeBlock(x,y)
    while randomblock in snake_blocks:
        randomblock.x = random.randint(0, COUNT_BLOCK - 1)
        randomblock.y = random.randint(0, COUNT_BLOCK - 1)
    return randomblock

def message(msg, color):
    mesg = end_game_style.render(msg, True, color)
    screen.blit(mesg, [25, size[0]/2])

def draw_block(color, row, column):
    pygame.draw.rect(screen,color,[SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column+1),HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row+1),SIZE_BLOCK,SIZE_BLOCK])

courier = pygame.font.SysFont('courier', 38)
end_game_style = pygame.font.SysFont("bahnschrift", 22)
snake_blocks = [SnakeBlock(9,8), SnakeBlock(9,9), SnakeBlock(9,10)]
food = get_random_block()
d_row = 0 
d_col = 1
total = 0
speed = 5
def gameLoop():
    game_over = False
    game_close = False
    d_row = 0 
    d_col = 1
    total = 1
    speed = 5
    snake_blocks = [SnakeBlock(9,8), SnakeBlock(9,9), SnakeBlock(9,10)]
    food = get_random_block()
    while not game_over:
        
        while game_close == True:
            message("Ви програли! Нажміть C-грати знову або Q-вийти", BLACK)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    d_row = -1
                    d_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    d_row = 1
                    d_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:
                    d_row = 0
                    d_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    d_row = 0
                    d_col = 1

        screen.fill(F_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0,0,size[0], HEADER_MARGIN])

        text_total = courier.render(f"Зібрано:{total}", 0, BLACK)
        screen.blit(text_total, (SIZE_BLOCK,SIZE_BLOCK))
        text_speed = courier.render(f" Швидкість:{speed}", 0, BLACK)
        screen.blit(text_speed, (SIZE_BLOCK+230,SIZE_BLOCK))

        for row in range(COUNT_BLOCK):
            for coloun in range(COUNT_BLOCK):
                if (row + coloun) % 2==0:
                    color = LIGHT_GREEN
                else:
                    color = GREEN

                draw_block(color, row, coloun)

        head = snake_blocks[-1]
        if not head.check_inside():
            game_close = True

        draw_block(RED, food.x, food.y)
        for block in snake_blocks:
            draw_block(SNAKE_COLOR, block.x, block.y)
        
        if food == head:
            total += 1
            if total%5==0:
                speed += 1
                if speed >= 15:
                    speed = 15
            snake_blocks.append(food)
            food = get_random_block()
        
        if total == (COUNT_BLOCK * COUNT_BLOCK):
            text_win = courier.render(f" Ви перемогли!Нажміть q, щоб вийти", 0, BLACK)
            screen.blit(text_win, (25, size[0]/2))

        new_head = SnakeBlock(head.x + d_row, head.y + d_col)
        if new_head in snake_blocks:
            game_close = True
        snake_blocks.append(new_head)
        snake_blocks.pop(0)
        
        pygame.display.flip()
        timer.tick(speed)
    pygame.quit()
    quit()
gameLoop()
