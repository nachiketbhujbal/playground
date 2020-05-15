#!/usr/local/bin/python3
'''
date: 2020-03-05
author: Nachiket Bhujbal
General set of tools which may have shared use between projects

'''
import sys
import time

def custominput(valuetype='value'):
    vowels = [valuetype.startswith(x) for x in ['a', 'e', 'i', 'o', 'u']]
    starts_with_vowel = any(vowels)
    fillvalue = 'a {} for'.format(valuetype)
    if starts_with_vowel:
        fillvalue = 'an {} for'.format(valuetype)

    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    else:
        N = int(input('Enter {} N = '.format(fillvalue)).strip())

    return N

def customoutput(solution_title, N, R, t=0.0):
    t = time.time() - t
    T = round(1000000 * t, 3)
    print('{} solution for N = {} -> {}'.format(solution_title, N, R))
    print('\t-- Solved in {} us'.format(T))
