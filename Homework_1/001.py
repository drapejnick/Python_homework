# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input("Введите число обозначающее день недели, от 1 до 7: "))

if (number == 6) or (number == 7):
    print('Да, это выходной день')
elif (number > 0) and (number < 6):
    print('Нет, это будний день')
else:
    print('Вы ввели некорретное число')
