from pygame import *
FPS = 60

font.init()
font = font.Font(None, 40)

clock = time.Clock()
window = display.set_mode((600,400))
score1 = 0
score2 = 0

#Классы
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.width = player_width
        self.height = player_height
        self.image = transform.scale(image.load(player_image),(player_width,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
        self.speed_x = self.speed
        self.speed_y = self.speed 
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 250:
            self.rect.y += self.speed
    def update2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_e] and self.rect.y > 1:
            self.rect.y -= self.speed
        if key_pressed[K_d] and self.rect.y < 250:
            self.rect.y += self.speed
class Ball(GameSprite):

    def ball_update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.y <= 0 or self.rect.y >= 360:
            self.speed_y *= -1
        
        if sprite.collide_rect(player2, ball):
            self.speed_x *= -1
        
        if sprite.collide_rect(player1, ball):

            self.speed_x *= -1

player1 = Player('raket1.png',20, 120,6,50,150)
player2 = Player('raket1.png',530, 120,6,50,150)
ball = Ball('ball1.png', 280, 180, 4, 40, 40)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        window.fill((0, 167, 179))

        player1.reset()
        player1.update1()

        player2.reset()
        player2.update2()

        ball.reset()
        ball.ball_update()

        if ball.rect.x < 0:
            score2 += 1
            ball.rect.x = 300
            ball.rect.y = 200

        if ball.rect.x > 600:
            score1 += 1
            ball.rect.x = 300
            ball.rect.y = 200
        
        text_score1 = font.render('Игрок 1 - ' + str(score1),True,(0,0,0))
        window.blit(text_score1,(70,10))
        text_score2 = font.render('Игрок 2 - ' + str(score2),True, (0,0,0))
        window.blit(text_score2,(390,10))

    display.update()
    clock.tick(FPS)
