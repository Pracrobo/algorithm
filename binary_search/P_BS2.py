# 10815번 숫자카드

from bisect import bisect_left, bisect_right

N = int(input()) # _ = int(input())
cards = sorted(map(int, input().split()))
M = int(input()) # _ = int(input())
match = list(map(int, input().split()))

# 반복문 O(MN) : 500,000 * 500,000 = 250,000,000,000 (시간초과)
# 이분탐색 : logN * M = 500,000 * M
ans = []
for m in match:
    l = bisect_left(cards, m)
    r = bisect_right(cards, m)
    ans.append(1 if r - l > 0 else 0) # l if r - l else 0

# print('', join(map(str, ans))
print(*ans)