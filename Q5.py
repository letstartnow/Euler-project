#1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# result = 1
# for i in range(20,0,-1):
#     if 
    
# 1 3 6 7 8 11 13 15 16 17 19
# 20
# 1 2 3 22 5 23 7 222 33 25 11 223 13 27 35 2222 17 233 19 225



# result = []
# pre = []
# for N in range(10,0,-1):
#     d = 2
#     while N != 1:
#         if N % d != 0:
#             d += 1
#         else:
#             N //= d
#             pre.append(d)
#     for i in pre:
#         if result.count(i) > pre.count(i):
#             pass
#         else:
#             result.append(d)
#     for a in pre:
#         result *= a
        
# print(result)


result=[]
for N in range(10,0,-1):
    d=2
    while N != 1:
        if N % d != 0:
            N