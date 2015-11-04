# Mini Project 3, Minimax Tic Tac Toe
# Principles of Computing, Part 2
# Jordan Hall
# 11/3/2015
"""
Mini-max Tic-Tac-Toe Player
"""

#import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
#import codeskulptor
#codeskulptor.set_timeout(120)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    if board.check_win() is not None:
        return SCORES[board.check_win()], (-1, -1)
        
    else:
        scores_and_moves = []
        for r_idx, c_idx in board.get_empty_squares():
            temp_board = board.clone()
            temp_board.move(r_idx, c_idx, player)
            score, move = mm_move(temp_board, provided.switch_player(player))
            if (score == 1 and player == provided.PLAYERX) or (score == -1 and player == provided.PLAYERO):
                return score, (r_idx, c_idx)
            scores_and_moves.append((score, (r_idx, c_idx)))
        
        if player == provided.PLAYERX:
            best_score = max([elem[0] for elem in scores_and_moves])
        else:
            best_score = min([elem[0] for elem in scores_and_moves])
        
        for score, move in scores_and_moves:
            if score == best_score:
                return score, move

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

provided.play_game(move_wrapper, 1, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)