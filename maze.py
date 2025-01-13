from pygame import *

window = display.set_mode((700,500))
display.set_caption('Лабиринт')
background = transform.scale(image.load("background.jpg"), (700, 500))
clock = time.Clock()
FPS = 60
mixer.init()
font.init()
font1 = font.Font(None, 70)
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.01)
mixer.music.play()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction = "left"
    def update(self):
        if self.rect.x <= 425:
            self.direction = "right"
        if self.rect.x >= 625:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color, wall_x, wall_y, wall_width, wall_hight):
        super().__init__()
        self.image = Surface((wall_width,wall_hight))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


           
        



    
player = Player("hero.png", 10, 425, 8)
enemy = Enemy("cyborg.png", 625, 300, 7)
money = GameSprite("treasure.png",625, 425, 0)
wall1 = Wall((14,35,15),100,10, 10, 240)
wall2 = Wall((14,35,15),100,350,10,135)
wall3 = Wall((14,35,15),100,10,420,10)
wall4 = Wall((14,35,15),100,485,470,10)
wall5 = Wall((14,35,15),200,10,10,350)
wall6 = Wall((14,35,15),320,100,10,395)
wall7 = Wall((14,35,15),420,250,10,240)
wall8 = Wall((14,35,15),520,10,10,250)
game = True
finish = False
while game:
    clock.tick(FPS)
    window.blit(background, (0,0))
    if finish == False:
        player.reset()
        enemy.reset()
        money.reset()
        player.update()
        enemy.update()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        if sprite.collide_rect(player,enemy):
            win = font1.render('YOU LOSE!', True,(255,215,0))
            finish = True
        if sprite.collide_rect(player,money):
            win = font1.render('YOU WIN!', True,(255, 215, 0))
            finish = True
        if sprite.collide_rect(player, wall1) or sprite.collide_rect(player,wall2) or sprite.collide_rect(player,wall3) or sprite.collide_rect(player,wall4) or sprite.collide_rect(player,wall5) or sprite.collide_rect(player,wall6) or sprite.collide_rect(player,wall7) or sprite.collide_rect(player,wall8):
            player.rect.x = 10
            player.rect.y = 425
    
    if finish == True:
        window.blit(win,(240,250))
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                finish = False
                player.rect.x = 10
                player.rect.y = 425


    display.update()