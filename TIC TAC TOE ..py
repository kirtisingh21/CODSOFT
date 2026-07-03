board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()
player = "X"
for turn in range(9):
    print_board()
    pos = int(input("Enter position (1-9): ")) - 1
    if pos < 0 or pos > 8:
        print("Invalid Position!")
        continue
    if board[pos] == " ":
        board[pos] = player
    else:
        print("Position already filled!")
        continue
    if ((board[0] == board[1] == board[2] != " ") or
        (board[3] == board[4] == board[5] != " ") or
        (board[6] == board[7] == board[8] != " ") or
        (board[0] == board[3] == board[6] != " ") or
        (board[1] == board[4] == board[7] != " ") or
        (board[2] == board[5] == board[8] != " ") or
        (board[0] == board[4] == board[8] != " ") or
        (board[2] == board[4] == board[6] != " ")):
        print_board()
        print("Player", player, "wins!")
        break
    if player == "X":
        player = "O"
    else:
        player = "X"
else:
    print_board()
    print("Match Draw!")
