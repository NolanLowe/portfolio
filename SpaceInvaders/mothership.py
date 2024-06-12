from constants import *
import random

class Mothership(pygame.sprite.Sprite):
    def __init__(self, starting_x, starting_y):
        super().__init__()
        file = "assets/mothership.png"
        img = pygame.image.load(file).convert()

        self.surf = pygame.transform.scale(img, (ENEMY_SPRITE_WIDTH, ENEMY_SPRITE_HEIGHT))
        self.rect = self.surf.get_rect(center=(starting_x, starting_y))
        self.vertical_jump_distance = MSHIP_VJUMP_DIST
        self.horizontal_jump_distance = MSHIP_JUMP_DIST

        self.pos = vec((starting_x, starting_y))

    def move(self, dt, direction):
        """

        :param direction: 1 = RIGHT, -1 = LEFT
        :return:
        """
        self.pos.x += MSHIP_JUMP_DIST * direction * dt  # normal movement
        self.rect.center = self.pos


    def advance(self, distance):
        """
        move ship forwards
        :param distance:
        :return:
        """
        self.pos.y += self.vertical_jump_distance
        self.rect.center = self.pos
