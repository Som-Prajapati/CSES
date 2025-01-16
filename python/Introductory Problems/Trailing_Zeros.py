import math

n = int(input())
result = 0
loop = int(math.log(n , 5)//1)
for i in range(loop , 0 , -1):
  result += n//5**i
print(result)