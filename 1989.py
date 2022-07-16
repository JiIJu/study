T = int(input())

for n in range(T):
    word = list(input())
    if word == word[::-1]:
        print(f'#{n+1} 1')
    else:
        print(f'#{n+1} 0')
