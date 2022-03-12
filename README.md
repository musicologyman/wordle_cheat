# Wordle Cheat


## Description
Wordle cheat is a tool for assisting the user in solving a Wordle puzzle. It does this by filtering an extensive list of five-letter words according to the constraints that a user provides. The constraints are

1. disallowed letters
2. allowed letters
3. letters that are known to be part of the word but are not in their proper places
4. letters that are known to be part of the word that are in their proper positions

The tool produces a list of candidate words given the constraints that the user has provided to the script. The user can then choose one of the candidates as a Wordle guess.

## Compatibility
This script has been run using python versions 3.9 and 3.10, but it's simple enough that it's probably backward compatible to any version that supports generator expressions.

## Setup
To use wordle_cheat, it's necessary first to run the script **`setup.py`.** Running this script will create a SQLite 3 database (named **`five_letter_words.sqlite3`)** with a single table **(`words`)** with all the words from the file **`five_letter_words.txt`.** 

## Notes

### 12 Mar 2022
At this point, it's necessary for the programmer to make ad hoc changes to fit the script to their needs for a particular puzzle.

The code here was used for solving the Wordle puzzle of the day for 12 Mar. 2022.

The constrains listed above suggest the path forward for coding a generalization of this tool. 

 