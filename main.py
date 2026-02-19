import pygame

print('Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 400))
print('Finish')

while True:
    # Check for all events
    for event in pygame.event.get():
        # If the user clicks the close button, quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        