# Напишите алгоритм, заполняющий список произвольными целыми 

# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
n=4
while n!=len(numbers):
    numbers.append(random.randint(-100,100))
print(numbers)

# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here
