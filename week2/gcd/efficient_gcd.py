num1 = int(input("Enter first number:\n"))
num2 = int(input("Enter second number:\n"))
res = int(0)
lower = min(num1,num2)
def gcd(a,b):
    if(b==0):
        return a
    else:
        print(a,b)
        return gcd(b,int(a%b))
print(gcd(num1,num2))
