#                           जय श्री राम

import sys; import math; from collections import *
# sys.setrecursionlimit(10**6)

def get_ints(): return map(int, input().split())
def get_list(): return list(get_ints())
def printspx(*args): return print(*args, end="")
def printsp(*args): return print(*args, end=" ")

UGLYMOD = int(1e9+7); SEXYMOD = 998244353; MAXN = int(1e5)

# sys.stdin  = open("input.txt","r"); sys.stdout = open("output.txt","w")

n = int(input())
li = get_list()
prefix = [0]
c = 0
for i in li:
    c += i
    prefix.append(c)
li.sort()
minprefix = [0]
c= 0
for i in li:
    c += i
    minprefix.append(c)
for _testcases_ in range(int(input())):
    t, l, r = get_ints()
    if t == 1:
        print(prefix[r] - prefix[l-1])
    else:
        print(minprefix[r] - minprefix[l-1])




'''
>>> COMMENT THE STDIN!! CHANGE ONLINE JUDGE !!
THE LOGIC AND APPROACH IS MINE @luctivud ( UDIT GUPTA )
Link may be copy-pasted here if it's taken from other source.
DO NOT PLAGIARISE.
>>> COMMENT THE STDIN!! CHANGE ONLINE JUDGE !!
'''