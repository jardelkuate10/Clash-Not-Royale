import pygame

class Projectile:
    def __init__(self, screen, x, y, color, speed, damage, direction):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.size = 10
        self.speed = speed
        self.damage = damage
        self.direction = direction
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move(self):
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed

    def check_collision(self, towers):
        for tower in towers:
            if self.rect.colliderect(tower.rect):
                tower.take_damage(self.damage)  # Deal dmg
                return True  # if collision happens return true
        return False
