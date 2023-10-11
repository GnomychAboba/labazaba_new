def elem():
    arr = []
    while True:
        inp = input()
        if inp == "":
            break
        else:
            arr.append(inp)
    return arr


def count_elements(lst):
    element_count = {}

    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    for element, count in element_count.items():
        print(f"{element} | {count}")


ls = elem()
print(count_elements(ls))
