import pygame
import math

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Map dimensions
MAP_WIDTH = 24
MAP_HEIGHT = 24

# Map layout
world_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

LIGHTRED = (255, 100, 100)
DARKRED = (139, 0, 0)

# Player starting position and direction
pos_x = 22.0
pos_y = 12.0
dir_x = -1.0
dir_y = 0.0
plane_x = 0.0
plane_y = 1.0

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def draw():

    # Draw ceiling
    screen.fill((100, 100, 100), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT // 2))

    # Draw floor
    screen.fill((50, 50, 50), (0, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT // 2))

    for x in range(SCREEN_WIDTH):
        # Calculate ray position and direction
        camera_x = 2 * x / float(SCREEN_WIDTH) - 1
        ray_dir_x = dir_x + plane_x * camera_x
        ray_dir_y = dir_y + plane_y * camera_x

        # Which box of the map we're in
        map_x = int(pos_x)
        map_y = int(pos_y)

        # Length of ray from current position to next x or y-side
        side_dist_x = 0
        side_dist_y = 0

        # Length of ray from one x or y-side to next x or y-side
        delta_dist_x = abs(1 / ray_dir_x) if ray_dir_x != 0 else float('inf')
        delta_dist_y = abs(1 / ray_dir_y) if ray_dir_y != 0 else float('inf')
        perp_wall_dist = 0

        # Direction to go in x and y
        step_x = 0
        step_y = 0

        hit = 0  # Was there a wall hit?
        side = 0  # Was a NS or a EW wall hit?

        # Calculate step and initial sideDist
        if ray_dir_x < 0:
            step_x = -1
            side_dist_x = (pos_x - map_x) * delta_dist_x
        else:
            step_x = 1
            side_dist_x = (map_x + 1.0 - pos_x) * delta_dist_x
        if ray_dir_y < 0:
            step_y = -1
            side_dist_y = (pos_y - map_y) * delta_dist_y
        else:
            step_y = 1
            side_dist_y = (map_y + 1.0 - pos_y) * delta_dist_y

        # Perform DDA
        while hit == 0:
            # Jump to next map square, OR in x-direction, OR in y-direction
            if side_dist_x < side_dist_y:
                side_dist_x += delta_dist_x
                map_x += step_x
                side = 0
            else:
                side_dist_y += delta_dist_y
                map_y += step_y
                side = 1
            # Check if ray has hit a wall
            if world_map[map_x][map_y] > 0:
                hit = 1

        # Calculate distance projected on camera direction (Euclidean distance will give fisheye effect!)
        if side == 0:
            perp_wall_dist = (map_x - pos_x + (1 - step_x) / 2) / ray_dir_x
        else:
            perp_wall_dist = (map_y - pos_y + (1 - step_y) / 2) / ray_dir_y

        # Calculate height of line to draw on screen
        line_height = int(SCREEN_HEIGHT / perp_wall_dist)

        # Calculate lowest and highest pixel to fill in current stripe
        draw_start = -line_height / 2 + SCREEN_HEIGHT / 2
        if draw_start < 0:
            draw_start = 0
        draw_end = line_height / 2 + SCREEN_HEIGHT / 2
        if draw_end >= SCREEN_HEIGHT:
            draw_end = SCREEN_HEIGHT - 1

        # Choose wall color
        color = LIGHTRED
        if side == 1: color = DARKRED

        # Darken the color based on distance
        color_intensity = max(0, 255 - int(perp_wall_dist * 10))
        color = (color[0] * color_intensity // 255, color[1] * color_intensity // 255, color[2] * color_intensity // 255)

        # Draw the pixels of the stripe as a vertical line
        pygame.draw.line(screen, color, (x, draw_start), (x, draw_end))

def main():
    global pos_x, pos_y, dir_x, dir_y, plane_x, plane_y
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dt = pygame
        move_speed = 0.05
        rot_speed = 0.03

        if keys[pygame.K_UP]:
            if world_map[int(pos_x + dir_x * move_speed)][int(pos_y)] == 0:
                pos_x += dir_x * move_speed
            if world_map[int(pos_x)][int(pos_y + dir_y * move_speed)] == 0:
                pos_y += dir_y * move_speed
        if keys[pygame.K_DOWN]:
            if world_map[int(pos_x - dir_x * move_speed)][int(pos_y)] == 0:
                pos_x -= dir_x * move_speed
            if world_map[int(pos_x)][int(pos_y - dir_y * move_speed)] == 0:
                pos_y -= dir_y * move_speed
        if keys[pygame.K_RIGHT]:
            old_dir_x = dir_x
            dir_x = dir_x * math.cos(-rot_speed) - dir_y * math.sin(-rot_speed)
            dir_y = old_dir_x * math.sin(-rot_speed) + dir_y * math.cos(-rot_speed)
            old_plane_x = plane_x
            plane_x = plane_x * math.cos(-rot_speed) - plane_y * math.sin(-rot_speed)
            plane_y = old_plane_x * math.sin(-rot_speed) + plane_y * math.cos(-rot_speed)
        if keys[pygame.K_LEFT]:
            old_dir_x = dir_x
            dir_x = dir_x * math.cos(rot_speed) - dir_y * math.sin(rot_speed)
            dir_y = old_dir_x * math.sin(rot_speed) + dir_y * math.cos(rot_speed)
            old_plane_x = plane_x
            plane_x = plane_x * math.cos(rot_speed) - plane_y * math.sin(rot_speed)
            plane_y = old_plane_x * math.sin(rot_speed) + plane_y * math.cos(rot_speed)

        screen.fill((0, 0, 0))
        draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()