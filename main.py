import pygame

pygame.init()

width, height = 800, 600

config = {
    "fps": 60,
    "size": (width, height),
    "caption": "caption",
    "icon": "images/d72fb4f666a872b84759bb9e636aedb1.png"
}

screen = pygame.display.set_mode(config["size"])
pygame.display.set_caption(config["caption"])
image = pygame.image.load(config['icon'])
pygame.display.set_icon(image)

# Set up ball properties
ball_radius = 20
ball_x = width // 2
ball_y = height // 2
ball_speed = 5

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(config["fps"])
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_x += ball_speed

    # Check if the ball is out of bounds and change direction
    if ball_x + ball_radius > width or ball_x - ball_radius < 0:
        ball_speed = -ball_speed

    # Fill the background
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, (0, 0, 255), (int(ball_x), int(ball_y)), ball_radius)

    pygame.display.flip()

    # Set the frames per second
    clock.tick(60)


pygame.quit()