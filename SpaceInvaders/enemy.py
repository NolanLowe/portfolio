from constants import *
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, starting_x, starting_y):
        super().__init__()
        file = "assets/ship_" + str(random.choice(range(1, 6))) + ".png"
        img = pygame.image.load(file).convert()

        self.surf = pygame.transform.scale(img, (ENEMY_SPRITE_WIDTH, ENEMY_SPRITE_HEIGHT))
        self.rect = self.surf.get_rect(center=(starting_x, starting_y))
        self.vertical_jump_distance = ENEMY_SPRITE_HEIGHT * 2
        self.horizontal_jump_distance = ENEMY_JUMP_DISTANCE

        self.pos = vec((starting_x, starting_y))

    def move(self, dt, direction):
        """

        :param direction: 1 = RIGHT, -1 = LEFT
        :return:
        """
        self.pos.x += ENEMY_JUMP_DISTANCE * direction * dt  # normal movement
        self.rect.center = self.pos


    def advance(self, distance):
        """
        move ship forwards
        :param distance:
        :return:
        """
        self.pos.y += distance
        self.rect.center = self.pos
