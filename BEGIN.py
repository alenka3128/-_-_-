# Begin1. Дана сторона квадрата a. Найти его периметр P = 4·a.
a = float(input())
perimeter = 4 * a
print(perimeter)

# Begin2. Дана сторона квадрата a. Найти его площадь S = a².
a = float(input())
area = a ** 2
print(area)

# Begin3. Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b).
a = float(input())
b = float(input())
area = a * b
perimeter = 2 * (a + b)
print(area)
print(perimeter)

# Begin4. Дан диаметр окружности d. Найти ее длину L = π·d.
d = float(input())
pi = 3.14
length = pi * d
print(length)

# Begin5. Дана длина ребра куба a. Найти объем куба V = a³ и площадь его поверхности S = 6·a².
a = float(input())
volume = a ** 3
surface_area = 6 * (a ** 2)
print(volume)
print(surface_area)

# Begin6. Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c).
a = float(input())
b = float(input())
c = float(input())
volume = a * b * c
surface_area = 2 * (a * b + b * c + a * c)
print(volume)
print(surface_area)

# Begin7. Найти длину окружности L и площадь круга S заданного радиуса R.
R = float(input())
pi = 3.14
length = 2 * pi * R
area = pi * (R ** 2)
print(length)
print(area)

# Begin8. Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2.
a = float(input())
b = float(input())
average = (a + b) / 2
print(average)

# Begin9. Даны два неотрицательных числа a и b. Найти их среднее геометрическое: √(a·b).
import math
a = float(input())
b = float(input())
geometric_mean = math.sqrt(a * b)
print(geometric_mean)

# Begin10. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.
a = float(input())
b = float(input())
a_sq = a ** 2
b_sq = b ** 2
sum_sq = a_sq + b_sq
diff_sq = a_sq - b_sq
prod_sq = a_sq * b_sq
quot_sq = a_sq / b_sq
print(sum_sq)
print(diff_sq)
print(prod_sq)
print(quot_sq)

# Begin11. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей.
a = float(input())
b = float(input())
mod_a = abs(a)
mod_b = abs(b)
sum_mod = mod_a + mod_b
diff_mod = mod_a - mod_b
prod_mod = mod_a * mod_b
quot_mod = mod_a / mod_b
print(sum_mod)
print(diff_mod)
print(prod_mod)
print(quot_mod)

# Begin12. Даны катеты прямоугольного треугольника a и b. Найти его гипотенузу c и периметр P.
import math
a = float(input())
b = float(input())
c = math.sqrt(a ** 2 + b ** 2)
perimeter = a + b + c
print(c)
print(perimeter)

# Begin13. Даны два круга с общим центром и радиусами R1 и R2 (R1 > R2). Найти площади этих кругов S1 и S2, а также площадь S3 кольца.
R1 = float(input())
R2 = float(input())
pi = 3.14
S1 = pi * (R1 ** 2)
S2 = pi * (R2 ** 2)
S3 = S1 - S2
print(S1)
print(S2)
print(S3)

# Begin14. Дана длина L окружности. Найти ее радиус R и площадь S круга.
L = float(input())
pi = 3.14
R = L / (2 * pi)
S = pi * (R ** 2)
print(R)
print(S)

# Begin15. Дана площадь S круга. Найти его диаметр D и длину L окружности.
S = float(input())
pi = 3.14
import math
R = math.sqrt(S / pi)
D = 2 * R
L = 2 * pi * R
print(D)
print(L)

# Begin16. Найти расстояние между двумя точками с заданными координатами x1 и x2 на числовой оси.
x1 = float(input())
x2 = float(input())
distance = abs(x2 - x1)
print(distance)

# Begin17. Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму.
x1 = float(input())  # A
x2 = float(input())  # B
x3 = float(input())  # C
AC = abs(x3 - x1)
BC = abs(x3 - x2)
total = AC + BC
print(AC)
print(BC)
print(total)

# Begin18. Даны три точки A, B, C на числовой оси. Точка C расположена между точками A и B. Найти произведение длин отрезков AC и BC.
x1 = float(input())  # A
x2 = float(input())  # B
x3 = float(input())  # C
AC = abs(x3 - x1)
BC = abs(x3 - x2)
product = AC * BC
print(product)

# Begin19. Даны координаты двух противоположных вершин прямоугольника. Найти периметр и площадь.
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
width = abs(x2 - x1)
height = abs(y2 - y1)
perimeter = 2 * (width + height)
area = width * height
print(perimeter)
print(area)

# Begin20. Найти расстояние между двумя точками с заданными координатами (x1, y1) и (x2, y2) на плоскости.
import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(distance)