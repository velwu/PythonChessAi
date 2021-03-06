import chess
#import sunfish
import math
import random
import sys
import print_board as pbv

# Package required: https://pypi.org/project/python-chess/
# pip install python-chess

def minimaxRoot(depth, board,isMaximizing):
    possibleMoves = board.legal_moves
    bestMove = -9999
    secondBest = -9999
    thirdBest = -9999
    bestMoveFinal = None

    print("Depth: ", (4 - depth + 1), " ", len(list(possibleMoves)), " Possible Moves")

    for x in possibleMoves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        # value = max(bestMove, minimax(depth - 1, board, not isMaximizing))
        current_val = max(bestMove, minimax(depth - 1, board, not isMaximizing))
        value = max(bestMove, current_val)
        print("Move:", x, " Value:", current_val)
        board.pop()
        if( value > bestMove):
            print("Best score: " ,str(bestMove))
            print("Best move: ",str(bestMoveFinal))
            print("Second best: ", str(secondBest))
            thirdBest = secondBest
            secondBest = bestMove
            bestMove = value
            bestMoveFinal = move
    return bestMoveFinal

def minimax(depth, board, is_maximizing):
    if(depth == 0):
        return -evaluation(board)

    possibleMoves = board.legal_moves

    print("Depth: ", (4 - depth + 1), " ", len(list(possibleMoves)), " Possible Moves")

    # TODO: Restore the print statement when not playing
    # print(possibleMoves)
    if(is_maximizing):
        bestMove = -9999
        for x in possibleMoves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            # bestMove = max(bestMove,minimax(depth - 1, board, not is_maximizing))
            mm_thing = minimax(depth - 1, board, not is_maximizing)

            bestMove = max(bestMove, mm_thing)
            # print("X:", x, "best move:", bestMove)
            board.pop()
        return bestMove
    else:
        bestMove = 9999
        for x in possibleMoves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            bestMove = min(bestMove, minimax(depth - 1, board, not is_maximizing))
            # print("X:", x, "best move:", bestMove)
            board.pop()
        return bestMove


#def calculateMove(board):
#    possible_moves = board.legal_moves
#    if(len(possible_moves) == 0):
#        print("No more possible moves...Game Over")
#        sys.exit()
#    bestMove = None
#    bestValue = -9999
#    n = 0
#    for x in possible_moves:
#        move = chess.Move.from_uci(str(x))
#        board.push(move)
#        boardValue = -evaluation(board)
#        board.pop()
#        if(boardValue > bestValue):
#            bestValue = boardValue
#            bestMove = move
#
#    return bestMove

def evaluation(board):
    i = 0
    evaluation = 0
    x = True
    try:
        x = bool(board.piece_at(i).color)
    except AttributeError as e:
        x = x
    while i < 63:
        i += 1
        evaluation = evaluation + (getPieceValue(str(board.piece_at(i))) if x else -getPieceValue(str(board.piece_at(i))))
    return evaluation

def getPieceValue(piece):
    if(piece == None):
        return 0
    value = 0
    if piece == "P" or piece == "p":
        value = 10
    if piece == "N" or piece == "n":
        # value = 30
        value = 70
    if piece == "B" or piece == "b":
        value = 30
    if piece == "R" or piece == "r":
        value = 50
    if piece == "Q" or piece == "q":
        # value = 90
        value = 1500
    if piece == 'K' or piece == 'k':
        # value = 900
        value = 2000
    #value = value if (board.piece_at(place)).color else -value
    return value

def main():
    board = chess.Board()
    n = 0
    pbv.print_board(board, False)
    while n < 100:
        if n%2 == 0:
            move = input("Enter move: ")
            move = chess.Move.from_uci(str(move))
            board.push(move)
        else:
            print("Computers Turn:")
            # move = minimaxRoot(4,board,True)
            # move = minimaxRoot(1,board,False)
            move = minimaxRoot(4, board, True)
            move = chess.Move.from_uci(str(move))
            board.push(move)
        pbv.print_board(board, False)
        n += 1





if __name__ == "__main__":
    main()