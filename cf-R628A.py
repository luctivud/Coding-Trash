#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Udit Gupta @luctivud  神 | LIGHT | GREED | CIPHER | XAYN
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                ##     ##   ######   # #  ######
                ##     ##   ##  ##   ###    ##
                ##     ##   ##   #   # #    ##
                ###### ##   ######   # #    ##
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   | WORSHIPPER OF GREED | 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import math
for _testcases_ in range(int(input())):
    n = int(input())
    for i in range(1, (n//2)+1):
        a = i
        b = n-i
        if math.gcd(a,b) + ((a*b)//math.gcd(a,b)) == n:
            print(a,b)
            break