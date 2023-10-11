def time_year(x):
    if x < 13:
        if x == 1 or x == 2 or x == 12:
            return 'Зима'
        if x == 3 or x == 4 or x == 5:
            return 'Весна'
        if x == 6 or x == 7 or x == 8:
            return 'Лето'
        if x == 9 or x == 10 or x == 11:
            return 'Осень'
    else:
        return 'Error'


inp = int(input())
print(time_year(inp))
