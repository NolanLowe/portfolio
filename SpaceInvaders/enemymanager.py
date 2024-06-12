from enemy import *
from mothership import Mothership


class EnemyManager:

    def __init__(self):
        self.sprites = pygame.sprite.Group()

        self.max_x = SCREEN_WIDTH - (ENEMY_SPRITE_WIDTH)
        self.min_x = ENEMY_SPRITE_WIDTH

        self.mothership_spawned = False

        space = 1.2
        spacing = vec(ENEMY_SPRITE_WIDTH * space, ENEMY_SPRITE_HEIGHT * space)

        enemies_per_row = round(SCREEN_WIDTH / spacing.x) - 4
        num_rows = round((SCREEN_HEIGHT / 4) / spacing.y) - 2

        self.direction = 1
        self.advancing = False
        self.need_to_check = True

        ship_loc = vec(spacing.x, spacing.y)
        for _ in range(num_rows):
            for _ in range(enemies_per_row):
                self.sprites.add(Enemy(ship_loc.x, ship_loc.y))
                ship_loc.x += spacing.x

            ship_loc.x = spacing.x
            ship_loc.y += spacing.y

    def spawn_mothership(self):
        loc = vec(ENEMY_SPRITE_WIDTH * 1.2, ENEMY_SPRITE_HEIGHT * 1.2)
        self.sprites.add(Mothership(loc.x, loc.y))
        self.mothership_spawned = True

    def strafe(self, dt):
        if not self.advancing:
            for e in self.sprites:
                e.move(dt=dt, direction=self.direction)
                if self.need_to_check:  # if even one enemy is headed OOB, no need to check the rest of them
                    if (e.pos.x > self.max_x and self.direction == 1) or (
                            e.pos.x < self.min_x and self.direction == -1):
                        self.advancing = True  # one of the ships is headed OOB -> everybody will move forwards on the next move cycle
                        self.need_to_check = False
        else:  # you're advancing. all enemy sprites move towards the player and reverse direction
            for e in self.sprites:
                e.advance(ENEMY_SPRITE_HEIGHT * 0.5)
            self.direction *= -1
            self.advancing = False
            self.need_to_check = True
