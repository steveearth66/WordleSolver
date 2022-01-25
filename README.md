# WordleSolver
uses Entropy to find the best next guess for Wordle, given the color clues

use player.py and enter in the string for the suggested clue word: use Y for yellow, G for Green, and x for blank

of the 2315 words, it solves 44 of them in 2 tries, 1219 in 3 tries, 988 in 4 tries, 63 in 5 tries, and 1 takes all 6 tries ("waver")

allowed.txt = all words Wordle considers legal for guessing\n
guesses.txt = how many guesses my Solver takes for each possible target\n
player.py = the python program which plays the game\n
ranker.py = a slight modification of the player.py program which generated guesses.txt\n
wordlist.txt = all possible target words used by Wordle (as of Jan 2022)
