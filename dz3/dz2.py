import random
N = int (input('Введите длину массива '))
X = int (input('Какое число ищем? '))
arr = []
index = 0
for i in range(N):
    n = random.randint(2,7)
    arr.append(n)

res = abs(X - arr[0])
for i in range(1,N):
    temp = abs (X - arr[i])
    if temp < res:
        res = temp
        index = i 

print(arr)         
print(f'Ближайшее к искомому числу {X} - это {arr[index]}')