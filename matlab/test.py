z = int(input())

def convertToBinary(n):
    if n > 1:
        convertToBinary(n // 2)
    b.append(n % 2)
    return b


for i in range(z):
    n = int(input())
    t = list(map(int, input().split()))
    t=list(set(t))
    b=[]
    b = convertToBinary(n)
    b=b[::-1]
    # print(b)
    x=0
    for i in t:
        if(i<=len(b)):
            if(b[i-1]==1):
                x+=2**(i-1)

    print(n-x)



