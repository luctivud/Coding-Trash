#                          JAI SHREE RAM

import math; from collections import *
import sys; from functools import reduce

def get_ints(): return map(int, input().strip().split())
def get_list(): return list(get_ints())
def getlistofstring(): return list(input().strip().split())
def printxsp(*args): return print(*args, end="")
def printsp(*args): return print(*args, end=" ")

UGLYMOD = int(1e9)+7; SEXYMOD = 998244353; MAXN = int(1e5)

# sys.setrecursionlimit(10**6)
# sys.stdin=open("input.txt","r");sys.stdout=open("output.txt","w")

for _testcases_ in range(int(input())):
    n = int(input())
    ans = [0, 0, 0]
    for i in range(n):
        moves = getlistofstring()
        used = set(moves)
        if len(used) == 2:
            used = list(used)
            if (used[0] == 'R' and used[1] == 'P') or (used[0] == 'P' and used[1] == 'R'):
                factor = 0
                for i in range(3):
                    if moves[i] == 'R': factor += 1
                for i in range(3):
                    if moves[i] == 'R': ans[i] -= (3-factor)
                    else: ans[i] += factor
            elif (used[0] == 'P' and used[1] == 'S') or (used[0] == 'S' and used[1] == 'P'):
                factor = 0
                for i in range(3):
                    if moves[i] == 'P': factor += 1
                for i in range(3):
                    if moves[i] == 'P': ans[i] -= (3-factor)
                    else: ans[i] += factor
            elif (used[0] == 'R' and used[1] == 'S') or (used[0] == 'S' and used[1] == 'R'):
                factor = 0
                for i in range(3):
                    if moves[i] == 'S': factor += 1
                for i in range(3):
                    if moves[i] == 'S': ans[i] -= (3-factor)
                    else: ans[i] += factor
    print(*ans)

'''
>>> COMMENT THE STDIN!! CHANGE ONLINE JUDGE !!
THE LOGIC AND APPROACH IS MINE @luctivud ( UDIT GUPTA )
Link may be copy-pasted here if it's taken from other source.
DO NOT PLAGIARISE.
>>> COMMENT THE STDIN!! CHANGE ONLINE JUDGE !!
'''