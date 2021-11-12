# 10824번

import sys

date = list(sys.stdin.readline().split())
num1 = 0
num2 = 0

for n in date[0]:
    num1 *= 10
    num1 += ord(n) - ord('0')

for n in date[1]:
    num1 *= 10
    num1 += ord(n) - ord('0')

for n in date[2]:
    num2 *= 10
    num2 += ord(n) - ord('0')

for n in date[3]:
    num2 *= 10
    num2 += ord(n) - ord('0')

print(num1 + num2)
