
num = int(input("Enter a number:\n"))
res = [0,1]
def fib(n):
    if(n<=1):
        return n
    else:
        for i in range(2,n+1):
            res.append(res[i-1]+res[i-2])
    return res[n]

print(fib(num))
