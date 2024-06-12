import pygame

from player import Player
from enemymanager import EnemyManager
from barriermanager import BarrierManager
from constants import *
from bullet import Bullet
from timer import Timer
import random
from barrier import Barrier

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
dt = 0

all_sprites = pygame.sprite.Group()  # every sprite, regardless of side - used for movement
bullet_sprites = pygame.sprite.Group()  # the players bullets
shootable_sprites = pygame.sprite.Group()  # sprites the players bullets can damage
player_side_sprites = pygame.sprite.Group()  # sprites the enemy can damage

surviving_enemy_ratio: float = None

player = Player()
player_gun_timer = Timer()
enemy_movement_timer = Timer()
all_sprites.add(player)
shootable_sprites.add(player)
player_side_sprites.add(player)

# assemble the enemies, assign to groups
enemies = EnemyManager()
for e in enemies.sprites:
    all_sprites.add(e)
    shootable_sprites.add(e)

# assemble the barriers, assign to groups
barriers = BarrierManager()
for b in barriers.sprites:
    all_sprites.add(b)
    shootable_sprites.add(b)
    player_side_sprites.add(b)

enemy_bullets = pygame.sprite.Group()

while running:
    # make sure close -> [X] works
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # draw everything: player, enemies, bullets
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # move the enemies
    enemies.strafe(dt)

    # move the bullets (player and enemy)
    for bullet in bullet_sprites:
        bullet.move(dt)
    for bullet in enemy_bullets:
        bullet.move(dt)

    # collisions from Player bullets against barrier, or enemy ships
    for sprite in pygame.sprite.groupcollide(groupa=shootable_sprites, groupb=bullet_sprites, dokilla=1, dokillb=1):
        pass

    # make the enemies fire bullets
    for ship in enemies.sprites:
        if len(enemy_bullets) > 10:
            break
        if random.random() < 0.001:
            b = Bullet(ship.pos.x, ship.pos.y + ENEMY_SPRITE_HEIGHT * 1.2, direction=-1)
            all_sprites.add(b)
            enemy_bullets.add(b)

    # collisions from Enemy bullets against barrier, or player
    for sprite in pygame.sprite.groupcollide(groupa=player_side_sprites, groupb=enemy_bullets, dokilla=0, dokillb=1):
        if isinstance(sprite, Player):
            # player took a hit ->
            if player.hit():
                player.kill()
        if isinstance(sprite, Barrier):
            # barrier took a hit ->
            sprite.kill()

    if len(enemies.sprites) == 0 and (not enemies.mothership_spawned):
        # all conventional enemies dead -> bring in the mothership
        enemies.spawn_mothership()
        for ms in enemies.sprites:
            all_sprites.add(ms)
            shootable_sprites.add(ms)

    keys = pygame.key.get_pressed()

    # quit game
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit(0)

    # player shoots gun!
    if keys[pygame.K_SPACE]:
        if player_gun_timer.can_fire():
            b = Bullet(player.pos.x, player.pos.y - ENEMY_SPRITE_HEIGHT * 1.2)
            all_sprites.add(b)
            bullet_sprites.add(b)

    # player movement: a .. d  or <- ->
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move(direction=-1, dt=dt)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move(direction=1, dt=dt)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
