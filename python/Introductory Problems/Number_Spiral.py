# Taking inputs
n = int(input())
result = []
for i in range(0,n):
  x,y = map(int,input().split(" "))
  if x > y :
    if x%2!= 0:
      result.append((x-1)**2 + y)
    else:
      result.append(x**2 + 1 - y)
  else:
    if y%2 == 0:
      result.append((y-1)**2 + x)
    else:
      result.append(y**2 + 1 - x)
  result.append(" ")
print("".join(map(str,result)))