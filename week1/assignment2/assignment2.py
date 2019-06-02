#python3
def find_max(arr):
    n = len(arr)
    first = 0
    second = 0
    for i in range(n):
        if(arr[i]>first):
            second = first
            first = arr[i]
        elif(arr[i]>second):
            second = arr[i]
    return first*second

input_n = int(input())
input_numbers = [int(x) for x in input().split()]
print(find_max(input_numbers))
