def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    
    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter column (0-2): "))

        if board[row][col] != " ":
            print("This cell is already taken. Try again.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return
        
        player = "O" if player == "X" else "X"
    
    print_board(board)
    print("It's a draw!")
