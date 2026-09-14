'''
Chess
main code for game
'''
import game_setup, create_gameboard
create_gameboard

for game_piece in game_setup.gameboard_pieces:
    print(f'{game_piece}')

input("\nPress Enter to exit...")