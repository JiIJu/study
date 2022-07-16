N = int(input())

s = list(map(int,input().split()))

s.sort()

#a = (N-1)/2
print(s[int((len(s)-1)/2)])