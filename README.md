Dice Game
Description
This is a Python-based dice game where players roll three dice to achieve the highest score. The game introduces an exciting mechanic where if all three dice show the same value ("tuple out"), the player’s score for that turn becomes zero. Players can choose to re-roll unfixed dice to improve their chances of a high score.

How to Play
At the start of each turn, all three dice are rolled.
The dice values are displayed, and the player can decide whether to re-roll unfixed dice.
If all three dice show the same value ("tuple out"), the turn ends immediately with a score of 0.
Players can "fix" dice automatically if two of them match, preventing those dice from being re-rolled.
Players can continue re-rolling unfixed dice until they decide to stop or tuple out.
Once the player stops re-rolling, the sum of the dice values is calculated as the score for that turn (unless tupled out).
Controls
Start a Turn: The game automatically begins a new turn when the player decides to play.
Re-roll Dice: Type y when prompted to re-roll unfixed dice.
End Turn: Type n when prompted to stop re-rolling.
Play Again: After a turn ends, type y to play another turn or n to exit the game.
Rules
If all three dice have the same value ("tuple out"), the turn ends with a score of 0.
If two dice match, those dice are automatically fixed, and only the third dice can be re-rolled.
The final score for the turn is the sum of all dice values unless tupled out.
Requirements
Python 3.x
random module (standard library)
Installation
Save the script as dice_game.py on your system.
Ensure Python 3.x is installed.
Run the script using the command:
python dice_game.py
