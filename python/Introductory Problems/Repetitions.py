l = input()

mc = 0
c = 1
mc = 1 if len(l) > 0 else mc
  
for i in range(1,len(l)):
  if l[i-1]==l[i]:
    c += 1  
  else:
    c = 1
  mc= max(mc,c)

print(mc)
