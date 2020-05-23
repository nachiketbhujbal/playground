#!/usr/local/bin/python3
'''
date: 2020-03-05
author: Nachiket Bhujbal
simple script used to quickly count words and chars in my application for the
OMSCS program at GaTech.
'''


def background_and_goals():
    essay = (
    """
    I graduated with a Bachelor of Science in Engineering Physics from the
    University of Illinois at Urbana-Champaign. My specialization was in
    Computational Physics, with a minor in Computer Science. My cumulative GPA
    by graduation was 3.01/4.0.

    During my undergraduate career, I spent time doing research was in a
    soybean genomics lab. This inspired me to further my education in computer
    science. However, primarily the financial markets drove much of my
    curiosity, where my education in physics helped me draw conclusions between
    the physical and the financial worlds.

    Now, I spend my days wrangling with complex and large sets of financial
    data across all types of markets, from stocks and bonds, to complex
    derivatives like futures and options. Using the language of math to
    formalize the relationships between these various sets of data, and the
    tools of physics to break down these problems into fundamental units, I can
    start putting together the pieces of this enourmous puzzle.

    It takes a significant amount of time translating this math, often
    expressed in continuous forms, to the language of computers (programming
    languages), which involves discretization and implementing various
    numerical methods and solutions. These are the types of problems I deal
    with on a day to day basis. These are fun problems to me.

    If the kinds of problems I’ve described above are familiar to you and
    you’re interested in working together to solve these kinds of problems, or
    you just want to network and connect, feel free to chat and get in touch!
    If you're all the way down here, thanks for reading and I hope you enjoyed
    my summary!
    """
    )
    count_words(bggessay)
    count_chars(bggessay)

def statement_of_purpose():
    essay = (
    """

    """
    )
    count_words(bggessay)
    count_chars(bggessay)

def count_chars(essay):
    essay = essay.strip()
    lines = [x.strip() for x in essay.split('\n')]
    chars = 0
    for line in lines:
        if len(line) == 0:
            chars += 1
        else:
            chars += len(line)

    print('Character Count: {}'.format(chars))

def count_words(essay):
    essay = essay.strip()
    lines = [x.strip().split() for x in essay.split('\n')]
    words = []
    for line in lines:
        words += line

    print('Word Count: {}'.format(len(words)))
    print('Number of Unique words: {}'.format(len(set(words))))

def main():
    background_and_goals()
    statement_of_purpose()



if __name__ == '__main__':
    main()
