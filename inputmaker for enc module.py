import random

fileToFill = open("gen-enc-input.txt", "w")

for time in range(0, int(1E6)):
    fileToFill.write(chr(random.randint(ord('A'), ord('z'))))
