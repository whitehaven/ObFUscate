#!/usr/bin/env python
# (Supposedly allows execution without python keyword)

__author__ = "whitehaven"

from sys import stdin
import argparse

BLOCK_SIZE = 8

def binlist(char):
    result = []
    while char:
        if char & 1 == 1:
            result.append(1)
        else:
            result.append(0)
        char >>= 1
    if len(result) < 8:
        for leftover in range(len(result),8):
            result.append(0)
    result.reverse()
    return result # must be size 8

# function to convert chars to TF values to garble chars (8 bit, [0-255] range)
# receives strings
def str2garble( subject ):
    results = []
    for element in subject:
        print(binlist(element))
        results.append(binlist(element))



# function to convert garble chars to TF values into chars
# receives strings of garble

encryptThis = bytearray("Shiz monkeys", 'utf-8')

str2garble(encryptThis)

# argparse these options
#	-h help
#	-i inline
# ?	-s? standard input
#	-d decrypt mode

# take -o= for file output
# otherwise, std input

# > > encryption:
# break down to chars
# 	convert to binaryish arrays
#	encrypt
# 	output

# > > decryption:
# read in 8-byte bits
#	decrypt
# 	convert to char
# 	output
