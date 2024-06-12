from constants import *
from constants import red_tint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pygame.image.load('assets/player.png').convert()
        self.surf = pygame.transform.scale(img, (PLAYER_SPRITE_WIDTH, PLAYER_SPRITE_HEIGHT))
        self.rect = self.surf.get_rect(center=(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] - PLAYER_SPRITE_HEIGHT / 2))

        self.pos = vec((SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] - PLAYER_SPRITE_HEIGHT / 2))
        self.vel = vec(PLAYER_VELOCITY, PLAYER_VELOCITY)

        self.health = 2

    def move(self, direction, dt):
        self.pos.x += self.vel.x * dt * direction

        if self.pos.x > SCREEN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH

        self.rect.center = self.pos


    def hit(self):
        """
        change player sprite to indicate health
        white -> orange -> red -> dead
        :return: true if dead, false otherwise
        """
        self.health -= 1
        if self.health == 1:
            red_tint(self.surf)
        elif self.health == 0:
            red_tint(self.surf)
        else:
            return True

