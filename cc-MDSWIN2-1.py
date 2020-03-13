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
def checkIfMagicEvenWillYield(magicNums):
    fightingLength = 0
    for i in range(2, max(magicNums)):
        if i not in magicNums:
            fightingLength = i
            break
    if fightingLength != 0:
        return True
    else:
        return False
# ##########################################################
def nCr(n, r): 
    return (fact(n) // (fact(r) * fact(n - r))) % 998244353

def fact(n): 
    res = 1
    for i in range(2, n+1): 
        res = res * i 
    return res 
# ##########################################################
for _testcases_ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    for _query_ in range(int(input())):
        d = {};  countNumbers = {}
        l, r = map(int, input().split())
        for i in range(l-1, r):
            try:
                d[li[i]] += 1
            except:
                d[li[i]] = 1
        for k, v in d.items():
            try:
                countNumbers[v] += 1
            except:
                countNumbers[v] = 1
        # print(countNumbers)
        multiCountNums = []; singleCount = 0; magicNums = [];
        ans = 0
        for k, v in countNumbers.items():
            if k == 1:
                singleCount = v
            else:
                multiCountNums.append(k)
                if v%2==1:
                    magicNums.append(k)
        # print(multiCountNums, singleCount, magicNums)
        # #############################################################3333
        magicNumsLength = len(magicNums)
        if magicNumsLength%2 == 0:
            if magicNumsLength == 0:
                if singleCount%2 == 0:
                    ans = 0
                else:
                    ans = singleCount
            else:
                if singleCount%2 == 0:
                    if checkIfMagicEvenWillYield(magicNums) == False:
                        ans = singleCount
                    magicNums.sort(reverse = True)
                    for i in range(magicNumsLength):
                        choi = 0
                        for j in range(i+1, magicNumsLength):
                            choi += nCr(magicNums[i], magicNums[j])
                        ans += countNumbers[magicNums[i]] * choi
                else:
                    fightingLength = 0
                    for i in range(2, max(magicNums)):
                        if i not in magicNums:
                            fightingLength = i
                            break
                    if fightingLength != 0:
                        mx = max(magicNums)
                        ans += countNumbers[mx] * nCr(mx, fightingLength)
                    else:
                        ans = 0
        else:
            if magicNumsLength == 1:
                if singleCount%2 == 0:
                    for i in magicNums:
                        ans += countNumbers[i]
                else:
                    for i in magicNums:
                        ans += (countNumbers[i] * i)
            else:
                if singleCount%2 == 0:
                    for i in magicNums:
                        magicNumsCpy = magicNums.copy()
                        magicNumsCpy.remove(i)
                        if checkIfMagicEvenWillYield(magicNumsCpy) == False:
                            ans += (countNumbers[i] * i)
                else:
                    for i in magicNums:
                        magicNumsCpy = magicNums.copy()
                        magicNumsCpy.remove(i)
                        if checkIfMagicEvenWillYield(magicNumsCpy) == False:
                            ans += countNumbers[i]
                    else:
                        ans = 0
        print(ans % 998244353)