N = int(input())

if N >1000:
    a= N//1000
    N = N%1000
    b = N//100
    N = N%100
    c = N//10
    N = N%10
    print(a+b+c+N)
elif N>100:
    a=N//100
    N=N%100
    b=N//10
    N=N%10
    print(a+b+N)
elif N>10:
    a=N//10
    N=N%10
    print(a+N)
else:
    print(N)