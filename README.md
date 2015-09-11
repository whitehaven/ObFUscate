# ObFUscate
Simple obfuscatory cipher

This is the idea:

This is primarily a learning exercise on argparse, but will theoretically be a decent form of encryption against the unaware.

The algorithm is this:
char -> binary byte list -> randomly choose a-m if 0, n-z if 1 -> garble
'c' -> [ 0|1 * 8 ] -> [ a-m if 0, n-z if 1 * 8 ] -> garbled message text (8 letters per char)

Example:
'S' -> [0, 1, 0, 1, 0, 0, 1, 1] -> [a, n, b, o, c, d, p, q] -> anbocdpdq
'SSSSSS' -> anbocdpdqanbocdpdqanbocdpdqanbocdpdqanbocdpdqanbocdpdq (except random - see why that's hard to get?)