#!/usr/local/bin/python3
'''
date: 2020-03-05
author: Nachiket Bhujbal
simple script used to quickly count words and chars in my application for the
OMSCS program at GaTech.
'''
import docx

DOCROOT = '/Users/nachiketbhujbal/OneDrive/Documents/GeorgiaTech/'

def process_docx():
    docpath = DOCROOT + 'goals_and_background_2020.docx'
    doc = docx.Document(docpath)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)

    return '\n'.join(fulltext)

def background_and_goals():
    print('background_and_goals:')

def statement_of_purpose():
    print('statement_of_purpose:')

def count_chars(essay):
    essay = essay.strip()
    lines = [x.strip() for x in essay.split('\n')]
    chars = 0
    for line in lines:
        if len(line) == 0:
            chars += 1
        else:
            chars += len(line)

    if chars > 1:
        print('Character Count: {}'.format(chars))

def count_words(essay):
    essay = essay.strip()
    lines = [x.strip().split() for x in essay.split('\n')]
    words = []
    for line in lines:
        words += line

    if len(words) > 0:
        print('Word Count: {}'.format(len(words)))
        print('Number of Unique words: {}'.format(len(set(words))))

def main():
    text = process_docx()
    print(text)


if __name__ == '__main__':
    main()
