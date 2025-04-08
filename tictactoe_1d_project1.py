PLAYER_MARK = "x"
PC_MARK = "o"


def evaluate(board):
    if "xxx" in board:
        return "x"
    elif "ooo" in board:
        return "o"
    elif "-" not in board:
        return "!"
    else:
        return "-"


def move(board, mark, position):
    if position < 0:
        raise ValueError("The position cannot be negative!")
    board_updated = list(board)
    board_updated[position] = mark
    return "".join(board_updated)


def player_move(board):
    while True:
        position = int(input("Which position do you want to move?"))
        if position >= 0 and position < len(board):
            if board[position] == "-":
                break
        print("The entered position is not valid, try again")
    new_board = move(board, PLAYER_MARK, position)
    print(new_board)
    return new_board


def pc_move(board):
    from random import randrange

    position_pc = randrange(0, 19)
    if board[position_pc] == "-":
        new_board = move(board, PC_MARK, position_pc)
        print(new_board)
        return new_board
    else:
        print("The position is not available, try again")
        return pc_move(board)


def tictactoe_1d():
    game_board = "-" * 20
    print(game_board)
    while evaluate(game_board) == "-":
        game_board = player_move(game_board)
        if evaluate(game_board) == "x":
            print("You have won!")
            break
        elif evaluate(game_board) == "o":
            print("The computer won")
            break
        elif evaluate(game_board) == "!":
            print("Nobody won, the game is over!")
            break

        game_board = pc_move(game_board)
        if evaluate(game_board) == "x":
            print("You have won!")
            break
        elif evaluate(game_board) == "o":
            print("The computer won")
            break
        elif evaluate(game_board) == "!":
            print("Nobody won, the game is over!")
            break


if __name__ == "__main__":
    tictactoe_1d()
