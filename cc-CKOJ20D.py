'''     J A I ~ S H R E E ~ R A M     '''

# Title: cc-CKOJ20D.py
# created on: 20-07-2020 at 20:46:04
# Creator & Template : Udit Gupta "@luctivud"
# https://github.com/luctivud
# https://www.linkedin.com/in/udit-gupta-1b7863135/


import math; from collections import *
import sys; from functools import reduce
from itertools import groupby

# sys.setrecursionlimit(10**6)

def get_ints(): return map(int, input().strip().split())
def get_list(): return list(get_ints())
def get_string(): return list(input().strip().split())
def printxsp(*args): return print(*args, end="")
def printsp(*args): return print(*args, end=" ")


DIRECTIONS = [[0, 1], [0, -1], [1, 0], [1, -1]] #up, down, right, left
NEIGHBOURS = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i!=0 or j!=0)]


OrdUnicode_a = ord('a'); OrdUnicode_A = ord('A')
CAPS_ALPHABETS = {chr(i+OrdUnicode_A) : i for i in range(26)}
SMOL_ALPHABETS = {chr(i+OrdUnicode_a) : i for i in range(26)}


MOD_JOHAN = int(1e9)+7; MOD_LIGHT = 998244353; INFINITY = float('inf')
MAXN_EYEPATCH = int(1e5)+1; MAXN_FULLMETAL = 501

# Custom input output is now piped through terminal commands.

def bfs(s):
    queue = deque()
    visited = set()
    visited.add(1)
    queue.append((1, 0))
    while len(queue):
        node, dep = queue.popleft()
        dep += 1
        for zen in tree[node]:
            if zen not in visited:
                visited.add(zen)
                if dep & 1:
                    global xorsum
                    xorsum ^= li[zen]
                queue.append((zen, dep))
        # print(queue)
        


# for _testcases_ in range(int(input())): 
n = int(input())
li = [0] + get_list()
tree = defaultdict(list)
for _  in range(n-1):
    a, b = get_ints()
    tree[a].append(b)
    tree[b].append(a)
xorsum = 0
bfs(1)
# print(xorsum)
print("First" if xorsum else "Second")




'''
THE LOGIC AND APPROACH IS MINE ( UDIT GUPTA )
Link may be copy-pasted here, otherwise.
'''
