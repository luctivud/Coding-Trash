'''     ##     ##  #######  # #  ######
        ##     ##  ##   ##  ###    ##
        ##     ##  ##    #  # #    ##
        #########  #######  # #    ##    '''

import sys
import math
# sys.setrecursionlimit(10**6)

def get_ints(): return map(int, input().strip().split())
def get_list(): return list(get_ints())

def printspx(*args): return print(*args, end="")
def printsp(*args): return print(*args, end=" ")
def printchk(*args): return print(*args, end=" \ ")

MODPRIME = int(1e9+7); BABYMODPR = 998244353;

ONLINE_JUDGE = 1
if not ONLINE_JUDGE:
    sys.stdin = open("input.txt","r")  # <<<  Comment this line  >>> #
    sys.stdout = open("output.txt","w")  # <<<  Comment this line  >>> #
    sys.stderr = open("output.txt","w")  # <<<  Comment this line  >>> #

# for _testcases_ in range(int(input())):
import bisect
n, l = get_ints()
li = []
for i in range(n):
    s = input()
    bisect.insort(li, s)
print("".join(li))
'''
>>> COMMENT THE STDIN!! CHANGE ONLINE JUDGE !!
THE LOGIC AND APPROACH IS BY ME @luctivud ( UDIT GUPTA )
SOME PARTS OF THE CODE HAS BEEN TAKEN FROM WEBSITES LIKE::
(I Own the code if no link is provided here or I may have missed mentioning it)
DO NOT PLAGIARISE.
TESTCASES:
>>> COMMENT THE STDIN!! CHANGE ONLINE JUDGE !!
'''