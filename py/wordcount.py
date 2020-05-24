#!/usr/local/bin/python3
'''
date: 2020-03-05
author: Nachiket Bhujbal
simple script used to quickly count words and chars in my application for the
OMSCS program at GaTech.

requirements:
lxml==4.5.1
Pillow==7.1.2
python-docx==0.8.10

pip install -U python-docx
'''
import docx

DOCROOT = '/Users/nachiketbhujbal/OneDrive/Documents/GeorgiaTech/'

def process_docx(docpath):
    doc = docx.Document(docpath)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)

    fulltext = '\n'.join(fulltext)
    count_words(fulltext)
    count_chars(fulltext)

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
    print('\ngoals_and_background:')
    docpath = DOCROOT + 'goals_and_background_2020.docx'
    text = process_docx(docpath)

    print('\nstatement_of_purpose:')
    docpath = DOCROOT + 'statement_of_purpose_2020.docx'
    text = process_docx(docpath)

if __name__ == '__main__':
    main()
