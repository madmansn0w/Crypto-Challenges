#!/usr/bin/env python
# -*- coding: ascii -*-
# Filename: cryptoSetOne.py

"""Crypto challenge set #1. https://cryptopals.com/sets/1/challenges/1
Convert hex to base64:
The string:
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Should produce:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
*Always operate on raw bytes, never on encoded strings.
 Only use hex and base64 for pretty-printing.*
"""

import base64  # Conversion package
from binascii import unhexlify  # Operate on raw bytes, not encoded strings.

__author__ = "John Knowles"

hexString = ("49276d206b696c6c696e6720796f757220627261696e"
             "206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
result = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

# encode -> bytes ; decode -> string
encoded = hexString.decode("hex").encode("base64")
print (encoded, result, '\n', len(encoded), len(result), '\n',
       encoded.decode("base64") == result.decode("base64"), '\n',
       encoded.decode("base64"))

# Oh, wow. Hahaha. Good one, Cryptopals.
# Too easy, however; let's try doing it with other methods.
hexString[0:2]
hexString[0::2]
hexString[1::2]
# tuples
byteForm = [''.join(x) for x in zip(hexString[0::2], hexString[1::2])]
print byteForm
decimalForm = ([int(''.join(x), 16) for x in
                zip(hexString[0::2], hexString[1::2])])
print decimalForm
charForm = ([chr(int(''.join(x), 16)) for x in
            zip(hexString[0::2], hexString[1::2])])
print ''.join(charForm)


def hexToBase64(s):
    '''hexToBase64 Conversion'''
    byteSeq = unhexlify(s)
    return base64.b64decode(byteSeq)


unhexlified = hexToBase64(hexString)
unhexlified
print unhexlified
