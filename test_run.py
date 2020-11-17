import argparse
import json

import mechanics
import print_board

# chess_board = mechanics.create_chess_board("Gardner")
chess_board = mechanics.create_chess_board("Jacobs–Meirovitz")
print_board.print_board(chess_board, True)

"""
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--piece", help="chess piece name: ex- rook, knight, pawn etc")
parser.add_argument("-l", "--location", help="chess notation string: ex- E4, D6 etc")
args = parser.parse_args()

"""


piece = "rook"
location = (0,2)
# According to the type of piece adjust function
if (piece == "rook"):
    print(json.dumps({"piece":piece,
                      "current_location": location,
                      "moves": mechanics.get_rook_moves(location, chess_board)}))


thing = mechanics.get_piece_at_position((4,3), chess_board)
print(thing)
"""
elif (piece == "knight"):
    print(json.dumps({"piece":piece,
                      "current_location": location,
                      "moves": mechanics.getKnightMoves(location, chess_board)}))


"""