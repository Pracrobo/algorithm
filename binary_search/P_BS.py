## 문제 2512번
from bisect import bisect_left, bisect_right
N = int(input())
budges = list(map(int, input().split()))
budges.sort()
M = int(input())

avg = M / N
limit_in = bisect_left(budges, avg)
(M - limit_in) / (N - limit_out)


print(f'지방의 수 : {N}')
print(f'각 지방별 예상 예산액 :{budges}')
print(f'총 예산 수 : {M}')

