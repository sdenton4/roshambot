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

The default tournament produces the following kind of output:

    sage: %time tournament()
    Number of players:  23
    Games per player:  66
    Average number of games won:  32.8
    Sdev of games won:  15.5
    55 	|   Bayes 3
    53 	|   Rfind
    50 	|   Bayes 5
    50 	|   Terminator
    49 	|   Bayes 1
    49 	|   Bayes 4
    48 	|   Bayes 2
    47 	|   Frequentist 3
    46 	|   Frequentist 4
    45 	|   Bayes 6
    36 	|   Michael Jackson
    33 	|   Naive Bayes 1
    28 	|   Randy
    27 	|   ho0m4nbot
    26 	|   Naive Bayes 20
    21 	|   Freqbot
    18 	|   Switchbot
    16 	|   Smrt Homer
    14 	|   Edward Scissorhands
    13 	|   Lisa Simpson
    12 	|   Random bias (0.11, 0.87)
    10 	|   Bart Simpson
    9 	|   noskcaJ leahciM
    CPU times: user 27.88 s, sys: 0.07 s, total: 27.95 s
    Wall time: 28.01 s

followed by a matrix encoding how many games were won between pairs of bots.
