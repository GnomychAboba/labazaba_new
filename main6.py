def simple_num(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


number = int(input("Введите число: "))
print(simple_num(number))
