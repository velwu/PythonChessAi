import argparse
import json
import chess
import print_board

def get_piece_at_position(pos, chess_board):
    # print("Position queried:", pos)
    the_one_piece = chess_board[pos[0]][pos[1]]
    map_letter_reps_to_piece_names = {
        'R': 'Black Rook', 'N': 'Black Knight', 'B': 'Black Bishop',
        'Q': 'Black Queen', 'K': 'Black King', 'P': 'BLack Pawn',
        'r': 'White Rook', 'n': 'White Knight', 'b': 'White Bishop',
        'q': 'White Queen', 'k': 'White King', 'p': 'White Pawn',
        '.': 'nothing'
    }


    # print("The piece at", pos, "is a", map_letter_reps_to_piece_names[the_one_piece])
    return the_one_piece

def create_chess_board(variant_name):

    chess_board = [[".", ".", ".", ".", "."] for i in range(5)]

    if variant_name == "Gardner":
        chess_board[0] = ['R', 'N', 'B', 'Q', 'K']
        chess_board[1] = ['P' for p in range(5)]
        chess_board[-2] = ['p' for p in range(5)]
        chess_board[-1] = ['r', 'n', 'b', 'q', 'k']

    if variant_name == "Jacobs–Meirovitz":
        chess_board[0] = ['B', 'N', 'R', 'Q', 'K']
        chess_board[1] = ['P' for p in range(5)]
        chess_board[-2] = ['p' for p in range(5)]
        chess_board[-1] = ['k', 'q', 'r', 'n', 'b']

    elif variant_name == "Mallett":
        chess_board[0] = ['R', 'B', 'Q', 'K', 'B']
        chess_board[1] = ['P' for p in range(5)]
        chess_board[-2] = ['p' for p in range(5)]
        chess_board[-1] = ['r', 'n', 'q', 'k', 'n']

    # print("Board type:", variant_name, "\n", *chess_board, sep="\n")
    print("Board type:", variant_name)
    return chess_board

#TODO: Implement Crusader moves first
#TODO: Ask during OH how Archer moves can be implemented


def get_rook_moves(pos, chess_board):
    """ A function that returns the all possible moves of a Rook at a given position
        pos: The current position of the Rook
        chess_board: The current game board state represented by a 2D array/list
    """
    solution_moves = []
    # Look for potential moves in the same row
    for j in range(len(chess_board)):
        if j != pos[1]:
            solution_moves.append((pos[0], j))

    # Look for potential moves in the same column
    for i in range(len(chess_board)):
        if i != pos[0]:
           solution_moves.append((i, pos[1]))

    solution_moves.sort()
    print("Rook moves without collisions from", pos, ":", solution_moves)


    for each_move_choice in solution_moves:
        # Condition: If the target position is not empty
        if get_piece_at_position(each_move_choice, chess_board) != ".":
            # Condition: If it is occupied by an friendly piece
            if get_piece_at_position(each_move_choice, chess_board).isupper() == get_piece_at_position(pos, chess_board).isupper():
                solution_moves = [x for x in solution_moves if x != each_move_choice]
                print(solution_moves)
            # TODO: Finish this section
            # Condition: If it is occupied by an enemy piece
    return solution_moves
        

    




"""
def getKnightMoves(pos, chess_board):

    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_alpha_to_index[column]
    i,j = row, column
    solution_moves = []
    try:
        temp = chess_board[i + 1][j - 2]
        solution_moves.append([i + 1, j - 2])
    except:
        pass
    try:
        temp = chess_board[i + 2][j - 1]
        solution_moves.append([i + 2, j - 1])
    except:
        pass
    try:
        temp = chess_board[i + 2][j + 1]
        solution_moves.append([i + 2, j + 1])
    except:
        pass
    try:
        temp = chess_board[i + 1][j + 2]
        solution_moves.append([i + 1, j + 2])
    except:
        pass
    try:
        temp = chess_board[i - 1][j + 2]
        solution_moves.append([i - 1, j + 2])
    except:
        pass
    try:
        temp = chess_board[i - 2][j + 1]
        solution_moves.append([i - 2, j + 1])
    except:
        pass
    try:
        temp = chess_board[i - 2][j - 1]
        solution_moves.append([i - 2, j - 1])
    except:
        pass
    try:
        temp = chess_board[i - 1][j - 2]
        solution_moves.append([i - 1, j - 2])
    except:
        pass

    # Filter all negative values
    temp = [i for i in solution_moves if i[0] >=0 and i[1] >=0]
    allPossibleMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    allPossibleMoves.sort()
    return allPossibleMoves

"""


# TEST CODES below: Might delete later~

#test_board_1 = create_chess_board("Gardner")
#print_board.print_board(test_board_1, True)

#test_board_2 = create_chess_board("Mallett")
#print_board.print_board(test_board_2, True)
