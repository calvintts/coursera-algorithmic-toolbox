# Uses python3

def lcm_naive(a, b):
    for i in range(1,a+1):
        if(b*i%a==0):
            return b*i


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))
