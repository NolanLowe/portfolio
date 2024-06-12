from constants import *


class Barrier(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.surf = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(x_pos, y_pos))



