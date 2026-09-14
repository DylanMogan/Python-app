import game_setup, config
x = 0
y = 0

while y < config.size:
    y += 1
    x = 0
    while x < config.size:
        gameboard_info_instance = game_setup.info.copy()
        x += 1
        cords = (x,y)
        gameboard_info_instance['cords'] = cords
        game_setup.gameboard_pieces.append(gameboard_info_instance)