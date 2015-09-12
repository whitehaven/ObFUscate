#!/usr/bin/env python
# (Supposedly allows execution without python keyword)

__author__ = "whitehaven"

import sys
import argparse
from random import randint


# function to convert chars to TF values to garble chars (8 bit, [0-255] range)
def str2garble(subject):
    garbled = []  # will be list of lists of a-m|n-z
    for element in subject:

        binarray = []

        while element:
            if element & 1 == 1:
                binarray.append(1)
            else:
                binarray.append(0)
            element >>= 1
        if len(binarray) < 8:
            for leftover in range(len(binarray), 8):
                binarray.append(0)
        binarray.reverse()

        garbledlist = []

        for element in binarray:
            if element == 1:
                garbledlist.append(randint(110, 122))  # note these are 'n' and 'z' (ord() has overhead)
            else:  # if element == 0
                garbledlist.append(randint(97, 109))  # 'a' and 'm'

        garbled.append(garbledlist)

    return garbled


# main encryption process:
def encryptMode():
    garblednumerals = str2garble(bytearray(args.infile.read(), 'utf-8'))
    for element in garblednumerals:
        for subelement in element:
            args.outfile.write(chr(subelement))
    quit(0)


# main decryption process:
def decryptMode():
    print("decrypt fail")
    quit(0)


# parser:
parser = argparse.ArgumentParser(description='WHI Obfuscation Cipher v1.0')
parser.add_argument('--version', action='version', version='ObFUscate v1.0 | 11 Sept 2015')

subparsers = parser.add_subparsers(dest='mode')

parser_encrypt = subparsers.add_parser('encrypt', help='execute (forward) operation')
parser_encrypt.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                            help='(default to stdin)')
parser_encrypt.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                            help='(default to stdin)')

parser_decrypt = subparsers.add_parser('decrypt', help='execute (backward) operation')
parser_decrypt.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                            help='(default to stdin)')
parser_decrypt.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                            help='(default to stdin)')

args = parser.parse_args()

# entry point

if args.mode == 'encrypt':
    encryptMode()
else:  # if args.mode == 'decrypt'
    decryptMode()
