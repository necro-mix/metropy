import sys
import pygame

pygame.init()

width, height = 800, 600

config = {
    "ticks": 60,
    "size": (width, height),
    "caption": "Metropy",
    "icon": "images/d72fb4f666a872b84759bb9e636aedb1.png"
}

screen = pygame.display.set_mode(config["size"])
pygame.display.set_caption(config["caption"])
image = pygame.image.load(config['icon'])
pygame.display.set_icon(image)

ball2_radius = 20
ball2_x = width/2
ball2_y = height/2
ball2_speed = 5
# Set up ball properties
ball1_radius = 20
ball1_x = width // 2
ball1_y = height // 2
ball1_speed = 5

clock = pygame.time.Clock()
running = True

while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        if ball2_x - ball2_radius < 0:
            ball2_x = 0 + ball2_radius
        ball2_x -= ball2_speed
    if key[pygame.K_d]:
        if ball2_x + ball2_radius > width:
            ball2_x = width - ball2_radius
        ball2_x += ball2_speed
    if key[pygame.K_w]:
        if ball2_y - ball2_radius < 0:
            ball2_y = 0 + ball2_radius
        ball2_y -= ball2_speed
    if key[pygame.K_s]:
        if ball2_y + ball2_radius > height:
            ball2_y = height - ball2_radius
        ball2_y += ball2_speed
    # Move the ball
    ball1_x += ball1_speed

    # Check if the ball is out of bounds and change direction
    if ball1_x + ball1_radius > width or ball1_x - ball1_radius < 0:
        ball1_speed = -ball1_speed

    # Fill the background
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, (0, 200, 50), (int(ball2_x), int(ball2_y)), ball1_radius)
    pygame.draw.circle(screen, (0, 0, 255), (int(ball1_x), int(ball1_y)), ball1_radius)

    if (ball1_x, ball1_y) == (ball2_x, ball2_y):
        sys.exit()

    pygame.display.flip()
    clock.tick(config["ticks"])

pygame.quit()