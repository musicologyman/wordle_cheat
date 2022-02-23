from copy import copy
from functools import cache
import sqlite3

ALL_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

@cache
def get_all_words():
    with sqlite3.connect('words.db') as cn:
        cur = cn.cursor()
        cur.execute('SELECT word FROM five_letter_words')
        return [row[0] for row in cur.fetchall()]

def reduce_letter_list(letters_to_ignore):
    permitted_letters = copy(ALL_LETTERS)
    for c in permitted_letters:
        permitted_letters.remove(c)

    return permitted_letters

def find_words():
    return [word for word in get_all_words()
            if word[:2] == 'o']
    
def main():
    print(find_words())

if __name__ == '__main__':
    main()

