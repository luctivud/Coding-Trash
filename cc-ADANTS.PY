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
points = 0
oddOdd = []; evenOdd = []; oddEven = []; evenEven = [];
for _points_ in range(int(input())):
    li = list(map(int, input().split()))
    li.append(_points_+1)
    if li[0]%2 and li[1]%2:
        oddOdd.append(li)
    elif li[0]%2 == 0 and li[1]%2 == 1:
        evenOdd.append(li)
    elif li[0]%2 == 0 and li[1]%2 == 0:
        evenEven.append(li)
    else:
        oddEven.append(li)
    points += 1
while(points!=1):
    i = 0; j = 0;
    while(i < len(oddOdd) or j < len(evenOdd)):
        