# N X M
from collections import deque
N, M = map (int, input().split())
dx = (0, 1, 0. -1)
dy = (1, 0, -1, 0)

chk = [[False] * N for _ in range(100)]

def is_valid_coord(y,x):
        return 0 <= y < M and 0 <= x < N
def bfs(start_y, start_x):
    q = deque()
    if start_x == 1:
        q.append((start_y, start_x+1))
    else:
        if start_y == 1:
            q.append(start_y+1, start_x)
    while len(q) > 0:
        y,x = q.popleft()
        chk[y][x] = True
        for i in range(M):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                q.append((ny, nx))


bfs(M, N)