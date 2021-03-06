#!/usr/bin/env python
# (Supposedly allows execution without python keyword)

__author__ = "whitehaven"

import sys
import argparse
from random import shuffle
from array import array

ALPHABET_LENGTH = 26
HALF_ALPHABET_LENGTH = int(ALPHABET_LENGTH / 2)
BLOCK_LENGTH = 8

# pre-generate random list of chars to avoid using randint(), which is face-meltingly slow
AtoM = array('b', (range(ord('a'), ord('n'))))  # a-m
NtoZ = array('b', (range(ord('n'), ord('z') + 1)))  # n-z

shuffle(AtoM)
shuffle(NtoZ)


# function to convert chars to TF values to garble chars (8 bit, [0-255] range)
def str2garble(subject):
    garbled = []
    index_premade_random_letters = 0
    for element in subject:

        garbledlist = []

        while element:
            if element & 1 == 1:
                garbledlist.append(NtoZ[index_premade_random_letters])
            else:
                garbledlist.append(AtoM[index_premade_random_letters])
            element >>= 1

            index_premade_random_letters = (index_premade_random_letters + 1) % HALF_ALPHABET_LENGTH

        if len(garbledlist) < BLOCK_LENGTH:  # if not 8, fill the rest with 0s
            for leftover in range(len(garbledlist), BLOCK_LENGTH):
                garbledlist.append(AtoM[index_premade_random_letters])

        garbledlist.reverse()

        garbled.append(garbledlist)

    return garbled


def garble2str(garbled_input):
    translated_list = []
    for char_block in range(0, len(garbled_input), BLOCK_LENGTH):
        char_total = 0
        for char_of_8 in range(0 + char_block, BLOCK_LENGTH + char_block):
            if garbled_input[char_of_8] >= 'n':  # if should be 1
                char_total |= (0b1 << ((BLOCK_LENGTH - char_of_8 - 1) % BLOCK_LENGTH))
        translated_list.append(chr(char_total))

    translated_string = ''.join(translated_list)

    return translated_string


# main encryption process:
def encryptMode():
    garblednumerals = str2garble(bytearray(args.infile.read(), 'utf-8'))
    for element in garblednumerals:
        for subelement in element:
            args.outfile.write(chr(subelement))
    quit(0)


# main decryption process:
def decryptMode():
    string_output = garble2str(args.infile.read())
    args.outfile.write(string_output)

    quit(0)


# parser:
parser = argparse.ArgumentParser(description='WHI Obfuscation Cipher v1.0')
parser.add_argument('--version', action='version', version='ObFUscate v1.0 | 11 Sept 2015')

subparsers = parser.add_subparsers(dest='mode')

parser_encrypt = subparsers.add_parser('encrypt', help='execute encryption (forward operation)')
parser_encrypt.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                            help='(default to stdin)')
parser_encrypt.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                            help='(default to stdin)')

parser_decrypt = subparsers.add_parser('decrypt', help='execute decryption (backward operation)')
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
