from barrier import *


class BarrierManager:
    def __init__(self):
        self.sprites = pygame.sprite.Group()

        width_in_blocks = round(BARRIER_WIDTH / BLOCK_SIZE)
        height_in_blocks = round(BARRIER_HEIGHT / BLOCK_SIZE)
        offset_x = round(width_in_blocks * BLOCK_SIZE / 2)
        offset_y = round(height_in_blocks * BLOCK_SIZE / 2)

        space_between_barriers = round((SCREEN_WIDTH - 3 * BARRIER_WIDTH) / 4)
        barrier_dead_center = vec(round(space_between_barriers + BARRIER_WIDTH / 2), round(SCREEN_HEIGHT * (7 / 8)))

        for _ in range(3):  # make 3 barriers total
            barrier_x = barrier_dead_center.x
            barrier_y = barrier_dead_center.y

            for _ in range(height_in_blocks):   # each barrier made of many blocks, each destructable
                for _ in range(width_in_blocks):
                    _x = barrier_x - offset_x
                    _y = barrier_y - offset_y
                    self.sprites.add(Barrier(x_pos=_x, y_pos=_y))
                    barrier_x += BLOCK_SIZE
                barrier_x = barrier_dead_center.x
                barrier_y += BLOCK_SIZE

            barrier_dead_center.x += space_between_barriers + BARRIER_WIDTH
