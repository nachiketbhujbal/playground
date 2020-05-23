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
    I graduated with a Bachelor of Science in Engineering Physics in 2018 from
    the University of Illinois at Urbana-Champaign. My specialization was in
    Computational Physics, with a minor in Computer Science. My cumulative GPA
    by graduation was 3.01/4.0.

    During my undergraduate career, I worked as a data analyst on a two-man
    team in a soybean genetics lab on campus. I created a program for analyzing
    gene sequences taken from real soybene samples and pattern-matched them
    against a university database. I also wrote a GUI-based application wrapper
    around this program for my PI and the other RAs in our lab to use easily.

    After graduation, I accepted a 1-year internship at RBC Capital Markets,
    where I worked full time as a quant developer on the central risk trading
    desk. I wrote software to analyze enormous sets of financial markets data
    and built a full-stack trading platform that is now used across the company
    by  more than 100 traders in the US, Canada, and London.

    During my internship, I worked on a project to speed up our automated
    trading algorithms and execute orders more effeciently. By then, I was fully
    engrossed in all aspects of computer science, from software engineering, to
    algorithmic complexity and computational theory.

    By the end of the internship, I had greatly sharpened my math and critical
    thinking skills. I had also become proficient at Python, C++, JavaScript,
    SQL, and various other programming languages. I learned more linear algebra,
    statistics, and differential equations in that year, than I could have ever
    absorbed from undergraduate courses, since I would frequently apply concepts
    as soon as I learned them on huge sets of stochastic market data.

    I was hired full time with RBC in 2019, after that year long internship.
    Now I work on algorithmic strategy development and am also helping to build
    the developer API, which provides a framework for others within the firm to
    offer custom cross-asset strategies for their clients.
    """
    )
    print('background_and_goals:')
    count_words(essay)
    count_chars(essay)

def statement_of_purpose():
    essay = (
    """
    """
    )
    print('statement_of_purpose:')
    count_words(essay)
    count_chars(essay)

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
    print()
    background_and_goals()
    print()
    statement_of_purpose()



if __name__ == '__main__':
    main()
