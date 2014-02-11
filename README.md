Roshambot
=========

A Python/Sage framework for creating rock-paper-scissors bots and testing them against one another.

Includes some examples of machine learning algorithms, described at the author's blog: http://inventingsituations.net/tag/rps/

Getting Started
---------------

The script is best used with iPython or Sage.  All functionality should work fine in standard iPython except for the plot command for the game master, which is written with Sage in mind.

*Choosing Players* - There are a wide array of RPS players in the main file.  Each is implemented as an individual class.  The required methods for a player-bot are a `get_move` method and a `report` method.  `get_move` decides on the next move to play, and `report` is called by the game master after each round to tell the bot how things played out.  `rps_random` is a good template to start from if you would like to make your own. Note that some bots, like `bayes`, can also take arguments when initialized.

*The Game Master* - The `game_master` class is used to pit two bots against each other.  For example: 

`R=random_rps(); S=switchbot(); G=game_master(R,S); G.run_game(); print G.score` 

will initialize the players `random_rps` and `switchbot`, then play 1001 rounds of iterated rock paper scissors, then print the final score.

*Tournaments* - The `tournament` function can be used to play a large number of games amongst a collection of bots.  It will then print out the results of the tournament.

