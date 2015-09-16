# ObFUscate
Simple obfuscatory cipher

Proof of bi-directionality:
	|-> diff --brief gen-enc-input.txt gen-dec-output.txt 
	Files gen-enc-input.txt and gen-dec-output.txt differ

	|-> time python3 ObFUscate.py encrypt gen-enc-input.txt gen-enc-output.txt

	real	0m9.068s
	user	0m8.832s
	sys	0m0.146s

	|-> time python3 ObFUscate.py decrypt gen-enc-output.txt gen-dec-output.txt

	real	0m3.266s
	user	0m3.228s
	sys	0m0.030s

	|-> diff --brief gen-enc-input.txt gen-dec-output.txt 


This is the idea:

This is primarily a learning exercise on argparse, but will theoretically be a decent form of encryption against the unaware.

The algorithm is this:
char -> binary byte list -> randomly choose a-m if 0, n-z if 1 -> garble
'c' -> [ 0|1 * 8 ] -> [ a-m if 0, n-z if 1 * 8 ] -> garbled message text (8 letters per char)

Example:
'S' -> [0, 1, 0, 1, 0, 0, 1, 1] -> [a, n, b, o, c, d, p, q] -> anbocdpdq
'SSSSSS' -> anbocdpdqanbocdpdqanbocdpdqanbocdpdqanbocdpdqanbocdpdq (except random - see why that's hard to get?)