# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества "))
a = list()
for _ in range (n):
    x = int (input())
    a.append(x)
a = set(a)
print(*a)
m = int(input("Введите количество элементов второго множества "))
b = list()
for _ in range (m):
    x = int (input())
    b.append(x)
b = set(b)
print(*b)

print (*a & b)
