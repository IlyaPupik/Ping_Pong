from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_hide):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_hide))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 545:
            self.rect.y += self.speed
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 545:
            self.rect.y += self.speed

window = display.set_mode((900, 700))
back = (0, 255, 30)
window.fill(back)

display.set_caption('Ping_Pong')

clock = time.Clock()

rocket_r = Player('racket.png', 820, 300, 5, 50, 150)
rocket_l = Player('racket.png', 30, 300, 5, 50, 150)
ball = GameSprite('tenis_ball.png', 400, 300, 5, 50, 50)

finish = False
game = True
speed_x = 3
speed_y = 3
font.init()
text = font.SysFont('Arial', 40)
lose1 = text.render('Игрок слева проиграл', True, (255, 0, 0))
lose2 = text.render('Игрок справа проиграл', True, (255, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        rocket_r.update_r()
        rocket_r.reset()
        rocket_l.update_L()
        rocket_l.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y >= 650 or ball.rect.y <= 0:
            speed_y *= -1
        if sprite.collide_rect(rocket_r, ball) or sprite.collide_rect(rocket_l, ball):
            speed_x *=  -1
        if ball.rect.x <= 0:
            finish = True
            window.blit(lose1, (300, 300))
        if ball.rect.x >= 850:
            finish = True
            window.blit(lose2, (300, 300))
        ball.reset()
    display.update()
    clock.tick(60)