from constants import *
import random


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, direction=1):
        """
        :param x_pos:
        :param y_pos:
        :param direction: 1=UP, -1=DOWN
        """
        super().__init__()
        file = "assets/pew_" + str(random.choice(range(1, 3))) + ".png"
        img = pygame.image.load(file).convert()

        self.surf = pygame.transform.scale(img, (BULLET_WIDTH, BULLET_HEIGHT))
        self.rect = self.surf.get_rect(center=(x_pos, y_pos))

        self.pos = vec((x_pos, y_pos))
        self.hits_taken = 0

        self.pos = vec((x_pos, y_pos))
        self.vel = BULLET_VELOCITY
        self.direction = direction

    def move(self, dt):
        self.pos.y -= self.vel * dt * self.direction

        if self.pos.y > SCREEN_HEIGHT or self.pos.y < 0:
            self.kill()

        self.rect.center = self.pos