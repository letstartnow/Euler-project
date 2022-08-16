# 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수

import math

LCM = 1

for i in range(1, 21):
    GCD = math.gcd(i,LCM)
    LCM = int(i*LCM/GCD)
    print(i, LCM)


num = 1

while num > 0:
    for n in range(1,21):
        if num % n != 0:
            num += 1
            break
    else:
        print(num)
        num = 0