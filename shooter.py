import pygame
from projectile import Projectile  # Make sure you import the new Projectile class

class Shooter:
    def __init__(self, screen, x, y, color, my_side, enemy_side):
        self.size = 20
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.my_side = my_side
        self.enemy_side = enemy_side
        self.speed = 1
        self.dmg = 50
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.projectiles = []

        #fire rate
        self.fire_rate = 250  #tiem between last shoot
        self.last_shot_time = 0  # Timestamp of the last fired shot

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        for projectile in self.projectiles:
            projectile.draw()

    def move(self):
        # Check keyboard state
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect = self.rect.move(0, -self.speed)
        if keys[pygame.K_a]:
            self.rect = self.rect.move(-self.speed, 0)
        if keys[pygame.K_s]:
            self.rect = self.rect.move(0, self.speed)
        if keys[pygame.K_d]:
            self.rect = self.rect.move(self.speed, 0)

        self.update()

    def update(self):
        # Update projectiles
        for projectile in self.projectiles[:]:
            projectile.move()
            if projectile.check_collision(self.enemy_side.towers):
                self.projectiles.remove(projectile)  # Remove projectile after they collide

        for tower in self.enemy_side.towers:
            if self.rect.colliderect(tower.rect):
                tower.take_damage(self.dmg)

    def fire_projectile(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        if keys[pygame.K_SPACE] and current_time - self.last_shot_time >= self.fire_rate:
            self.last_shot_time = current_time  # Reset shot timer

            direction = 'up'
            projectile = Projectile(self.screen, self.rect.centerx - 4, self.rect.centery - 25, 'red', 10, 100, direction)
            self.projectiles.append(projectile)
