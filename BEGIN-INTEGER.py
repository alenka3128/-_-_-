# Begin22. Поменять местами содержимое переменных A и B
A = float(input())
B = float(input())
A, B = B, A
print(A)
print(B)

# Begin25. Найти значение функции y = 3x⁶ − 6x² − 7.
x = float(input())
y = 3 * (x ** 6) - 6 * (x ** 2) - 7
print(y)

# Begin29. Дано значение угла α в градусах (0 < α < 360). Определить значение этого же угла в радианах.
alpha_deg = float(input())
pi = 3.14
alpha_rad = alpha_deg * pi / 180
print(alpha_rad)

# Integer1. Дано расстояние L в сантиметрах. Найти количество полных метров в нем.
L = int(input())
meters = L // 100
print(meters)

# Integer5. Даны целые положительные числа A и B (A > B). Найти длину незанятой части отрезка A.
A = int(input())
B = int(input())
remainder = A % B
print(remainder)

# Begin23. Даны переменные A, B, C. Переместить: A -> B, B -> C, C -> A.
A = float(input())
B = float(input())
C = float(input())
A, B, C = C, A, B
print(A)
print(B)
print(C)

# Begin24. Даны переменные A, B, C. Переместить: A -> C, C -> B, B -> A.
A = float(input())
B = float(input())
C = float(input())
A, B, C = B, C, A
print(A)
print(B)
print(C)

# Begin26. Найти значение функции y = 4·(x−3)⁶ − 7·(x−3)³ + 2.
x = float(input())
t = x - 3
y = 4 * (t ** 6) - 7 * (t ** 3) + 2
print(y)

# Begin27. Вычислить A⁸, используя вспомогательную переменную и три операции умножения.
A = float(input())
A2 = A * A
A4 = A2 * A2
A8 = A4 * A4
print(A2)
print(A4)
print(A8)

# Begin28. Вычислить A¹⁵, используя две вспомогательные переменные и пять операций умножения.
A = float(input())
A2 = A * A
A3 = A2 * A
A5 = A3 * A2
A10 = A5 * A5
A15 = A10 * A5
print(A2)
print(A3)
print(A5)
print(A10)
print(A15)

# Begin30. Дано значение угла α в радианах. Определить значение этого же угла в градусах.
alpha_rad = float(input())
pi = 3.14
alpha_deg = alpha_rad * 180 / pi
print(alpha_deg)

# Begin31. Дано значение температуры T в градусах Фаренгейта. Определить значение в градусах Цельсия.
TF = float(input())
TC = (TF - 32) * 5 / 9
print(TC)

# Begin32. Дано значение температуры T в градусах Цельсия. Определить значение в градусах Фаренгейта.
TC = float(input())
TF = TC * 9 / 5 + 32
print(TF)

# Begin33. X кг конфет стоит A рублей. Определить, сколько стоит 1 кг и Y кг этих же конфет.
X = float(input())
A = float(input())
Y = float(input())
price_per_kg = A / X
price_Y = price_per_kg * Y
print(price_per_kg)
print(price_Y)

# Begin34. X кг шоколадных конфет стоит A рублей, Y кг ирисок стоит B рублей.
X = float(input())
A = float(input())
Y = float(input())
B = float(input())
price_choc = A / X
price_toff = B / Y
ratio = price_choc / price_toff
print(price_choc)
print(price_toff)
print(ratio)

# Begin35. Путь лодки: по озеру T1 ч (скорость V), против течения T2 ч (скорость V - U).
V = float(input())
U = float(input())
T1 = float(input())
T2 = float(input())
S = V * T1 + (V - U) * T2
print(S)

# Begin36. Расстояние между автомобилями через T часов, если они удаляются друг от друга.
V1 = float(input())
V2 = float(input())
S = float(input())
T = float(input())
new_distance = S + (V1 + V2) * T
print(new_distance)

# Integer2. Дана масса M в килограммах. Найти количество полных тонн в ней.
M = int(input())
tons = M // 1000
print(tons)

# Integer3. Дан размер файла в байтах. Найти количество полных килобайтов (1 КБ = 1024 Б).
bytes_size = int(input())
kb_size = bytes_size // 1024
print(kb_size)

# Integer4. Даны целые положительные числа A и B (A > B). Найти количество отрезков B на отрезке A.
A = int(input())
B = int(input())
count = A // B
print(count)