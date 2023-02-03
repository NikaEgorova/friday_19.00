from pygame import *

window_width = 700
window_height = 500
display.set_caption('labirint lol')
background = (255, 255, 255)
window = display.set_mode((window_width, window_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        if player.rect.x <= window_width - 80 and player.x_speed > 0 or player.rect.x >= 0 and player.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, walls, False)
        if self.x_speed > 0:
            for platforms in platforms_touched:
                self.rect.right = min(self.rect.right, platforms.rect.left)
        elif self.x_speed < 0:
            for platforms in platforms_touched:
                self.rect.left = max(self.rect.left, platforms.rect.right)

        if player.rect.y <= window_height - 80 and player.y_speed > 0 or player.rect.y >= 0 and player.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, walls, False)
        if self.y_speed > 0:
            for platforms in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, platforms.rect.top)
        elif self.y_speed < 0:
            for platforms in platforms_touched:
                self.rect.top = max(self.rect.top, platforms.rect.bottom)
    def fire(self):
        bullet = Bullet('bulllet.png', self.rect.right - 25, self.rect.centery - 16, 15, 20, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    side = 'left'
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self,player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        if self.rect.x <= 420:
            self.side = 'right'
        if self.rect.x >= window_width - 80:
            self.side = 'left'

        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор GameSprite
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    # рух ворога
    def update(self):
        self.rect.x += self.speed
        # зникає, якщо виходить за межі екрану
        if self.rect.x > window_width + 10:
            self.kill()

class Enemy1(GameSprite):
    side = 'left'

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self):
        if self.rect.x <= - 30:
            self.side = 'right'
        if self.rect.x >= window_width - 380:
            self.side = 'left'

        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed




wall1 = GameSprite('wall.png', 400, 100, 50, 400)
wall2 = GameSprite('wall2.png', 200, 250, 200, 25)
wall3 = GameSprite('wall2.png', 550, 300, 150, 25)
wall4 = GameSprite('wall.png', 200, 250, 25, 150)
wall5 = GameSprite('wall2.png', 550, 100, 150, 25)
wall6 = GameSprite('wall.png', 200, 0, 20, 100)

walls = sprite.Group()
bullets = sprite.Group()
walls.add(wall1)
walls.add(wall2)
walls.add(wall3)
walls.add((wall4))
walls.add(wall5)
walls.add(wall6)

player = Player('hero.png', 5, window_height -80, 80, 80, 0, 0)
monster = Enemy('enemy.png', 450, 200, 80, 80, 3)
monstr = Enemy1('enemy.png', 50, 170, 80, 80, 3)
monstryk = GameSprite('enemy.png', 250, 280, 80, 80)
finish = GameSprite('end.png', 550, window_height -80, 80, 80)

monsters = sprite.Group()
monsters.add(monster)
monsters.add(monstr)
monsters.add(monstryk)

win = False
run = True
while run:
    time.delay(17)

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                player.y_speed = -5
            elif e.key == K_s:
                player.y_speed = 5
            elif e.key == K_a:
                player.x_speed = -5
            elif e.key == K_d:
                player.x_speed = 5
            elif e.key == K_SPACE:
                player.fire()
        elif e.type == KEYUP:
            if e.key == K_w:
                player.y_speed = 0
            elif e.key == K_s:
                player.y_speed = 0
            elif e.key == K_a:
                player.x_speed = 0
            elif e.key == K_d:
                player.x_speed = 0
    if not win:
        window.fill(background)
        bullets.draw(window)
        monsters.draw(window)
        bullets.update()
        player.reset()
        player.update()
        finish.reset()
        walls.draw(window)

        sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monsters.draw(window)
        sprite.groupcollide(bullets, walls, True, False)


        if sprite.spritecollide(player, monsters, False):
            win = True
            img = image.load('lose.jpg')
            window.blit(transform.scale(img, (window_width, window_height)), (0,0))

        if sprite.collide_rect(player, finish):
            win = True
            img = image.load('win.jpg')
            window.blit(transform.scale(img, (window_width, window_height)), (0,0))

        display.update()