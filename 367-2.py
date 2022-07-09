from bisect import bisect_left,bisect_right

#데이터 개수 반환 함수
def range(arr,l_value,r_value):
    left=bisect_left(arr,l_value)
    right=bisect_right(arr,r_value)
    return right-left

n,x=map(int,input().split())
a=list(map(int,input().split()))

count = range(a,x,x)

if count==0:
    print(-1)
else:
    print(count)