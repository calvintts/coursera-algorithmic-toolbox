# Uses python3
def calc_fib(n):
    res= [0,1]
    if(n<=1):
        return n
    else:
        for i in range(2,n+1):
            res.append(res[i-1]+res[i-2])
    return res[n]

n = int(input())
print(calc_fib(n))
