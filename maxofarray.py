def find_max(arr):
    max=arr[0]
    for num in arr:
        if num>max:        #2>2:false,3>2=True(max=3),4>3=True(max=4),5>4=true(max=5),6>5=true(max=6)
            max=num         
    return max
print(find_max([2,3,4,5,6]))