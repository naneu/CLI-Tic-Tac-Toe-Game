# CLI-Tic-Tac-Toe-Game
## About the game

Tic-tac-toe is a two-player game, that is played on a 3×3 square grid. Each player occupies a cell in turns, with the objective of placing three marks in a horizontal, vertical, or diagonal pattern. One player uses cross `'X'` as his marker, while the other uses a naught `'0'`.

## Algorithm 

1. ##### create a board using a using dictionaries  and initialize each element as empty

2. ##### write a function to show the board{the board will be shown multiple times}

3. ##### write a function to check whether a player has won or not

   - a player can win after the fifth move so we start checking after i.e. count >= 5
   - only check for draw after the last move i.e . at count == 9

4. ##### write a function to show the scoreboard once the game is over(either player wins or a draw)

5. ##### write a function to start the game

   - Write an infinite loop that breaks when the game is over (either win or draw).
     - Show the board to the user to select the spot for the next move.
     - Ask the user to enter the row and column number.
     - Update the spot with the respective player sign.
     - Check whether the current player won the game or not.
     - If the current player won the game, then print a winning message and break the infinite loop.
     - If the board is filled, then print the draw message and break the infinite loop.
   - Finally, show the user the final view of the board.
