from math import pow

n = int(input())
a = 1
while(a!=n+1):
  if a == 1 :
    result = 0
  elif a == 2:
    result = 6
  elif a == 3:
    result = 28
  else:
  
    result =( pow(a,2) * (pow(a , 2) - 1) / 2) - ((10 + (a - 4) * 4) * (a - 2)) - (4 + (a - 4 ) *  2 )
  a += 1  
  print(int(result))