N = int(input())
req = list(map(int, input().split()))
M = int(input())

low = 0
high = max(req)
middle = (low+high) // 2
ans = 0


def is_possible(middle):
     ## 원래 여기 부분이 얼마나 어려운가에 따라 나뉨
    return sum(min(r, middle) for r in req) <= M


while low <= high:
    if is_possible(middle):
        low = middle + 1
        ans = middle
    else:
        high = middle - 1

    middle = (low + high) // 2


print(ans)

