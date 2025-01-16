# n = int(input())
# a = "1"
# b = "2"
# c = "3"


# def tower_of_hanoi(n, a, b, c) -> None:
#     if n == 1:
#         return [f"{a} {c}"]
#     tower1 = tower_of_hanoi(n - 1, a, c, b)
#     tower2 = tower_of_hanoi(n - 1, b, a, c)
#     return [s for s in tower1] + [f"{a} {c}"] + [s for s in tower2]


# print((2**n) - 1)
# print("\n".join(tower_of_hanoi(n, a, b, c)))


r = """1 3"""

for i in range(int(input()) - 1):
    a = r.replace("2", "4")
    a = a.replace("3", "2")
    a = a.replace("4", "3")

    b = r.replace("1", "4")
    b = b.replace("2", "1")
    b = b.replace("4", "2")

    r = a + "\n1 3\n" + b

print(r.count("\n") + 1)
print(r)
