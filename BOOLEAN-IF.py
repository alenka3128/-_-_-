# Boolean 1. «Число A является положительным»

A = int(input())
result = A > 0
print(result)

# Boolean 2. «Число A является нечетным»

A = int(input())
result = (A % 2 != 0)
print(result)

# Boolean 3. «Число A является четным»

A = int(input())
result = (A % 2 == 0)
print(result)

# Boolean 4. «Справедливы неравенства A > 2 и B ≤ 3»

A, B = map(int, input().split())
result = (A > 2) and (B <= 3)
print(result)

# Boolean 5. «Справедливы неравенства A ≥ 0 или B < −2»

A, B = map(int, input().split())
result = (A >= 0) or (B < -2)
print(result)

# Boolean 6. «Справедливо двойное неравенство A < B < C»

A, B, C = map(int, input().split())
result = (A < B) and (B < C)
print(result)

# Boolean 7. «Число B находится между числами A и C»

A, B, C = map(int, input().split())
result = ((A < B < C) or (C < B < A))
print(result)

# Boolean 8. «Каждое из чисел A и B нечетное»

A, B = map(int, input().split())
result = (A % 2 != 0) and (B % 2 != 0)
print(result)

# Boolean 9. «Хотя бы одно из чисел A и B нечетное»

A, B = map(int, input().split())
result = (A % 2 != 0) or (B % 2 != 0)
print(result)

# Boolean 10. «Ровно одно из чисел A и B нечетное»

A, B = map(int, input().split())
result = (A % 2 != 0) != (B % 2 != 0)  # XOR через неравенство булевых
print(result)

# Boolean 11. «Числа A и B имеют одинаковую четность»

A, B = map(int, input().split())
result = (A % 2) == (B % 2)
print(result)

# Boolean 12. «Каждое из чисел A, B, C положительное»

A, B, C = map(int, input().split())
result = (A > 0) and (B > 0) and (C > 0)
print(result)

# Boolean 13. «Хотя бы одно из чисел A, B, C положительное»

A, B, C = map(int, input().split())
result = (A > 0) or (B > 0) or (C > 0)
print(result)

# Boolean 14. «Ровно одно из чисел A, B, C положительное»

A, B, C = map(int, input().split())
count_positive = (1 if A > 0 else 0) + (1 if B > 0 else 0) + (1 if C > 0 else 0)
result = (count_positive == 1)
print(result)

# Boolean 15. «Ровно два из чисел A, B, C являются положительными»

A, B, C = map(int, input().split())
count_positive = (1 if A > 0 else 0) + (1 if B > 0 else 0) + (1 if C > 0 else 0)
result = (count_positive == 2)
print(result)

# If 1. Если положительное — прибавить 1, иначе не менять

x = int(input())
if x > 0:
    x += 1
print(x)

# If 2. Если положительное — +1, иначе −2

x = int(input())
if x > 0:
    x += 1
else:
    x -= 2
print(x)

# If 3. Положительное → +1, отрицательное → −2, ноль → 10

x = int(input())
if x > 0:
    x += 1
elif x < 0:
    x -= 2
else:  # x == 0
    x = 10
print(x)

# If 4. Количество положительных среди трёх чисел

A, B, C = map(int, input().split())
count = 0
if A > 0: count += 1
if B > 0: count += 1
if C > 0: count += 1
print(count)

# If 5. Количество положительных и количество отрицательных среди трёх чисел

A, B, C = map(int, input().split())
pos = 0
neg = 0
for x in (A, B, C):
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
print(pos, neg)