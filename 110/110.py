import sys
import random


def permutations(a, n):

    if n == len(a):
        print(''.join(a))
        return
    permutations(a, n + 1)
    for i in range(n + 1, len(a)):
        a[n], a[i] = a[i], a[n]
        permutations(a, n + 1)
        a[n], a[i] = a[i], a[n]


if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required\n')
    sys.exit(1)

word = sys.argv[1]
permutations(list(word), 0)


