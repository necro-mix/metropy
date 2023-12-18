import pygame



pygame.init()

config = {
    "fps": 60,
    "size": (500, 500),
    "caption": "caption",
    "icon": "images/d72fb4f666a872b84759bb9e636aedb1.png"
}

screen = pygame.display.set_mode(config["size"])
pygame.display.set_caption(config["caption"])
image = pygame.image.load(config['icon'])
pygame.display.set_icon(image)
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(config["fps"])
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()


pygame.quit()