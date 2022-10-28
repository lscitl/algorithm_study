import sys

a = int(sys.stdin.readline())

for i in range(a):
    print(" " * i + "*" * (2 * (a - (i + 1)) + 1))
