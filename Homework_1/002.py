# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and
# ⋁ - or
# ¬ - not

List_X = [0, 1]
List_Y = [0, 1]
List_Z = [0, 1]

for i in List_X:
    for j in List_Y:
        for k in List_Z:
            if (not (List_X[i] or List_Y[j] or List_Z[k]) ==
                    (not List_X[i] and not List_Y[j] and not List_Z[k])):
                print('True')
else:
    print('False')
