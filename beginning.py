import pygame

# --- Config ---
WIDTH, HEIGHT = 600, 600
ROOM_MARGIN = 50          # thickness of the outer wall margin
PLAYER_RADIUS = 15
PLAYER_SPEED = 220        # pixels / second
BG_COLOR = (20, 20, 20)
WALL_COLOR = (200, 200, 200)
PLAYER_COLOR = (100, 200, 255)
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Very Basic Dungeon Room")
    clock = pygame.time.Clock()

    # Room boundaries (inner playable area)
    left   = ROOM_MARGIN
    right  = WIDTH - ROOM_MARGIN
    top    = ROOM_MARGIN
    bottom = HEIGHT - ROOM_MARGIN

    # Start player in the center
    x, y = WIDTH // 2, HEIGHT // 2

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # seconds since last frame

        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Input ---
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += 1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy += 1

        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.70710678
            dy *= 0.70710678

        # --- Update ---
        x += dx * PLAYER_SPEED * dt
        y += dy * PLAYER_SPEED * dt

        # Keep the player inside the room (circle vs. walls)
        x = max(left   + PLAYER_RADIUS, min(x, right  - PLAYER_RADIUS))
        y = max(top    + PLAYER_RADIUS, min(y, bottom - PLAYER_RADIUS))

        # --- Draw ---
        screen.fill(BG_COLOR)

        # Draw walls (four lines forming a square room)
        pygame.draw.rect(
            screen,
            WALL_COLOR,
            pygame.Rect(left, top, right - left, bottom - top),
            width=3
        )

        # Draw player
        pygame.draw.circle(screen, PLAYER_COLOR, (int(x), int(y)), PLAYER_RADIUS)

        # Optionally show FPS in the window title
        pygame.display.set_caption(f"Very Basic Dungeon Room  |  FPS: {clock.get_fps():.0f}")

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
