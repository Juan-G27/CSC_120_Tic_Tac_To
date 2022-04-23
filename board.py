board = [["-" for i in range(3)] for j in range(3)]
spaces = 3


def print_board():
    print('Board:')
    for row in board:
        print(row)


def check_mark(row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid inputs, please enter numbers (0-2)")
        return False
    if board[row][col] != "-":
        print("This spot in the board is already in use. ".format(row, col))
        return False
    return True


def place_mark(player, row, col):
    if player == 1:
        mark = "X"
    elif player == 2:
        mark = "O"
    board[row][col] = mark
    print("\nPlayer {} added mark at the location {},{}".format(player, row, col))
    if check_win(mark, row, col):
        return player


def check_win(symbol, row, col):
    if all_rows(col, symbol):
        return True

    if all_cols(row, symbol):
        return True

    if left_dia(row, col, symbol):
        return True

    if right_dia(row, col, symbol):
        return True

    return False


def all_rows(col, s):
    for row in range(spaces):
        if board[row][col] != s:
            return False
    return True


def all_cols(row, s):
    for col in range(spaces):
        if board[row][col] != s:
            return False
    return True


def left_dia(row, col, s):
    if row != col:
        return False
    for i in range(spaces):
        if board[i][i] != s:
            return False
    return True


def right_dia(row, col, s):
    if row + col != spaces - 1:
        return False
    j = spaces - 1
    for i in range(spaces):
        if board[i][j] != s:
            return False
        j -= 1
    return True


def main():
    num = 0
    player = 1
    while num < 9:
        if num % 2 == 0:
            player = 1
        else:
            player = 2
        print_board()
        print("\nPlayer {}, enter your spot on the board".format(player))
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if not check_mark(row, col):
            print("Invalid inputs try again")
            continue
        win = place_mark(player, row, col)
        if win == 1:
            print("Player 1 wins")
            break
        elif win == 2:
            print("Player 2 wins")
            break
        num += 1


main()
