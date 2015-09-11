#!/usr/bin/env python
# (Supposedly allows execution without python keyword)

__author__ = "whitehaven"

from sys import stdin
import argparse
from random import randint

BLOCK_SIZE = 8

parser = argparse.ArgumentParser()
parser.add_argument("TARGET", type=str, help="encryption target")
args = parser.parse_args()


def garblist(blist):
    garbledlist = []
    for element in blist:
        if element == 1:
            garbledlist.append(randint(ord('n'), ord('z')))
        else:  # if element == 0
            garbledlist.append(randint(ord('a'), ord('m')))
    return garbledlist


# this function is separate because it is useful elsewhere
def binlist(char):  # returns list of 1|0
    result = []
    while char:
        if char & 1 == 1:
            result.append(1)
        else:
            result.append(0)
        char >>= 1
    if len(result) < 8:
        for leftover in range(len(result), 8):
            result.append(0)
    result.reverse()
    return result  # will be size 8


# function to convert chars to TF values to garble chars (8 bit, [0-255] range)
# receives strings
def str2garble(subject):
    results = []  # will be list of lists of 1|0
    garbled = []  # will be list of lists of a-m|n-z
    for element in subject:
        results.append(binlist(element))
    # now, results has list of lists of the string passed in (0 and 1s)
    for element in results:
        garbled.append(garblist(element))

    return garbled


# encryptThis = bytearray(input("Encryption Target: "), 'utf-8')


garbledNumerals = str2garble(bytearray(args.TARGET, 'utf-8'))

for element in garbledNumerals:
    for subelement in element:
        print("%c" % (subelement), end="")



# argparse these options
#	-h help
#	-i inline
# ?	-s? standard input
#	-d decrypt mode

# take -o= for file output
# otherwise, std input





# function to convert garble chars to TF values into chars
# receives strings of garble
