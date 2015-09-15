import random

fileToFill = open("gen-dec-input.txt", "w")

for time in range(0, int(8E6)):
    fileToFill.write(chr(random.randint(ord('a'), ord('z'))))
