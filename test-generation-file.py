#                           जय श्री राम


import sys; import math; from collections import *; import random
# sys.setrecursionlimit(10**6)
sys.stdout = open("input.txt","w")

def get_ints(): return map(int, input().split())
def get_list(): return list(get_ints())
def printspx(*args): return print(*args, end="")
def printsp(*args): return print(*args, end=" ")

CAPS_ALPHABETS = {chr(i+ord('A')) : i for i in range(26)}
SMOL_ALPHABETS = {i : chr(i+ord('a')) for i in range(26)}
UGLYMOD = int(1e9+7); SEXYMOD = 998244353; MAXN = int(1e5)


n = random.randint(1, int(1e5))
print(n)
# s = '()'
li = [i+1 for i in range(n)]
random.shuffle(li)
print(*li)
random.shuffle(li)
print(*li)
# for i in range(n):
#     sz = random.randint(1, int(1e4))
#     print(sz)
    # for j in range(sz):
    #     printspx(s[random.randint(0, 1)])
    # print()
    # sz = random.randint(1, 5)
    # # printsp(sz)
    # for i in range(sz):
    #     printspx(SMOL_ALPHABETS[random.randint(0, 1)])
    # printsp()
    # # print(random.randint(1, 10), random.randint(1, 10))

'''

g++ -std=c++17 bits/stdc++.h

'''