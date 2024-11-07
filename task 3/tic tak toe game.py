def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        game_over = False

        print("Welcome to Tic-Tac-Toe!")
        print_board(board)

        while not game_over:
            try:
                row = int(input(f"Player {current_player}, enter the row (0-2): "))
                col = int(input(f"Player {current_player}, enter the column (0-2): "))
                
                if row not in range(3) or col not in range(3):
                    print("Invalid input! Please enter row and column between 0 and 2.")
                    continue

                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue

                board[row][col] = current_player
                print_board(board)

                if check_win(board, current_player):
                    print(f"Player {current_player} wins!")
                    game_over = True
                elif check_draw(board):
                    print("It's a draw!")
                    game_over = True
                else:
                    current_player = "O" if current_player == "X" else "X"
            
            except ValueError:
                print("Invalid input! Please enter numbers between 0 and 2.")
        
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing!")
            break

play_game()
