# 1부터 100까지 "제곱의 합"과 "합의 제곱"의 차

plus = 0
square = 0
for i in range(1,101):
    plus += i**2
    square += i

result = square**2 - plus
print(result)