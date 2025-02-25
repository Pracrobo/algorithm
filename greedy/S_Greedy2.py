## 1449번 / 수리공 항승


# 파이프에 물이 새는 곳 L.. N (1,000 보다 작은 자연수)
# L 인 테이프 무한개

N, L = map(int, input().split())
coordinates= [False] * 1001 # 0 - 1000 까지의 F로 채워진 점들을 만들듦
for i in map(int, input().split()):
    coordinates = True

x = 0
tape_count = 0
while x < 1001:
    if coordinates[x]:
        tape_count+=1
        x += L
    else:
        x+=1

print(tape_count)


