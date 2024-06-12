import pygame

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 720

# player
PLAYER_VELOCITY = 100
PLAYER_SPRITE_HEIGHT = 30
PLAYER_SPRITE_WIDTH = 50

# enemy
ENEMY_JUMP_DISTANCE = 30
ENEMY_SPRITE_WIDTH = 40
ENEMY_SPRITE_HEIGHT = 24

# mothership
MSHIP_JUMP_DIST = 320
MSHIP_VJUMP_DIST = 40

# general use vector creator
vec = pygame.math.Vector2

# bricks
BARRIER_WIDTH = 40
BARRIER_HEIGHT = 30
BLOCK_SIZE = 10  # size of a single barrier 'pixel'

# bullets
BULLET_VELOCITY = 400
BULLET_HEIGHT = 5
BULLET_WIDTH = 5


def red_tint(surface):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    for x in range(w):
        for y in range(h):
            col = surface.get_at((x, y))    # colors: r, g, b, a
            if col[0] < 220 and col[0] != 0:  # non-black pixels get redder: increase red band
                col[0] += 20
            if col[1] > 20:  # decrease green band
                col[1] -= 20
            if col[2] > 20:  # decrease blue band
                col[2] -= 20
            surface.set_at((x, y), col)
