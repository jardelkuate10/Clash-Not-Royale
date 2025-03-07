import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


def draw_glow_rect(surface, color, rect, glow_radius, num_glow_layers):
    """Draws a glowing rectangle."""
    for i in range(num_glow_layers):
        alpha = int(255 * (num_glow_layers - i) / num_glow_layers)
        glow_color = color + (alpha,)

        # Calculate the size of the glow layer
        glow_size = (rect.width + 2 * glow_radius * (i + 1),
                     rect.height + 2 * glow_radius * (i + 1))

        # Create a surface for the glow layer
        glow_surface = pygame.Surface(glow_size, pygame.SRCALPHA)

        # Draw the glow layer
        pygame.draw.rect(glow_surface, glow_color, (0, 0, *glow_size))

        # Calculate the position to blit the glow layer, centering it on the rect
        glow_position = (rect.centerx - glow_size[0] // 2,
                         rect.centery - glow_size[1] // 2)

        surface.blit(glow_surface, glow_position)


running = True
rect_color = (255, 69, 0)  # Orange color
rect = pygame.Rect(100, 100, 200, 100)
glow_radius = 10
num_glow_layers = 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background

    draw_glow_rect(screen, rect_color, rect, glow_radius, num_glow_layers)
    pygame.draw.rect(screen, rect_color, rect)  # Draw the main rectangle

    pygame.display.flip()
    clock.tick(60)

pygame.quit()