n = int(input())
arr = list(map(int, input().split(" ")))
arr.sort(reverse=True)
print(arr)

a = arr.pop(0)
b = 0
for i in range(len(arr)):
    if i == 0:
        b = arr.pop(0)
    else:
        if a >= b:
            if a >= (b + arr[0]):
                b += arr.pop(0)
            else:
                min = -1
                for i in range(len(arr)):
                    x = abs(a - (b + arr[i]))
                    if i == len(arr) - 1:
                        b += arr.pop(i)
                        break
                    elif min == -1 or x < min:
                        min = x
                    else:
                        b += arr.pop(i - 1)
                        break
        else:
            if b >= (a + arr[0]):
                a += arr.pop(0)
            else:
                min = -1
                for i in range(len(arr)):
                    x = abs(b - (a + arr[i]))
                    if i == len(arr) - 1:
                        a += arr.pop(i)
                        break
                    elif min == -1 or x < min:
                        min = x
                    else:
                        a += arr.pop(i - 1)
                        break

print(abs(a - b))
