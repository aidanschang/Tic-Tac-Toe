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
    # a,b,c is used to determine which index in a nested list that the player chose
    if column == 'a':
        index_c= 0
    elif column == 'b':
        index_c = 1
    elif column == 'c':
        index_c = 2
    #see if user placement has a value of 1 or 2, if yes, raise AttributeError
    if game_board[index_r][index_c] in range(1,3):
         raise AttributeError
    #mark the game board with player's move
    else:
        game_board[index_r][index_c]= mark

    #print game board
    print("   a  b  c  ")
    for row_index, board in enumerate(game_board):
        print(row_index, board)

    #check if a player has won the game

    if game_board[0]== [n, n, n] or game_board[1]== [n, n, n] or game_board[2]== [n, n, n]:
        print("\nPlayer {} win!".format(player))
        raise LookupError
    elif game_board[0][0] == n and game_board[1][0] == n and game_board[2][0] == n:
        print("\nPlayer {} win!".format(player))
        c=12
        raise LookupError
    elif game_board[0][1] == n and game_board[1][1] == n and game_board[2][1] == n:
        print("\nPlayer {} win!".format(player))
        c=12
        raise LookupError
    elif game_board[0][2] == n and game_board[1][2] == n and game_board[2][2] == n:
        print("\nPlayer {} win!".format(player))
        c=12
        raise LookupError
    elif game_board[0][0] == n and game_board[1][1] == n and game_board[2][2] == n:
        print("\nPlayer {} win!".format(player))
        c=12
        raise LookupError
    elif game_board[0][2] == n and game_board[1][1] == n and game_board[2][0] == n:
        print("\nPlayer {} win!".format(player))
        c=12
        raise LookupError

while True:
    print("            Welcome to Aidan's Tic Tac Toe!!\n{}".format('_'*60))
    print("   a  b  c  ")
    for row_index, board in enumerate(game_board):
            print(row_index, board)

    #c represents number of rounds but -2
    c = 0

    while c < 10:
        if c== 9:
            #Draw if total moves combined equals to 9
            print("Draw!")
            # if draw, reset the board
            game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            c = 12
            break
        if c%2==0:
            try:
                row, column = input("\nPlayer 1, please enter row and column separated by space: ").split(' ')
                player = '1'
                game_set(player, row, column)
                c+= 1
            except AttributeError:
                print("Someone has already played here!")
                continue
            except LookupError:
                c = 12
            except:
                print("You did not place your move correctly, please re-enter!")
                continue
        elif c%2 ==1:
            try:
                row, column = input("\nPlayer 2, please enter row and column separated by space: ").split(' ')
                player = '2'
                game_set(player, row, column)
                c+=1
            except AttributeError:
                print("Someone has already played here!")
                continue
            except:
                print("You did not place your move correctly, please re-enter!")
                continue
    else:
        x= input("\nDo you want another game(Y/N)?: ")
        x= x.upper()
        if x== 'Y':
            c=2
            game_board= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        else:
            print("\nThank you for playing!")
            break
