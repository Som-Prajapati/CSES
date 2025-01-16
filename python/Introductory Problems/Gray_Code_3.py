n = int(input())
# arr = [0] * n

# for i in range(2**n):


#     print("".join(map(str, arr)))
#     for j in range(n):
#         a = 2 ** (n - j)
#         if i % a == ((2 ** (n - j)) / 2 - 1):
#             if arr[j] == 0:
#                 arr[j] = 1
#             else:
#                 arr[j] = 0
def gray_code(n):
    if n == 0:
        return []
    if n == 1:
        return ["0", "1"]
    gray = gray_code(n - 1)
    return ["0" + s for s in gray] + ["1" + s for s in reversed(gray)]


print("\n".join(gray_code(n)))
