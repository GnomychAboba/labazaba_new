def elem():
    arr = []
    while True:
        inp = input()
        if inp == "":
            break
        else:
            arr.append(inp)
    return arr

print(elem())