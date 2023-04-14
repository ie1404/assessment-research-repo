import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Create a game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw game objects
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))

    # Update the game display
    pygame.display.update()

# Quit Pygame
pygame.quit()