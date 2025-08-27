import asyncio
import pygame
import config
from adventure_functions import (
    draw_room, is_blocked, draw_obstacle, draw_player, load_player_image
)

async def main():
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("3x3 Adventure Grid")
    clock = pygame.time.Clock()

    load_player_image()
    player_x = config.WIDTH // 2
    player_y = config.HEIGHT // 2

    running = True
    while running:
        dt = clock.tick(config.FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: dx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]: dy = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy = 1
        if dx != 0 and dy != 0:
            dx *= 0.7071; dy *= 0.7071

        new_x = player_x + dx * config.PLAYER_SPEED * dt
        new_y = player_y + dy * config.PLAYER_SPEED * dt
        if not is_blocked(new_x, new_y):
            player_x, player_y = new_x, new_y

        screen.fill(config.BG_COLOR)
        for row in range(config.GRID_ROWS):
            for col in range(config.GRID_COLS):
                draw_room(screen, row, col)
        draw_obstacle(screen)
        draw_player(screen, player_x, player_y)
        pygame.display.flip()

        # Important for browsers (yields control to JS event loop)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
