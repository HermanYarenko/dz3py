import random
N = int (input('Введите длину массива '))
X = int (input('Какое число ищем? '))
arr = []
count = 0
for i in range(N):
    n = random.randint(1,9)
    arr.append(n)
for i in range(len(arr)):
    if arr[i] == X:
        count += 1
print(arr)
print(f'Искомое число {X} встречается в массиве  {count} раз(а)')