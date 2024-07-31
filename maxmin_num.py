a=str(input())
b=[]
for i in a:
    b.append(i)
print(sorted(a))
print("max=",b[-1])
print("second max=",b[-2])
print("min=",b[0])
print("min=",b[1])