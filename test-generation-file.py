#                           जय श्री राम


import sys; import math; from collections import *; import random
# sys.setrecursionlimit(10**6)
sys.stdout = open("input.txt","w")

def get_ints(): return map(int, input().split())
def get_list(): return list(get_ints())
def printspx(*args): return print(*args, end="")
def printsp(*args): return print(*args, end=" ")

UGLYMOD = int(1e9+7); SEXYMOD = 998244353; MAXN = int(1e5)


n = random.randint(10, 40)
print(n)
for i in range(n):
    print(random.randint(1, 10), random.randint(1, 10))