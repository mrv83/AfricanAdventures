import random
import numpy as np

# Типи місцевості
TILE_TYPES = [
    "rocks", "savanna", "jungles", "swamps", "coasts",
    "water", "high_tree", "old_camp", "camp", "broken_car"
]


# Головний генератор мап
def generate_map(width, height):
    # Init map
    game_map = np.full((height, width), "empty")

    # 1. Create river
    create_water_line(game_map)

    # 2. Fill by "rocks"
    game_map[0, :] = game_map[-1, :] = "rocks"
    game_map[:, 0] = game_map[:, -1] = "rocks"
    for i in range(1, 5):
        # Top
        for x, t in enumerate(game_map[i, :]):
            if random.randint(0, 4-i) and game_map[i-1, x] == "rocks":
                game_map[i, x] = "rocks"
        # Bottom
        for x, t in enumerate(game_map[height-i-1, :]):
            if random.randint(0, 4-i) and game_map[height-i, x] == "rocks":
                game_map[height-i-1, x] = "rocks"
        # Left
        for y, t in enumerate(game_map[:, i]):
            if random.randint(0, 4-i) and game_map[y, i-1] == "rocks":
                game_map[y, i] = "rocks"
        # Right
        for y, t in enumerate(game_map[:, width-i]):
            if random.randint(0, 4-i) and game_map[y, width-i] == "rocks":
                game_map[y, width-i-1] = "rocks"

    # 3. Fill coast
    create_coasts(game_map)

    # 4. Fill rocks, jungles, swamps
    empty = 0
    for y in range(0, height-1):
        for x in range(0, width-1):
            if game_map[y, x] == "empty":
                empty += 1
    available = round((empty - width*height/2) / 3)
    print(available)
    for area_type in ['rocks', 'jungles', 'swamps']:
        count = 0
        while count < available:
            area_size = random.randint(20, 40)
            count += area_size
            create_areas(game_map, area_type, area_size)

    # 5. Fill Savanna
    fill_savanna(game_map)

    # 6. Setup high tree, old camp and other single elements
    create_single_elements(game_map)

    return game_map


def create_water_line(game_map):
    width, height = game_map.shape[1], game_map.shape[0]

    # Select strat point
    start_col = random.randint(round(width*0.3), round(width*0.7))
    wide = 3

    for y in range(1, height - 1):
        start_col += random.choice([-1, 0, 1])
        wide += random.choice([-1, 0, 1])
        if wide < 3:
            wide = 3
        if wide > 5:
            wide = 5
        if start_col < 0:
            start_col = 0
        if start_col + wide > width:
            start_col = width - wide - 1
        for i in range(0, wide+1):
            game_map[y, start_col+i] = "water"


def create_coasts(game_map):
    for y in range(1, game_map.shape[0]-1):
        for x in range(1, game_map.shape[1]-1):
            if game_map[y, x] == "empty":
                if (game_map[y, x+1] == "water" or game_map[y, x-1] == "water" or
                        game_map[y+1, x] == "water" or game_map[y-1, x] == "water"):
                    game_map[y, x] = "coasts"


def create_areas(game_map, area_type, area_size, attempt=0):
    if attempt > 10:
        return
    attempt += 1
    while True:
        start_x, start_y = random.randint(1, game_map.shape[1] - 2), random.randint(1, game_map.shape[0] - 2)
        if game_map[start_y, start_x] == 'empty':
            # print(start_y, start_x)
            if try_to_fill_area(game_map, start_y, start_x, area_size, []):
                for y in range(1, game_map.shape[0] - 1):
                    for x in range(1, game_map.shape[1] - 1):
                        if game_map[y, x] == "tmp":
                            game_map[y, x] = area_type
            else:
                for y in range(1, game_map.shape[0] - 1):
                    for x in range(1, game_map.shape[1] - 1):
                        if game_map[y, x] == "tmp":
                            game_map[y, x] = "empty"
                create_areas(game_map, area_type, area_size, attempt)
            break


def try_to_fill_area(game_map, y, x, area_size, all_available_coords):
    game_map[y, x] = "tmp"
    area_size -= 1
    if area_size == 0:
        return True
    for shift_y, shift_x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        available_coord = (min(y+shift_y, height-1), min(x+shift_x, width-1))
        if game_map[available_coord] == "empty":
            all_available_coords.append(available_coord)
    if not all_available_coords:
        return False
    random_coord = random.choice(all_available_coords)
    all_available_coords = [
        c for c in all_available_coords if not (c[0] == random_coord[0] and c[1] == random_coord[1])
    ]
    return try_to_fill_area(game_map, *random_coord, area_size, all_available_coords)


def fill_savanna(game_map):
    for y in range(game_map.shape[0]):
        for x in range(game_map.shape[1]):
            if game_map[y, x] == "empty":
                game_map[y, x] = "savanna"


def create_single_elements(game_map):
    elements = ["high_tree", "old_camp", "camp", "broken_car"]
    for element in elements:
        for i in range(1, 4):
            place_single_element(game_map, element)


def place_single_element(game_map, element):
    empty_tiles = np.argwhere(game_map == "savanna")
    if len(empty_tiles) > 0:
        x, y = random.choice(empty_tiles)
        game_map[y, x] = element


def print_map(game_map):
    for row in game_map:
        print("".join([c[0] for c in row]))


# def prepare_map(game_map):
#     prepared_map =


width, height = 64, 64
generated_map = generate_map(width, height)
print_map(generated_map)
# prepared_map = prepare_map(generated_map)
