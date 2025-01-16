n  = int(input())
sum = (n*(n+1)/2)
temp = sum / 2
list1 , list2 = [] , []

if sum%2  == 1:
  print("NO")
  exit()
else:
  print("YES")
  for i in range(n , 0 , -1):
    if (i <= temp):
      list1.append(i)
      temp -= i
    else:
      list2.append(i)

print(len(list1))
print(" ".join(str(num) for num in list1))
print(len(list2))
print(" ".join(str(num) for num in list2))
