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
import itertools
for __ in range(int(input())):
    n, k = map(int, input().split())
    d = {}
    for i in range(1,n+1):
        for j in range (1,n+1):
            if j!=i:
                try:
                    d[i].add(j)
                except:
                    d[i] = set()
                    d[i].add(j)
    # print(d)
    for ki in range(k):
        li = list(map(int, input().split()))
        for i in range (n):
            for j in range(i):
                try:
                    d[li[i]].remove(li[j])
                except:
                    pass
    permutli = [ [] for x in range(n) ]
    for key, val in d.items():
        if len(val) >= 1:
            for i in d[key]:
                permutli[key-1].append(i)
        else:
            permutli[key-1].append(0)
    # print(permutli)
    
    allpermutations = list(itertools.product(*permutli))
    count = n+2;    ansli = [];
    for perm in allpermutations:
        se = set()
        for i in perm:
            se.add(i)
        sz = 0
        for num in range(1, n+1):
            if num not in se:
                sz+=1
        if sz < count:
            count = sz
            ansli = list(perm).copy()
    print(count)
    for ele in ansli:
        print(ele, end = " ")
    print()