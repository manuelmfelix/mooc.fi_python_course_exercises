# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x<0 or y<0 or x>2 or y>2:
        return False
    elif game_board[y][x] != "":
        print(game_board[y][x])
        return False
    else:
        game_board[y][x] = piece
        return True


if __name__ == "__main__":
    game_board = [['', 'X', 'X'], ['O', 'O', ''], ['O', '', 'X']]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)