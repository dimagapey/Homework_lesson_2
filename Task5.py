# 5. В математике функция `sign(x)` (знак числа) определена так:
#    ``
#    sign(x) = 1, если x > 0,
#    sign(x) = -1, если x < 0,
#    sign(x) = 0, если x = 0.
#    ``
#    Для данного числа x выведите значение sign(x).
#    Эту задачу желательно решить с использованием каскадных
#    инструкций if... elif... else.


some_x = int(input('Введите число: '))
if some_x > 0:
    print(1)
elif some_x == 0:
    print(0)
else:
    print(-1)







