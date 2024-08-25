from itertools import chain
n = int(input())
# a = 1
# b = ""
if(n == 2 or n == 3):
    print("NO SOLUTION")
else:
  # solution 3
  # for i in range(2,n+1,2):
  #   print(i,end=" ")
  # for i in range(1,n+1,2):
  #   print(i,end=" ")
  # solution 1
  # else:
  #   for i in range(0,n):
  #     if((n-a) > 0):
  #       b += str(n-a) + ' '
  #       a += 2
  #     else:
  #       b += str(n) + " "
  #       a = 2
  # print(b)
  # solution 2
  print(" ".join(list(map(str,chain(range(2,n+1,2),range(1,n+1,2))))))

