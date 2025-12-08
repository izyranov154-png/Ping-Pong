from pygame import *
FPS = 60

clock = time.Clock()
window = display.set_mode((400,300))


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
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w]:
            self.rect.y -= self.speed
        if key_pressed[K_s]:
            self.rect.y += self.speed
    def update2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP]:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN]:
            self.rect.y += self.speed


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        window.fill((0, 167, 179))
        display.update()
clock.tick(FPS)