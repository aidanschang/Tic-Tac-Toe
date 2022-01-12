# tictactoe

## Overview
This tic tac toe game was wrote shortly after I finished my Information Structures with Python course. It is a simple logical program that doesn't involve any complex data structure but a nested list. Therefore, after I understood the logics of how to score the game, I wrote the entire program based out of how I like to play the game. With that, I added many details to increase user experience.

## User Interaction

### Duplicate placement
I raised an AttributeError when a player's input equals to 1 or 2 and AttributeError triggers except AttributeError. Results shown below:
  
![image](https://user-images.githubusercontent.com/84875731/149072117-b09a4d9c-292e-483d-8137-63004a02a16b.png)

### Draw
Tic Tac Toe is a game with 9 moves the most. As long as I am counting each player's move, I can easily track if a draw occured. In that case, the game automatically restart as below:

![image](https://user-images.githubusercontent.com/84875731/149072558-c088e6dd-e70c-4e1e-8457-c38c2d167eeb.png)

### Play Again
When a player won, it ask players if they want to play again. If yes, the game restart and the letter can be lower or uppercase. I think it's a nice little touch.

![image](https://user-images.githubusercontent.com/84875731/149072660-7638c1f1-a15a-4e50-986e-f23f31882be0.png)



