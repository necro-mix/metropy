import sys
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 500
GROUND_HEIGHT = 500

config = {
    "ticks": 60,
    "size": (WIDTH, HEIGHT),
    "caption": "Metropy",
    "icon": "img/d72fb4f666a872b84759bb9e636aedb1.png",
    "ground_height": GROUND_HEIGHT 
}

screen = pygame.display.set_mode(config["size"])
pygame.display.set_caption(config["caption"])
image = pygame.image.load(config['icon'])
pygame.display.set_icon(image)

# Load the background image
background_image = pygame.image.load("img/room.jpg").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Create the Mono sprite class
class Mono(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/mono.png").convert_alpha()
        # Adjust the size of the image if needed
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, config['ground_height'] - 20)
        self.velocity = 6
        self.jump_count = 10
        self.on_ground = True

    def update(self):
        # Apply gravity
        if not self.on_ground:
            if self.rect.y < config['ground_height']- 40:
                self.rect.y += self.velocity
            else:
                # Reset jump variables and position when on the ground
                self.jump_count = 10
                self.on_ground = True
                self.rect.y = config['ground_height'] - 45


# Create the sprite group
all_sprites = pygame.sprite.Group()
mono = Mono()
all_sprites.add(mono)

# Set up the clock
clock = pygame.time.Clock()

# Set up initial jump variables
jump = False

# Draw the background onto a separate surface
background_surface = pygame.Surface((WIDTH, HEIGHT))
background_surface.blit(background_image, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed() 

    if keys[pygame.K_a] and mono.rect.left > 0:
        mono.rect.x -= mono.velocity

    if keys[pygame.K_d] and mono.rect.right < WIDTH:
        mono.rect.x += mono.velocity

    # Jump
    if not jump and mono.on_ground:
        if keys[pygame.K_SPACE]:
            jump = True
            mono.on_ground = False
    else:
        if mono.jump_count >= -10:
            neg = 1
            if mono.jump_count < 0:
                neg = -1
            mono.rect.y -= (mono.jump_count ** 2) * 0.5 * neg
            mono.jump_count -= 1
        else:
            jump = False
            mono.jump_count = 10

    # Update the display with the background surface
    screen.blit(background_surface, (0, 0))

    # Draw the sprites
    all_sprites.draw(screen)
    
    # Update the display
    pygame.display.flip()

    # Update the sprite group
    all_sprites.update()

    # Cap the frame rate
    clock.tick(config['ticks'])
