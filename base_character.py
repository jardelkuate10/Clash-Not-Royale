import pygame


class BaseCharacter:
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
        self.rect = pygame.Rect(x, y, self.size, self.size  )

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move(self):
        # Check keyboard state
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        self.update()

    def update(self):
        for tower in self.enemy_side.towers:
            if self.rect.colliderect(tower.rect):
                tower.take_damage(self.dmg)
