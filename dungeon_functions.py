# dungeon_functions.py
import pygame
import config

def draw_room(screen, row, col):
    left = col * config.ROOM_WIDTH
    right = left + config.ROOM_WIDTH
    top = row * config.ROOM_HEIGHT
    bottom = top + config.ROOM_HEIGHT
    mid_x = (left + right) // 2
    mid_y = (top + bottom) // 2

    # Top wall
    if row == 0:
        pygame.draw.line(screen, config.WALL_COLOR, (left, top), (right, top), config.WALL_THICK)
    else:
        pygame.draw.line(screen, config.WALL_COLOR, (left, top), (mid_x - config.DOOR_SIZE // 2, top), config.WALL_THICK)
        pygame.draw.line(screen, config.WALL_COLOR, (mid_x + config.DOOR_SIZE // 2, top), (right, top), config.WALL_THICK)

    # Bottom wall
    if row == config.GRID_ROWS - 1:
        pygame.draw.line(screen, config.WALL_COLOR, (left, bottom), (right, bottom), config.WALL_THICK)
    else:
        pygame.draw.line(screen, config.WALL_COLOR, (left, bottom), (mid_x - config.DOOR_SIZE // 2, bottom), config.WALL_THICK)
        pygame.draw.line(screen, config.WALL_COLOR, (mid_x + config.DOOR_SIZE // 2, bottom), (right, bottom), config.WALL_THICK)

    # Left wall
    if col == 0:
        pygame.draw.line(screen, config.WALL_COLOR, (left, top), (left, bottom), config.WALL_THICK)
    else:
        pygame.draw.line(screen, config.WALL_COLOR, (left, top), (left, mid_y - config.DOOR_SIZE // 2), config.WALL_THICK)
        pygame.draw.line(screen, config.WALL_COLOR, (left, mid_y + config.DOOR_SIZE // 2), (left, bottom), config.WALL_THICK)

    # Right wall
    if col == config.GRID_COLS - 1:
        pygame.draw.line(screen, config.WALL_COLOR, (right, top), (right, bottom), config.WALL_THICK)
    else:
        pygame.draw.line(screen, config.WALL_COLOR, (right, top), (right, mid_y - config.DOOR_SIZE // 2), config.WALL_THICK)
        pygame.draw.line(screen, config.WALL_COLOR, (right, mid_y + config.DOOR_SIZE // 2), (right, bottom), config.WALL_THICK)


def is_blocked(x, y):
    """Return True if the player is hitting a wall (excluding doors)"""
    for row in range(config.GRID_ROWS):
        for col in range(config.GRID_COLS):
            left = col * config.ROOM_WIDTH
            right = left + config.ROOM_WIDTH
            top = row * config.ROOM_HEIGHT
            bottom = top + config.ROOM_HEIGHT
            mid_x = (left + right) // 2
            mid_y = (top + bottom) // 2

            if left <= x <= right and top <= y <= bottom:
                if x - config.PLAYER_RADIUS < left:
                    if col == 0 or not (mid_y - config.DOOR_SIZE//2 <= y <= mid_y + config.DOOR_SIZE//2):
                        return True
                if x + config.PLAYER_RADIUS > right:
                    if col == config.GRID_COLS - 1 or not (mid_y - config.DOOR_SIZE//2 <= y <= mid_y + config.DOOR_SIZE//2):
                        return True
                if y - config.PLAYER_RADIUS < top:
                    if row == 0 or not (mid_x - config.DOOR_SIZE//2 <= x <= mid_x + config.DOOR_SIZE//2):
                        return True
                if y + config.PLAYER_RADIUS > bottom:
                    if row == config.GRID_ROWS - 1 or not (mid_x - config.DOOR_SIZE//2 <= x <= mid_x + config.DOOR_SIZE//2):
                        return True
                return False

    return True
