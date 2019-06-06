# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    res= [0,1]
    if(n<=1):
        return n
    else:
        for i in range(2,n+1):
            res.append((res[i-1]+res[i-2])%10)
    return res[n]

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
