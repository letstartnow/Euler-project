# 곱해서 대칭수 만들기

# 일단 대칭수들을 표현하는 것 부터가 우선일듯
# 10000 <= x <= 999*999

numbers = []
for i in range(100,999):
    for m in range(100,999):
        number = str(i*m)
        if len(number) == 6:
            if number[0] == number[5] and number[1] == number[4] and number[2] == number[3]:
                numbers.append(number)
                A = max(numbers)

print(A)