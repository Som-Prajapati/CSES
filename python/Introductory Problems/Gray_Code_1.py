from math import log2, floor

n = 4
# n = int(input())
count = 0


def gray_converter(i: int) -> None:
    if i < (2**n):
        val = i
        arr = [0] * n
        while (i) != 0:
            x = floor(log2(i))
            i -= 2**x
            arr[-(x + 1)] = 1
        print("".join(map(str, arr)))


gray_converter(count)


for i in range(1, (2**n)):
    a = 1
    b = 2
    while True:
        if i % b == 0:
            a = b
            b *= 2
        else:
            sign = (i / a) - (i // b)
            if sign % 2 == 0:
                count -= a
                break
            else:
                count += a
                break
    gray_converter(count)
