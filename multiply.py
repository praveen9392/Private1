a=int(input())
b=10
for i in range(b+1):
    print(a,"*",i,"=",a*i)

# Pointer: a pointer is a variable which is used to store the memory location of another variable
#we cam create pointer in this way in python by using object references  
x=5
y=x
print(id(x))
print(id(y))