n = int(input())
list = sum(map(int,input().split()))
total = int(n*(n+1)/2)
print(total - list)
