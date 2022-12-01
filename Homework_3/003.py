# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

# Первый вариант
list = [1.1, 1.2, 3.1, 10.01]
new_lst = [round(i % 1, 2) for i in list]
print(max(new_lst) - min(new_lst))

# Второй вариант
list = [1.1, 1.2, 3.1, 10.01]
a = []
for i in range(len(list)):
    res = list[i] - int(list[i])
    a.append(res)

max = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]

min = 10*100
for i in range(len(a)):
    if a[i] < min:
        min = a[i]

result_ = max - min
print(round(result_, 2))
