# T = int(input())
# for a in range(1,T+1): 
#     N , M = map(int,input().split())
#     A = list(map(int,input().split()))
#     B = list(map(int,input().split()))
#     if N>M:
#         pass
#     else:
#         A,B = B,A
#         N,M = M,N
#     sum_list = []
#     for i in range(N):
#         n = i
#         m = 0
#         sum = 0
#         total = 0
#         if n == N - M +1:
#             break
#         while m<M:
#             total = total + B[m]*A[n]
#             n = n + 1
#             m = m + 1
#         sum_list.append(total)
#     max = sum_list[0]
#     for i in sum_list:
#         if i > max:
#             max = i
#     print('#{} {}'.format(a,max))
    
T = int(input())
for a in range(1,T+1):
    N,M = map(int,input().split())
    A= list(map(int,input().split()))
    B= list(map(int,input().split()))
    if N > M:
        pass
    else:
        N,M = M,N
        A,B = B,A
    sum_list = []
    for i in range(N):
        n = i
        m = 0
        total = 0
        
        if n == N-M+1:
            break
        while m<M:
            total = total + A[n]*B[m]
            n = n+1
            m = m+1
        sum_list.append(total)
    max = sum_list[0]
    for j in sum_list:
        if j > max:
            max = j
    print('#{} {}'.format(a,max))