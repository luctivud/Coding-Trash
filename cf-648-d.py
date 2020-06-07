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


# sys.stdin = open("input.txt","r")  # <<<  Comment this line  >>> #
for _testcases_ in range(int(input())):
    n, m = get_ints()
    matr = []
    for i in range(n):
        li = list(input())
        matr.append(li)
    flag = True; flagGood = False
    for i in range(n):
        for j in range(m):
            if matr[i][j] == 'B':
                if j + 1 < m:
                    if matr[i][j+1] == 'G':
                        flag = False
                if j-1 >= 0:
                    if matr[i][j-1] == 'G':
                        flag = False
                if i + 1 < n:
                    if matr[i+1][j] == 'G':
                        flag = False
                if i - 1 >= 0:
                    if matr[i-1][j] == 'G':
                        flag = False
            elif matr[i][j] == 'G':
                flagGood = True

    flag1 = flag2 = True
    if n-2 >= 0 and m-1 >=0:
        if flagGood and matr[n-2][m-1] == 'B':
            flag = False
    if n-1 >=0  and m-2 >=0:
        if flagGood and matr[n-1][m-2] == 'B':
            flag = False
    if n-2 >= 0 and m-1 >=0:
        if flagGood and matr[n-2][m-1] == '#':
            flag1 = False
    if n-1 >=0  and m-2 >=0:
        if flagGood and matr[n-1][m-2] == '#':
            flag2 = False
    if flag1 and flag2 == False:
        flag = False
    
    if flag :
        print("Yes")
    else:
        print("No")
    


'''
THE LOGIC AND APPROACH IS BY ME @luctivud ( UDIT GUPTA )
SOME PARTS OF THE CODE HAS BEEN TAKEN FROM WEBSITES LIKE::
(I Own the code if no link is provided here or I may have missed mentioning it)
>>> DO NOT PLAGIARISE.
TESTCASES:
>>> COMMENT THE STDIN !!
'''