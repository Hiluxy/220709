from bisect import bisect_left, bisect_right

n,x=map(int,input().split())
a=list(map(int,input().split()))


right=bisect_right(a,x)
left=bisect_left(a,x)
if right==left:
    print(-1)
else:
    print(right-left)
