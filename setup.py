#!/usr/bin/env python3
import sqlite3

CREATE_TABLE_STMT = 'CREATE TABLE words (word TEXT NOT NULL)'
DB_NAME = 'five_letter_words.sqlite3'
INSERT_STMT = 'INSERT INTO words(word) VALUES(:word)'
WORDS_FILE = 'five_letter_words.txt'

def read_words(words_file=WORDS_FILE):
    with open(words_file) as fp:
        return [line[:-1] for line in fp]

def save_db(cn_src, name=DB_NAME):
    with sqlite3.connect(name) as cn_dest:
        cn_src.backup(cn_dest)

def create_database(name=DB_NAME):
    with sqlite3.connect(':memory:') as cn:
        cn.execute(CREATE_TABLE_STMT)
        save_db(cn, name)

def populate_database(words, name=DB_NAME):
    with sqlite3.connect(name) as cn:
        for word in words:
            cn.execute(INSERT_STMT, {'word': word})

        cn.commit()

def main():
    create_database()
    words = read_words()
    populate_database(words)

if __name__ == '__main__':
    main()

