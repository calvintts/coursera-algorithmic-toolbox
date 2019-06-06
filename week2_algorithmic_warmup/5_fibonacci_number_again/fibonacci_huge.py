# Uses python3
import sys

def calc_fib(n):
    res= [0,1]
    if(n<=1):
        return n
    else:
        for i in range(2,n+1):
            res.append(res[i-1]+res[i-2])
    return res[n]

def fib_pattern(n):
    res= [0,1]
    if(n<=1):
        return n
    else:
        for i in range(2,pow(2,n)+2):
            res.append((res[i-1]+res[i-2])%n)
            if(res[-2:]==[0,1] and len(res)>2):
                return res[:-2]
    return res

def get_fibonacci_huge_naive(n, m):
    if(n<m):
        return calc_fib(n)%m
    else:
        periodic = fib_pattern(m)
        return periodic[n%len(periodic)]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))
