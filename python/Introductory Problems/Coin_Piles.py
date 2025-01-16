n  = int(input())
l = []
for i in range(n):
  a , b = map(int, input().split())
  if abs(a - b) <= (max(a , b) / 2) and ((a + b) % 3 == 0) :
    l.append("YES")
  else:
    l.append("NO")
  l.append("\n")
  
print("".join(l))

