# Read input, split it into components, convert each to int, and create a list
a = list(map(int, input().split()))
for i in a:
    if i%2==0:
        print(i)