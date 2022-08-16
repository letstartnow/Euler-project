#Q2.py

# def fib(n):
#    if n == 0:
#       return 1
#    if n == 1:
#       return 2
#    return fib(n-2) + fib(n-1)

# fibbo = [fib(x) for x in range(32)]
# 
# result = 0
# for i in fibbo:
#    if i % 2 == 0:
#       result += i
    
# print(result)

a = 1
b = 1
c = a + b
result = 0

while c < 4000000:
    if c % 2 == 0:
        result += c
    a = b
    b = c
    c = a + b

print(result)