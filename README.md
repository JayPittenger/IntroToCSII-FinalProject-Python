# IntroToCSII-FinalProject-Python
Python program that simulates the game of Xiangqi, or Chinese Chess

Note: Permission was obtained from instructor to publicly host this final project. 

For specific rules on the game of XiangQi, please refer to the Wikipedia article on the game:
https://en.wikipedia.org/wiki/Xiangqi

# Description

This python program allows players to play a game of Xianqi and tracks both the red team and the black team.
Once an instance of XianqiGame class is initialized, methods are run on that object to perform moves to play the game.
Methods can be run to make a move of a game piece by defining the position on the board that the piece is, as well as 
passing in the destination coordinate of the desired move. The game keeps track of the current state of the game board.

If it is not currently the turn of the team who owns the piece at the specified location, the game will not allow
the move to be made.

There are classes for each type of piece in the game, and depending on the piece, this defines what kinds of moves can
be made and how that particular piece captures opponent pieces. If the move desired is not valid for the type of piece
at the source coordinate, the game will not allow the move to be made.

The game also tracks whether or not each team is in check or checkmate. The game can be won by one team putting the other
in checkmate, or by capturing all of the pieces, or by a team being put in stalemate. The game will not allow a team to 
make a move that puts themselves in check. There is a method that can be run and passed a team name (either RED or BLACK), 
and that method will return true if that team is in check and false if not.

The game records if someone has won the game, and what team that is and will not allow any further moves to be made once 
a team has won. To determine which team has one if the game has finished, get_game_state method can be run on the 
XiangQiGame class. 

# Key Takeaways

- Class and method organization - object oriented programming design
- Inheritance for all the game pieces, which each inherit from Piece class parent
- Recursion to determine valid moves which helps the game determine if a particular team is in check or checkmate
- Input validation for correct positions on the board when a move is being made
