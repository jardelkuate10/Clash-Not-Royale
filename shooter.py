import pygame
from projectile import Projectile
from base_character import BaseCharacter# Make sure you import the new Projectile class


class Shooter(BaseCharacter):
    def __init__(self, screen, x, y, color, my_side, enemy_side):
        super().__init__(screen, x, y, color, my_side, enemy_side)

        self.projectiles = []
        #fire rate
        self.fire_rate = 250  #tiem between last shoot
        self.last_shot_time = 0  # Timestamp of the last fired shot

    def draw(self):
        super().draw()
        for projectile in self.projectiles:
            projectile.draw()

    def update(self):
        super().update()
        # Update projectiles
        for projectile in self.projectiles[:]:
            projectile.move()
            if projectile.check_collision(self.enemy_side.towers):
                self.projectiles.remove(projectile)  # Remove projectile after they collide

    def fire_projectile(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        if keys[pygame.K_SPACE] and current_time - self.last_shot_time >= self.fire_rate:
            self.last_shot_time = current_time  # Reset shot timer

            direction = 'up'
            projectile = Projectile(self.screen, self.rect.centerx - 4, self.rect.centery - 25, 'red', 10, 100, direction)
            self.projectiles.append(projectile)
