# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка.

x = int(input("Введите координаты точки х: "))
y = int(input("Введите координаты точки y: "))

if x > 0 and y > 0:
    print('Указанные коордианты находятся в 1 четверти плоскости')
elif x < 0 and y > 0:
    print('Указанные коордианты находятся в 2 четверти плоскости')
elif x < 0 and y < 0:
    print('Указанные коордианты находятся в 3 четверти плоскости')
elif x > 0 and y < 0:
    print('Указанные коордианты находятся в 4 четверти плоскости')
elif x == 0 or y == 0:
    print('Заданные коордианты не должны быть равны 0')
