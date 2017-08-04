#!/usr/bin/env python
# -*- coding: ascii -*-
# Filename: cryptoSetTwo.py
"""Crypto challenge set #2. https://cryptopals.com/sets/1/challenges/2
Fixed XOR:
Write a function that takes two equal-length
buffers and produces their XOR combination.
If your function works properly,
then when you feed it the string:
1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965
... should produce:
746865206b696420646f6e277420706c6179"""
import sys
sys.path.append('./Cryptopals')
import workHub as whub
from Crypto.Util.strxor import strxor


__author__ = "John Knowles"

hexStr = "1c0111001f010100061a024b53535009181c"
xorStr = "686974207468652062756c6c277320657965"
result = "746865206b696420646f6e277420706c6179"

s = whub.unhexlify(hexStr)
t = whub.unhexlify(xorStr)
u = whub.unhexlify(result)

print (s, t, u)
xorResult = strxor(s, t)
print xorResult
if u != xorResult:
    raise Exception("Unexpected results.")
