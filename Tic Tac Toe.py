game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def game_set(player, row, column):
    """This function modified game board according to row/column index that a player played,
    then it calculates if the player has won the game"""

    #modified game board according to player's input
    index_r= int(row)
    if player == '1':
        mark = 1
        n = 1
    elif player == '2':
        mark = 2
        n = 2
    if column == 'a':
        index_c= 0
    elif column == 'b':
        index_c = 1
    elif column == 'c':
        index_c = 2
    if game_board[index_r][index_c] in range(1,3):
         raise AttributeError
    else:
        game_board[index_r][index_c]= mark

    #print game board
    print("   a  b  c  ")
    for row_index, board in enumerate(game_board):
        print(row_index, board)

    #check if a player has won the game
    if game_board[0]== [n, n, n] or game_board[1]== [n, n, n] or game_board[2]== [n, n, n]:
        print("Player 1 win!")
        raise LookupError
    elif game_board[0][0] == n and game_board[1][0] == n and game_board[2][0] == n:
        print("player 1 win!")
        c=12
        raise LookupError
    elif game_board[0][1] == n and game_board[1][1] == n and game_board[2][1] == n:
        print("player 1 win!")
        c=12
        raise LookupError
    elif game_board[0][2] == n and game_board[1][2] == n and game_board[2][2] == n:
        print("player 1 win!")
        c=12
        raise LookupError
    elif game_board[0][0] == n and game_board[1][1] == n and game_board[2][2] == n:
        print("player 1 win!")
        c=12
        raise LookupError
    elif game_board[0][2] == n and game_board[1][1] == n and game_board[2][0] == n:
        print("player 1 win!")
        c=12
        raise LookupError

while True:
    print("            Welcome to Aidan's Tic Tac Toe!!\n{}".format('_'*60))
    print("   a  b  c  ")
    for row_index, board in enumerate(game_board):
            print(row_index, board)
    c = 2
    while c < 12:
        if c== 11:
            print("Draw!")
            c = 12
            break
        if c%2==0:
            try:
                row, column = input("Player 1, please enter row and column separated by space: ").split(' ')
                player = '1'
                game_set(player, row, column)
                c+= 1
            except AttributeError:
                print("Someone has already played here!")
                continue
            except LookupError:
                c = 12
            except:
                print("Input error!")
                continue
        elif c%2 ==1:
            try:
                row, column = input("Player 2, please enter row and column separated by space: ").split(' ')
                player = '2'
                game_set(player, row, column)
                c+=1
            except AttributeError:
                print("Someone has already played here!")
                continue
            except:
                print("Input error!")
                continue
    else:
        x= input("Do you want another game(Y/N)?: ")
        if x== 'Y':
            c=2
            game_board= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        else:
            "Thank you for playing!"
            break
