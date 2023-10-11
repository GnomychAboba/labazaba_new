def average(num):
    if len(num) == 0:
        return None
    sum_of_num = sum(num)
    count = len(num)
    average_num = sum_of_num / count

    return average_num


number = []
length = int(input("Введите длину: "))
for i in range(length):
    n = int(input("Введите числа: "))
    number.append(n)

print(average(number))
