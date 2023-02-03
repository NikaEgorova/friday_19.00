from pygame import *

win_width = 500
win_height = 500
background = (200, 255, 255)
WIN_COLOR = (78, 255, 97)
LOSE_COLOR = (255, 42, 56)
window = display.set_mode((win_width, win_height))
clock = time.Clock()
game = True


class GameSprite(sprite.Sprite):
    def __init__(self, spr_image, spr_x, spr_y, spr_size_x, spr_size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(spr_image), (spr_size_x, spr_size_y))
        self.size_x = spr_size_x
        self.size_y = spr_size_y
        self.rect = self.image.get_rect()
        self.rect.x = spr_x
        self.rect.y = spr_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, spr_image, spr_x, spr_y, spr_size_x, spr_size_y, spr_speed_x, spr_speed_y):
        GameSprite.__init__(self, spr_image, spr_x, spr_y, spr_size_x, spr_size_y)
        self.x_speed = spr_speed_x
        self.y_speed = spr_speed_y
        self.coins = None
        self.collected_coins = 0


    def update(self):
        if self.rect.x <= win_width - self.size_x and self.x_speed > 0 or self.rect.x >= 0 and self.x_speed < 0:
            self.rect.x += self.x_speed
        walls_touched = sprite.spritecollide(self, walls, False)
        if self.x_speed > 0:
            for wall in walls_touched:
                self.rect.right = min(self.rect.right, wall.rect.left)
        elif self.x_speed < 0:
            for wall in walls_touched:
                self.rect.left = max(self.rect.left, wall.rect.right)
        if self.rect.y <= win_height - self.size_y and self.y_speed > 0 or self.rect.y >= 0 and self.y_speed < 0:
            self.rect.y += self.y_speed
        walls_touched = sprite.spritecollide(self, walls, False)
        if self.y_speed > 0:
            for wall in walls_touched:
                self.y_speed = 0
                if wall.rect.top < self.rect.bottom:
                    self.rect.bottom = wall.rect.top
        elif self.y_speed < 0:
            for wall in walls_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, wall.rect.bottom)

class Enemy_x(GameSprite):
    side = "left"
    def __init__(self, spr_image, spr_x, spr_y, spr_size_x, spr_size_y, x_left_granica, x_right_granica, x_speed, y_speed):
        GameSprite.__init__(self, spr_image, spr_x, spr_y, spr_size_x, spr_size_y)
        self.x_right_granica = x_right_granica
        self.x_left_granica = x_left_granica
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        if self.rect.x <= self.x_left_granica:
            self.side = 'right'
        if self.rect.x >= self.x_right_granica:
            self.side = 'left'

        if self.side == 'left':
            self.rect.x -= self.x_speed
        elif self.side == 'right':
            self.rect.x += self.x_speed
class Enemy_y(GameSprite):
    side = "left"
    def __init__(self, spr_image, spr_x, spr_y, spr_size_x, spr_size_y, y_up_granica, y_down_granica, x_speed, y_speed):
        GameSprite.__init__(self, spr_image, spr_x, spr_y, spr_size_x, spr_size_y)
        self.y_up_granica = y_up_granica
        self.y_down_granica = y_down_granica
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        if self.rect.y <= self.y_up_granica:
            self.side = 'down'
        if self.rect.y >= self.y_down_granica:
            self.side = 'up'

        if self.side == 'up':
            self.rect.y -= self.y_speed
        elif self.side == 'down':
            self.rect.y += self.y_speed
font.init()
font1 = font.SysFont('arial', 25)

coins_amount_1 = 0


class Coin(GameSprite):
    def __init__(self, spr_image, spr_x, spr_y, spr_size_x, spr_size_y):
        GameSprite.__init__(self, spr_image, spr_x, spr_y, spr_size_x, spr_size_y)

player = Player("player.png", 10, 10, 30, 30, 0, 0)
enemy = Enemy_x("enemy.png", 400, 300, 50, 50, 350, 450, 1, 0,)
enemy_2 = Enemy_x("enemy.png", 400, 150, 50, 50, 350, 450, 1, 0,)
enemies = sprite.Group()
enemies.add(enemy)
enemies.add(enemy_2)
wall1 = GameSprite("experemental_wall.png", 60, -40, 50, 450)
wall2 = GameSprite("experemental_wall.png", 180, 60, 50, 450)
wall3 = GameSprite("experemental_wall.png", 300, -25, 50, 450)
walls = sprite.Group()

walls.add(wall1)
walls.add(wall2)
walls.add(wall3)
coin1 = Coin('coin.png', 135, 265, 20, 20)
coin2 = Coin('coin.png', 195, 35, 20, 20)
coin3 = Coin('coin.png', 265, 360, 20, 20)
coin4 = Coin('coin.png', 475, 317, 20, 20)
coin5 = Coin('coin.png', 375, 167, 20, 20)
coins = sprite.Group()
coins.add(coin1)
coins.add(coin2)
coins.add(coin3)
coins.add(coin4)
coins.add(coin5)


