n = int(input())
arr = list(map(int, input().split()))
count = 0

i = 0
while(i != len(arr)-1):
  if(arr[i] > arr[i+1]):
    count += (arr[i]-arr[i+1])
    arr[i+1]=arr[i]
  i+=1

print(count)
