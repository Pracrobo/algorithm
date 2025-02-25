## 11047번 / 동전 0


#종류 N
# N종류의 합을 K
# 동전 개수의 최소값

# N(1<= N <= 10), K(1 <= K <= 100,000,000)
# 두번째부터 N개 줄에 동전 가치 Ai가 오름차순 (i가 2이상인 경우 Ai 는 Ai-1의배수, A1 = 1, 1<= Ai <= 1,000,000)
##  튜플로 정리해서 합계 내보기!!!

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True) #내림차순변경
count = []
total = 0
for coin in coins:
    if K // coin > 0:
        amount = K // coin
        total += amount
    else:
        amount = 0
    count.append((coin, amount))
    K %= coin

answer = tuple(count)

print(f'coins: {answer}')
print(f'sum: {total}')



