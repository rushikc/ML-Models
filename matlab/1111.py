z=int(input())
for j in range(z):
    n=int(input())
    b=bin(n)
    b=b[2:]
    t=list(map(int,input().split()))


    x=0
    b=b[::-1]
    #print(b)
    #print(t)
    for i in t:
        if(i<=len(b)):
            if(b[i-1]=='1'):
                x+=2**(i-1)
            #print("entered ")
    print(n-x)