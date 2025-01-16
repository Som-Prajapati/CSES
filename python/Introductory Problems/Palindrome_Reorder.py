from collections import Counter


def no_solution() -> None:
    print("NO SOLUTION")


def even_word() -> None:
    for key, value in count.items():
        if value % 2 == 1:
            no_solution()
            exit()

    list = r_list = []
    for key, value in count.items():
        for i in range(value // 2):
            list.append(key)
    r_list = list.copy()
    r_list.reverse()
    print("".join(list + r_list))


def odd_word() -> None:
    counter = 1
    odd_list = []
    list = r_list = []
    for key, value in count.items():
        if value % 2 == 1:
            counter -= 1
            odd_list.append(key)

    if counter == 0:
        for key, value in count.items():
            for i in range(value // 2):
                list.append(key)
        r_list = list.copy()
        r_list.reverse()
        print("".join(list + odd_list + r_list))
    else:
        no_solution()
        exit()


word = str(input())
count = dict(Counter(word))

if len(word) % 2 == 0:
    even_word()

else:
    odd_word()
