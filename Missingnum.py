a=list(map(int,input().split()))
print(a)
n=len(a)+1           # length of the list + here we add 1(missing number) ,because missing number is also part of sequence that we want to find
expected_sum=n * (n+1) // 2         #sum of n numbersis n*(n+1)/2    ==Total
actual_sum=sum(a)                   #sum of list                     ==list_total
Missing_value=expected_sum - actual_sum    #Total-list_total   (we get missing value)
print(Missing_value)