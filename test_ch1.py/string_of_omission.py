def remove_nums(omit_list):
    num_list = list(range(21))

    for num in num_list:
        if num in omit_list:
            num_list.remove(num)

    return num_list


print(remove_nums([1, 3, 5]))
