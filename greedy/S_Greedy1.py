# Ai는 Ai-1의 배수라서 greedy 가능

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse() #[50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
amount = 0
for coin in coins:
    amount += K // coin
    K %= coin
    print(f'coin: {coin}, K:{K}, amount:{amount}')

print(amount)