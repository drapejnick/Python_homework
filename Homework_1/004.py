# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input("Введите номер четверти, от 1 до 4: "))

if x == 1:
    print(x, 'четверти соответствуют следующие координаты: x > 0 и y > 0')
elif x == 2:
    print(x, 'четверти соответствуют следующие координаты: x < 0 и y > 0')
elif x == 3:
    print(x, 'четверти соответствуют следующие координаты: x < 0 и y < 0')
elif x == 4:
    print(x, 'четверти соответствуют следующие координаты: x > 0 и y < 0')
else:
    print('Нужно ввести число от 1 до 4')