lvl1 = True
lvl2 = False
while game:
    if lvl1:
        clock.tick(80)
        display.update()
        window.fill(background)
        walls.draw(window)
        coins.draw(window)
        enemies.draw(window)
        player.reset()
        enemies.update()
        player.update()
        if sprite.spritecollide(player, enemies, False):
            img = transform.scale(image.load("lose.jpg"), (500, 500))
            window.blit(img, (0, 0))
            display.update()
            game = False
        if sprite.spritecollide(player, coins, True):
            coins_amount_1 += 1
        coin = font1.render(f'Монеток : {coins_amount_1}', True, (0, 0, 0))
        window.blit(coin, (10, 10))
        for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == KEYDOWN:
                if e.key == K_w:
                    player.y_speed = -3
                if e.key == K_s:
                    player.y_speed = +3
                if e.key == K_a:
                    player.x_speed = -3
                if e.key == K_d:
                    player.x_speed = +3
            if e.type == KEYUP:
                if e.key == K_w:
                    player.y_speed = 0
                if e.key == K_s:
                    player.y_speed = 0
                if e.key == K_a:
                    player.x_speed = 0
                if e.key == K_d:
                    player.x_speed = 0
        coins.draw(window)

    if coins_amount_1 >= 5:
        next_level = GameSprite("next_level.png", 375, 50, 100, 50)
        next_level.reset()
        if lvl2:
            if sprite.collide_rect(player, next_level):
                pass

        if lvl1:
            if sprite.collide_rect(player, next_level):
                lvl1 = False
                lvl2 = True
                window.fill(background)
                coins_amount_1 = 0
                player = Player("player.png", 10, 10, 30, 30, 0, 0)
                enemy = Enemy_x("enemy.png", 400, 300, 50, 50, 350, 450, 2, 0)
                enemy_2 = Enemy_x("enemy.png", 400, 150, 50, 50, 350, 450, 2, 0)
                enemy_3 = Enemy_x("enemy.png", 130, 60, 30, 30, 110, 160, 1, 0)
                enemy_4 = Enemy_x("enemy.png", 130, 300, 30, 30, 110, 160, 1, 0)
                enemy_5 = Enemy_x("enemy.png", 15, 150, 30, 30, -35, 35, 1, 0)
                last_sprite = GameSprite("cup.png", 400, 40, 50, 50)
                coin1 = Coin('coin.png', 115, 123, 20, 20)
                coin2 = Coin('coin.png', 175, 123, 20, 20)
                coin3 = Coin('coin.png', 115, 213, 20, 20)
                coin4 = Coin('coin.png', 175, 213, 20, 20)
                coin5 = Coin('coin.png', 265, 300, 20, 20)
                coin6 = Coin('coin.png', 355, 320, 20, 20)
                coin7 = Coin('coin.png', 465, 170, 20, 20)
                coin8 = Coin('coin.png', 3, 475, 20, 20)
                coin9 = Coin('coin.png', 35, 475, 20, 20)
                wall1 = GameSprite("experemental_wall.png", 60, 60, 50, 450)
                wall2 = GameSprite("experemental_wall.png", 100, 150, 100, 60)
                wall3 = GameSprite("experemental_wall.png", 300, -45, 50, 450)
                wall4 = GameSprite("experemental_wall.png", 200, 60, 50, 375)
                wall5 = GameSprite("experemental_wall.png", 350, 345, 90, 60)
                coins = sprite.Group()
                coins.add(coin1)
                coins.add(coin2)
                coins.add(coin3)
                coins.add(coin4)
                coins.add(coin5)
                coins.add(coin6)
                coins.add(coin7)
                coins.add(coin8)
                coins.add(coin9)
                coins.draw(window)
                enemies = sprite.Group()
                walls = sprite.Group()
                enemies.add(enemy)
                enemies.add(enemy_2)
                enemies.add(enemy_3)
                enemies.add(enemy_4)
                enemies.add(enemy_5)
                walls.add(wall1)
                walls.add(wall2)
                walls.add(wall3)
                walls.add(wall4)
                walls.add(wall5)

    if lvl2:
        window.fill(background)
        walls.draw(window)
        player.reset()
        player.update()
        enemies.draw(window)
        enemies.update()
        for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == KEYDOWN:
                if e.key == K_w:
                    player.y_speed = -3
                if e.key == K_s:
                    player.y_speed = +3
                if e.key == K_a:
                    player.x_speed = -3
                if e.key == K_d:
                    player.x_speed = +3
            if e.type == KEYUP:
                if e.key == K_w:
                    player.y_speed = 0
                if e.key == K_s:
                    player.y_speed = 0
                if e.key == K_a:
                    player.x_speed = 0
                if e.key == K_d:
                    player.x_speed = 0
        coin = font1.render(f'Монеток : {coins_amount_1}', True, (0, 0, 0))
        window.blit(coin, (10, 10))
        coins.draw(window)

        if sprite.spritecollide(player, enemies, False):
            img = transform.scale(image.load("lose.jpg"), (500, 500))
            window.blit(img, (0, 0))
            display.update()
            game = False
        if sprite.spritecollide(player, coins, True):
            coins_amount_1 += 1

        if coins_amount_1 >= 9:
            last_sprite.reset()
            if sprite.collide_rect(player, last_sprite):
                img = transform.scale(image.load("win.jpg"), (500, 500))
                window.blit(img, (0, 0))
                game = False
                display.update()
        clock.tick(80)
        display.update()

time.wait(2000)