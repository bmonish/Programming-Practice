import sys
sys.setrecursionlimit(20000)
def findPos(n, k):
    if n == 1:
        return 1
    else:
        return (findPos(n-1, k) + k -1) % n +1;
n, k = map(int, input().split(' '))
print(findPos(n, k))