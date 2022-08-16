# a + b + c = 1000 이 되는 피타고라스 수

result = 1
l = range(1,1000)
for a in l:
    for b in l:
        for c in l:
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    result = a*b*c
print(result)

#22.07.25