from math import log2, floor

n = int(input())
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
    if i % 2 == 1:
        sign = i - (i // 2)
        if sign % 2 == 0:
            count -= 1
        else:
            count += 1
    else:
        a = 2
        b = 4
        x = i / 2
        while x % b == 0:
            x /= b
            a *= b
            b *= 2
        while x % 2 == 0:
            x /= 2
            a *= 2
        sign = (i / a) - -(i // (a * 2))
        if sign % 2 == 0:
            count -= a
        else:
            count += a
    gray_converter(count)
