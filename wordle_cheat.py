from copy import copy
from functools import cache
import sqlite3
import shutil

ALL_LETTERS = list('abcdefghijklmnopqrstuvwxyz')
WORDS_DB = 'five_letter_words.sqlite3'

@cache
def get_all_words():
    with sqlite3.connect(WORDS_DB) as cn:
        cur = cn.cursor()
        cur.execute('SELECT word FROM words')
        return [row[0] for row in cur.fetchall()]

def reduce_letter_list(letters_to_ignore):
    permitted_letters = copy(ALL_LETTERS)
    for c in permitted_letters:
        permitted_letters.remove(c)

    return permitted_letters

def filter_words(letters_to_ignore):
    for word in get_all_words():
        if not (word[1] == 'o' and word[3] == 'a'):
            continue
        if not 'y' in list(word) or word[2] == 'y':
            continue
        for c in letters_to_ignore:
            if c in list(word):
                break
        yield word


def find_words():
    letters_to_ignore = list('aceiklmnrsw')
    filtered_words = filter_words(letters_to_ignore)
    
    columns, _ = shutil.get_terminal_size()
    words_per_line = columns // 7
    for i, word in enumerate(filtered_words):
        if i % words_per_line == 0:
            print()
        print(word, end=', ')
    
    print()
    
    
def main():
    print(find_words())

if __name__ == '__main__':
    main()

