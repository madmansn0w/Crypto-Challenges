#!/usr/bin/env python
# -*- coding: ascii -*-
# Filename: workHub.py

"""Crypto challenge function library."""

# import base64  # Conversion package
from binascii import unhexlify
# from Crypto.Util.strxor import strxor
# strxor(...)
# strxor(a:str, b:str) -> str
# Return a XOR b. Both a and b must have the same length.
__author__ = "John Knowles"


def is_hex(*args):
    for a in str.args:
        try:
            int(a, 16)
            return True
        except ValueError:
            return False


def unhexlified(*args):
    '''Python's unhexlify: hexadecimal conversion'''
    seq = [unhexlify(args)]
    return seq


def unhexToBase64Hack(*args):
    '''Hex to Base 64 "Hack." Python's terminology in v2.7 differs from v3+.
    Hex is still encoded in the mathematical sense, but Python's terminology
    is backwards and confusing. This function is for a quick-view look of the
    result.'''
    base64Seq = []
    for a in args:
        base64Seq += a.decode("hex").encode("base64")
    return base64Seq


def hexDecodeHack(arg):
    '''Hex decoding hack. See hexToBase64Hack explanation.'''
    strSeq = arg.decode("hex")
    return strSeq


def detXOR(*args):
    '''XOR two or more strings.
    Exclusive Or yields true for differing values.'''
    aln = [''.join(x) for x in zip(args[0], args[1])]
    return aln
