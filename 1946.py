# T = int(input())

# for n in range(1,T+1):
#     N = int(input())
#     test = ''
    
#     for a in range(N):
#         alpa,num = input().split()
#         test += alpa*int(num)
#     print('#{}'.format(n))
#     for i in range(0,len(test),10):
#         print(test[i:i+10])

T = int(input())

for i in range(1,T+1):
    N = int(input())
    test = ''
    for n in range(N):
        alpa,num = input().split()
        test = test + alpa*int(num)
    print('#{}'.format(i))
    for i in range(0,len(test),10):
        print(test[i:i+10])
        
        
        
       
    // print("참 잘했어요")
