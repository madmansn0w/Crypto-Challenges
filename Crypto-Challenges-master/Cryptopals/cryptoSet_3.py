#!/usr/bin/env python
# -*- coding: ascii -*-
# Filename: cryptoSet.py
"""Crypto challenge set #3. https://cryptopals.com/sets/1/challenges/2
Single-byte XOR cipher:
The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character.
Find the key, decrypt the message.
You can do this by hand. But don't: write code to do it for you.
How? Devise some method for "scoring" a piece of English plaintext.
Character frequency is a good metric. Evaluate each output
and choose the one with the best score."""

import sys
import binascii
sys.path.append('./Cryptopals')
from Crypto.Util.strxor import strxor_c
import itertools
import random
from nltk.corpus import words as nltk_words  # Module to match English words
from __future__ import division

__author__ = "John Knowles"


def freqCount(tokens):
    '''Character Counter'''
    freq = {}
    for word in tokens:
        for letter in word:
            if letter not in freq:
                freq[letter] = 1
            else:
                freq[letter] += 1
    alphaSort = sorted(freq, key=freq.__getitem__, reverse=True)
    alphaSort = [x for x in alphaSort if x.isalpha() or x.isspace()]
    n = sum([freq[letter] for letter in alphaSort])
    with open("Cryptopals\crime_and_p_letter_freq.txt", 'w') as file:
        for letter in alphaSort:
            file.write(letter + '; ' + str(freq[letter]) + '; '
                       + "{:.6f}%".format(freq[letter] / n * 100) + '\n')
    # print(letter + ': ' + str(freq[letter]) + ', '
    #       + "{:.6f}%".format(freq[letter] / n * 100))
    return alphaSort


def decryptByCharFreq(s, tokens):
    '''Pit the highest-to-lowest frequency characters against
    the encoded string until it makes sense.'''
    d = {}
    with open("Cryptopals\crime_and_p_letter_freq.txt", 'r') as f:
        for line in f:
            parts = line.replace('%', '').rstrip().split('; ')
            key = parts[0]
            freq = parts[-1]
            d[key] = freq
    xorResult = max([(l, strxor_c(s, ord(l)))
                    for token in tokens for l in token],
                    key=lambda x: scoring(x[1], d))
    return xorResult


def scoring(arg, d):
    counter = 0
    for i in arg:
        # print i
        if i.isalpha() and i in d:
            char = i.lower()
            if i in d:
                # print "i", i
                counter += float(d[char])
    dCheck = arg.split()
    word = dCheck[-1]
    # wordC = dict.fromkeys(nltk_words.words(), None)
    if word in nltk_words.words():
        print word
        counter += 50
    return counter


if __name__ == '__main__':
    enc = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    # with open(sys.argv[1], 'r') as file:
    #     contents = file.read()
    with open('Cryptopals\crime_and_punishment.txt', 'r') as f:
        contents = [line for line in f]
    alphaSort = freqCount(contents)
    unhexlified = binascii.unhexlify(enc)
    print(decryptByCharFreq(unhexlified, alphaSort))
