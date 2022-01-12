# tictactoe

## Overview
This tic tac toe game was wrote shortly after I finished my Information Structures with Python course. After I understood how the principle of the game works, I spent a little more than an hour to complete and fine-tune the detail.

## Interaction

### Duplicate placement
From the user experience perspective, I made sure to handle duplicate placement more interactive as below:
  
  a  b  c\ 
0 [2, 0, 0]\
1 [0, 1, 0]\
2 [0, 0, 0]\
Player 1, please enter row and column separated by space: 0 a
Someone has already played here!
Player 1, please enter row and column separated by space: 0 b\
   a  b  c\  
0 [2, 1, 0]\
1 [0, 1, 0]\
2 [0, 0, 0]\

### Draw
When a draw occured, the game automatically restart as below:

![image](https://user-images.githubusercontent.com/84875731/149071880-67852eb8-f410-41b9-b1e4-aab8e10e63bf.png)

