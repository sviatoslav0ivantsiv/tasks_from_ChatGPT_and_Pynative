def first_last_same(n):
    print ("Given numers:", n)

    first_number = n[0]
    last_number = n[-1]

    if first_number == last_number:
        return (True)
    else:
        return (False)


numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))