# 가장 큰 소인수 구하기

n = 600851475143
result = []
for i in range(2,n):
    if n % i == 0:
        result.append(i)
        n /= i
        if n % i == 1:
            break

print(result)