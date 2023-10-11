def fib(x):
    if x == 0:
        return 0
    if x < 2:
        return 1
    return fib(x-2) + fib(x-1)


n = int(input("Введите количество чисел!!: "))
for i in range(n):
    print(fib(i), end=" ")
