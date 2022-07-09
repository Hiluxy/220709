



def binary(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2

        if arr[mid]==target:
            if mid==target:
                return mid
            else:
                return None
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1

    return None

n=int(input())
a=list(map(int,input().split()))

result=-1
for target in range(n):
    re=binary(a,target,0,n-1)
    if re !=None:
        result=re
print(result)
