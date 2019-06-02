
num = int(input("Enter a number:\n"))

def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)
for i in range(0,num):
    print(str(i),fib(i))
