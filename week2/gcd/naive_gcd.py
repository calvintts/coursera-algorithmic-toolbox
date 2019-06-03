num1 = int(input("Enter first number:\n"))
num2 = int(input("Enter second number:\n"))
res = 0
zero = int(0)
lower = min(num1,num2)
for i in range(1,lower+1):
    if(num1%i==zero and num2%i==zero):
        res = i
print(res)
