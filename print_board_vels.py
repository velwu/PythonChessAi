import chess
#import sunfish
import math
import random
import sys
import Minimax as mnm
def print_board(board_class):
    uni_pieces = {'R':' ♜ ', 'N':' ♞ ', 'B':' ♝ ', 'Q':' ♛ ', 'K':' ♚ ', 'P':' ♟ ',
                  'r':' ♖ ', 'n':' ♘ ', 'b':' ♗ ', 'q':' ♕ ', 'k':' ♔ ', 'p':' ♙ ', '.':' 口 '}

    board_obj = str(board_class)
    #print(board_test)

    for key in uni_pieces.keys():
        board_obj = board_obj.replace(key, uni_pieces[key])
    print(board_obj)