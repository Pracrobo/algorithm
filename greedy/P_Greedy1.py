## 11047번 / 동전 0


#종류 N
# N종류의 합을 K
# 동전 개수의 최소값

# N(1<= N <= 10), K(1 <= K <= 100,000,000)
# 두번째부터 N개 줄에 동전 가치 Ai가 오름차순 (i가 2이상인 경우 Ai 는 Ai-1의배수, A1 = 1, 1<= Ai <= 1,000,000)
##  튜플로 정리해서 합계 내보기!!!

N, K = map(int, input())
coins = [int(input()) for _ in range (N)]
for coin in coins:
    if K / coin == 0: # 만약 coins의 리스트 값에 값/coin == 0 인게ㅇ 있다면
        amount = K % coin  #amount에 값을 계산해서 갯수 넣어주고
        coins.tuple = (coin, amount) # 튜플로
    else:
        coins.tuple(coin, 0)



