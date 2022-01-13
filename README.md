# Tic Tac Toe

## Overview
This tic tac toe game was wrote shortly after I finished my Information Structures with Python course in May 2021. It is a simple program that doesn't require any complex data structure, and it was an excellent practice for someone who just started learning coding. After I understood the logics to create the game board, I wrote the entire program based out of how I like to play the game. With that, I added many details to the game to further increase playability.

## Player Interaction Features

### Duplicate placement
The default value of each placement is 0. Depending on which player made the move, the placement values changes to 1 or 2. Therefore, I raised an AttributeError when a player played a move that the value of it is not 0. As results, AttributeError triggers except AttributeError and error message is printed. Results shown below:
  
![image](https://user-images.githubusercontent.com/84875731/149072117-b09a4d9c-292e-483d-8137-63004a02a16b.png)

### Draw
Tic Tac Toe is a simple game with a total of 9 moves in one game. So if I am counting each player's move, I can easily track if a draw occured, if no one has won. If draw, the game <u>automatically</u> restart as shown below:

![image](https://user-images.githubusercontent.com/84875731/149072558-c088e6dd-e70c-4e1e-8457-c38c2d167eeb.png)

### Play Again
When a player won, it ask players if they want to play again. If yes, the game restart and the letter can be lower or uppercase. I think it's a nice little touch.

![image](https://user-images.githubusercontent.com/84875731/149072660-7638c1f1-a15a-4e50-986e-f23f31882be0.png)



